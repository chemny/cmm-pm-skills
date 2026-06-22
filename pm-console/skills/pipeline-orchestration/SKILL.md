---
name: pipeline-orchestration
description: "cmm-pm-skills 全流水线的图谱、项目状态台账规范与协同/守门规则。当需要统筹一个产品项目（这个项目走到哪了、下一步该跑哪个阶段、产出存哪、续接之前的项目、协同/调度 PM 流程、/cmm-pm）时加载。它定义阶段→命令→产物的映射、_state.yaml 结构、进度看板格式与守门规则；不执行阶段本身、不硬调用其它插件命令。"
---

# Pipeline Orchestration（流水线总协同知识）

cmm-pm-skills 是一套端到端 PM 流水线。本技能是它的"协同层知识"：流水线图谱、项目台账规范、看板格式、守门规则。`/cmm-pm` 命令据此领航。

## 核心原则

- **协同 ≠ 执行**：本层只管"项目走到哪、下一步敲什么、门过没过"，**不产出阶段成果**（那是各阶段命令的事）。
- **零侵入**：只**读**各阶段产出的 markdown，从不修改它们；阶段命令完全不知道协同层存在。
- **不硬调用跨插件命令**：插件独立安装，只能用人话建议用户去敲 `/xxx`（守 repo 的 No cross-plugin references）。
- **用户是决策者**（CONVENTIONS §0a/§0c）：每阶段结尾的"风险结论→拍板"是硬门，门没过不放行下一阶段。

## 流水线图谱（阶段 → 命令 → 产物 → 归属）

| n | 阶段 | 阶段 key | 命令 | 产物（存 `_runs/<项目>/`） | 归属 |
|---|---|---|---|---|---|
| 01 | 市场分析 | `market-analysis` | `/market-analysis` | `01-市场分析.md` | PM |
| 02 | 需求洞察 | `insight` | `/insight` | `02-需求洞察.md` | PM |
| 03 | 产品战略 | `strategy` | `/strategy` | `03-产品战略.md` | PM |
| 04 | PRD | `prd` | `/write-prd` | `04-PRD.md` | PM |
| 05 | 界面设计 | `wireframe` | `/wireframe` | `05-界面设计.md` (+ `05-原型.html`) | PM |
| 06 | 技术方案 | `tech-design` | `/tech-design` | `06-技术方案.md` | ⚙️ 工程提案 |
| 07 | 用户故事 | `stories` | `/write-stories` | `07-用户故事.md` | PM |
| 08 | 测试 | `test` | `/test-scenarios` | `08-测试.md` | PM |
| 09 | 研发 | `dev` | —（外部 / Superpowers） | （代码，不在本套件） | ⚙️ 外部 |
| 10 | 上线 | `launch` | `/plan-launch` `/battlecard` `/growth-strategy` | `10-上线.md` | PM |
| 11 | 数据/迭代 | `data` | `/analyze-cohorts` `/north-star` `/analyze-test` | `11-数据迭代.md` | PM |

依赖细节（领航时用来判断"能不能进"）：②吃①；③吃①②；④吃①②③；⑤吃④；⑦吃④⑤；⑥吃④⑤⑦；⑧吃⑦；⑪的指标回到②形成闭环。

## 项目台账 `_runs/<项目slug>/_state.yaml`

唯一的跨会话状态源。结构：

```yaml
project: sayit
title: sayit 个性化语音输入法
created: 2026-06-22          # 绝对日期，不写"今天"
next: strategy              # 下一步该跑的阶段 key
open_risks:
  - "家长付费意愿未一手验证"
stages:
  market-analysis: { status: done,    artifact: 01-市场分析.md, gate: passed }
  insight:         { status: done,    artifact: 02-需求洞察.md, gate: passed }
  strategy:        { status: pending, artifact: null,          gate: null }
  prd:             { status: pending, artifact: null,          gate: null }
  wireframe:       { status: pending, artifact: null,          gate: null }
  tech-design:     { status: pending, artifact: null,          gate: null }
  stories:         { status: pending, artifact: null,          gate: null }
  test:            { status: pending, artifact: null,          gate: null }
  launch:          { status: pending, artifact: null,          gate: null }
  data:            { status: pending, artifact: null,          gate: null }
```

- `status`: `pending` | `in-progress` | `done`
- `gate`: `null`（未拍板）| `passed`（用户放行）| `revise`（要回去补）| `pivot`（改方向）
- **台账与磁盘以磁盘为准**：若 `_runs/<项目>/` 里有产物 md 但台账没记，按产物反推并修正台账（§9 不假装）。

## 进度看板（每次输出给用户）

```
项目：sayit · 进度 2/10 · 下一步：③ 产品战略 /strategy
① 市场分析   ✅ done   01-市场分析.md
② 需求洞察   ✅ done   02-需求洞察.md
③ 产品战略   ⬜ next   —
④ PRD …      ⬜
…
未决风险：家长付费意愿未一手验证
```

## 守门规则

1. 某阶段产物已存在但 `gate: null` → **先把该阶段的"风险结论"摘给用户、请他拍板**，再决定 `next`，绝不自动连跑。
2. 依赖未满足（如想跑④但③还没 done）→ 提示先补上游，不硬拦也不替他改需求（§0b）。
3. 闭环：⑪ 完成后，`next` 指回 ②（带上⑪的指标作为新输入）。
4. 每次输出结尾，给一行明确的「下一步敲什么」。
