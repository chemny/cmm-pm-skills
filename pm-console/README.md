# pm-console — cmm-pm-skills 总协同

## Overview / 总览

`pm-console` 是 cmm-pm-skills 套件的**总协同层**：站在 9 个阶段插件之上，统筹"一个产品项目走到哪了、下一步该跑哪个阶段、产出存哪、每阶段的门过了没"。

它是**领航员 + 项目台账**，不是自动执行器：
- **建/读项目台账** `_runs/<项目>/_state.yaml`（唯一的跨会话状态源，解决"换会话状态就丢"）；
- **显示流水线进度看板**；
- **按阶段守门**：每阶段"风险结论 → 用户拍板"过了才放行下一阶段；
- **引导下一步**该敲哪个阶段命令。

设计边界：**零侵入**（只读各阶段产出的 md，不改它们）、**不硬调用其它插件命令**（插件独立安装，只用人话建议用户去敲 `/xxx`）、**用户是决策者**。

## Install / 安装

随 cmm-pm-skills marketplace 一起安装：

```bash
claude plugin marketplace add chemny/cmm-pm-skills
claude plugin install pm-console@cmm-pm-skills
```

安装后开一个新的 Agent 会话，让它重新扫描插件。

## Command / 命令

| 命令 | 作用 |
|---|---|
| `/cmm-pm <项目名或想法>` | 新项目：建台账并领航 |
| `/cmm-pm` | 续接：列出已有项目 / 选一个协同 |
| `/cmm-pm status` | 看当前项目进度看板 |
| `/cmm-pm next` | 问"下一步该干嘛" |

## Skill / 技能

| 技能 | 作用 |
|---|---|
| `pipeline-orchestration` | 流水线图谱（阶段→命令→产物）、`_state.yaml` 台账规范、看板格式、守门规则。统筹项目时自动加载。 |

## 工作纪律

本插件遵循套件统一纪律 [`CONVENTIONS.md`](./CONVENTIONS.md)（安装即随插件分发）。
