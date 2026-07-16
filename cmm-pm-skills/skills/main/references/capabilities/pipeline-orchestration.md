---
name: pipeline-orchestration
description: "cmm-pm-skills 全流水线的图谱、项目状态台账规范与协同/守门规则。当需要统筹一个产品项目（这个项目走到哪了、下一步该跑哪个阶段、产出存哪、续接之前的项目、协同/调度 PM 流程、/cmm-pm-skills）时加载。它定义阶段→命令→产物的映射、_state.yaml 结构、进度看板格式与守门规则；本层本身不产出阶段成果，由总入口按环境能力代跑或给出下一步命令。"
scenarios: ["这个项目走到哪一步了下一步跑啥", "帮我统筹下整个产品流程", "续接之前那个项目继续推进"]
---

# Pipeline Orchestration（流水线总协同知识）

cmm-pm-skills 是一套端到端 PM 流水线。本技能是它的"协同层知识"：流水线图谱、项目台账规范、看板格式、守门规则。`/cmm-pm-skills` 命令据此领航。

## 核心原则

- **协同 ≠ 阶段产物本身**：本层只管"项目走到哪、下一步跑什么、门过没过"，**不直接产出阶段成果**（那是各阶段命令的事）；`/cmm-pm-skills` 可按环境能力代跑阶段，不能代跑时就给出下一步命令。
- **零侵入**：只**读**各阶段产出的 markdown，从不修改它们；阶段命令完全不知道协同层存在。
- **不硬调用跨插件命令**：插件独立安装，跨插件只能用人话建议；本插件内阶段命令可由总入口领航/代跑，或作为下一步命令提示给用户。
- **用户是决策者**（CONVENTIONS §0a/§0c）：每阶段结尾的"风险结论→拍板"是硬门，门没过不放行下一阶段。

## 流水线图谱（阶段 → 命令 → 识别关键词 → 归属）

阶段一律按**关键词**识别（文件名或文档首行标题命中任一即算该阶段）。**文件名前缀数字是"运行序号"，不是阶段号**——同一阶段可能迭代多份、可能有 pivot，序号只表示产出先后。

| 序 | 阶段 | 阶段 key | 命令 | 识别关键词（文件名/标题命中即算） | 归属 |
|---|---|---|---|---|---|
| ① | 市场分析 | `market-analysis` | `/market-analysis` | 市场分析 / 市场调研 / 五看 / market | PM |
| ② | 需求洞察 | `insight` | `/insight` | 需求洞察 / insight / JTBD | PM |
| ③ | 产品战略 | `strategy` | `/strategy` | 产品战略 / 战略 / strategy | PM |
| ④ | PRD | `prd` | `/write-prd` | PRD / 产品需求 | PM |
| ⑤ | 界面设计 | `wireframe` | `/wireframe` | 界面 / UI / 线框 / 原型 / wireframe / spec / prototype / diagrams | PM |
| ⑥ | 用户故事 | `stories` | `/write-stories` | 用户故事 / backlog / stories | PM |
| ⑦ | 技术方案 | `tech-design` | `/tech-design` | 技术方案 / tech-design / tech-arch / 架构 | ⚙️ 工程提案 |
| ⑧ | 测试 | `test` | `/test-scenarios` | 测试 / test | PM |
| ⑨ | 研发 | `dev` | —（外部 / Superpowers） | （代码，不跟踪） | ⚙️ 外部 |
| ⑩ | 上线 | `launch` | `/plan-launch` `/battlecard` `/growth-strategy` | 上线 / GTM / launch / battlecard | PM |
| ⑪ | 数据/迭代 | `data` | `/analyze-cohorts` `/north-star` `/analyze-test` | 数据 / 迭代 / cohort / north star / 指标 | PM |

依赖细节（领航时用来判断"能不能进"）：②吃①；③吃①②；④吃①②③；⑤吃④；⑥吃④⑤；⑦吃④⑤⑥；⑧吃⑥⑦；⑪的指标回到②形成闭环。

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
  market-analysis: { status: done,    artifact: 01-市场分析.md, research_gate: pass-strong, decision_gate: passed }
  insight:         { status: done,    artifact: 02-需求洞察.md, research_gate: pass-with-gaps, decision_gate: passed }
  strategy:        { status: pending, artifact: null,          research_gate: null, decision_gate: null }
  prd:             { status: pending, artifact: null,          research_gate: null, decision_gate: null }
  wireframe:       { status: pending, artifact: null,          research_gate: null, decision_gate: null }
  stories:         { status: pending, artifact: null,          research_gate: null, decision_gate: null }
  tech-design:     { status: pending, artifact: null,          research_gate: null, decision_gate: null }
  test:            { status: pending, artifact: null,          research_gate: null, decision_gate: null }
  launch:          { status: pending, artifact: null,          research_gate: null, decision_gate: null }
  data:            { status: pending, artifact: null,          research_gate: null, decision_gate: null }
```

- `status`: `pending` | `in-progress` | `done`
- `research_gate`: `null` | `pass-strong` | `pass-emerging` | `pass-with-gaps` | `revise` | `blocked`。定义见 [`Deep Research Contract`](../contracts/deep-research-contract.md)。依赖外部事实的阶段必须先过此门。
- `decision_gate`: `null`（未拍板）| `draft`（草案跑通，未正式拍板）| `passed`（用户放行）| `revise`（用户要求补）| `pivot`（改方向）。
- 兼容旧台账：旧字段 `gate` 只可迁移为 `decision_gate`，绝不能推断 `research_gate` 已通过。
- **台账与磁盘以磁盘为准**：台账缺失/过期时，扫 `_runs/<项目>/*`（含 `.md` 与 `.html`），按上表**关键词**（文件名或首行标题）反推阶段；识别不了的就**问用户**，不硬猜（§9 不假装）。
- **前缀=运行序号**：文件名数字前缀只表先后、允许同阶段多份，**绝不**当阶段号用。
- **同阶段多产物 → 最新为准**：取序号最大的那份作为该阶段当前产物（`status: done`），可在备注记迭代次数。
- **识别 pivot**：若出现两条产品线（如先"会议纪要"后"sayit"），以**最新线**为当前状态，旧线在 `notes` 标注"已 pivot 弃用"，不混算。
- **保存约定**：产物建议存 `_runs/<项目>/NN-阶段名-产品.md`（NN=运行序号，迭代不覆盖旧份）。阶段命令不强制此命名，故 console 领航"下一步"时**顺带提示按此保存到项目目录**，保证下次扫盘可靠。

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

1. 依赖外部事实的阶段先检查 `research_gate`。`revise` → 生成delta-query回退补搜；`blocked` → 报告决策缺口并转一手研究/POC；未过研究门不得仅凭文档存在标`done`。
2. `pass-emerging/pass-with-gaps` 可交付，但必须把证据等级、未知与验证要求传给下游；不得静默升级为事实。
3. 某阶段产物已存在但 `decision_gate: null` → **先把该阶段的"风险结论"摘给用户、请他拍板**，再决定 `next`，绝不自动连跑。
4. 下游继承前检查上游研究新鲜度。新增事实、过期事实、承重事实做增量复核；“继承”不等于免检。
5. 依赖未满足（如想跑④但③还没 done）→ 提示先补上游，不硬拦也不替他改需求（§0b）。
6. 闭环：⑪ 完成后，`next` 指回 ②（带上⑪的指标作为新输入）。
7. 每次输出结尾，给一行明确的「下一步敲什么」。
