# cmm-pm-skills — CMM 产品经理工作流（单插件全套）

## Overview / 总览

一个插件装下整套产品经理工作流：从市场分析到 PRD、原型、技术方案、用户故事、测试、上线、数据迭代，每个阶段一条命令、产出真实可用的交付物，并共享一套统一工作纪律 [`CONVENTIONS.md`](./CONVENTIONS.md)。

总入口 **`/cmm-pm-skills`** 让你一句话上手：从头做整套，或只做某一块（如只写 PRD）。

## Install / 安装

```bash
claude plugin marketplace add chemny/cmm-pm-skills
claude plugin install cmm-pm-skills@cmm-pm-skills
```

安装后开一个新的 Agent 会话，让它重新扫描插件。

## Command / 命令

| 命令 | 作用 |
|---|---|
| `/cmm-pm-skills` | **总入口/总协同**：一句话上手，整套或单块，含项目台账与守门 |
| `/market-analysis` | ① 市场分析（五看） |
| `/insight` | ② 需求洞察 |
| `/strategy` | ③ 产品战略 |
| `/write-prd` | ④ PRD |
| `/wireframe` | ⑤ 界面设计 |
| `/write-stories` | ⑥ 用户故事 |
| `/tech-design` | ⑦ 技术方案 |
| `/test-scenarios` | ⑧ 测试 |
| `/plan-launch` `/battlecard` `/growth-strategy` | ⑩ 上线 |
| `/analyze-cohorts` `/north-star` `/analyze-test` | ⑪ 数据/迭代 |

> 还有市场/战略/增长/工具箱等共 46 个命令，slash 菜单里都带中文说明，扫一眼即可。任意命令都能**单独调用**（§0d）。

## Skill / 技能

共 70 个分析技能（市场画像、竞品、JTBD、精益画布、用户故事、预演、红队……），按对话话题自动加载；其中 `pipeline-orchestration` 为总协同提供流水线图谱、项目台账规范与守门规则。

## 工作纪律

遵循 [`CONVENTIONS.md`](./CONVENTIONS.md)（随插件分发，安装即继承）。
