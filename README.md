# cmm-pm-skills

中文 | [English](./README.en.md)

cmm-pm-skills 是一个面向产品经理、创始人、独立开发者和 Agent 用户的产品经理工作流 skills 套件。它把"从市场到落地"的每个阶段做成可调用的命令，把零散的想法和调研整理成真实可用的交付物（市场分析、PRD、原型、技术方案……），方便后续设计、研发、测试与上线继续使用。

它支持市场分析、需求洞察、产品战略、PRD 与界面/技术设计，也可以一路贯通到用户故事、测试、上线与数据迭代——所有阶段共享一套统一工作纪律。

## 适合谁使用？

这个套件适合：

- 用 Claude Code / Codex 做产品的**产品经理、创始人、独立开发者**；
- 想要"从想法到 PRD 到原型"一条龙、且**每步有据可依、不被 AI 糊弄**的人；
- 需要把零散调研沉淀成可交付、可追溯产物的个人或小团队。

## 它能做什么？

通用 AI 给你一堆漂亮文字，但往往浅、爱编、容易跑偏。这套 skills 把产品经理各阶段做成命令，每步都遵循同一套纪律：继承上游不重造、自己搜证三角验证、不编造、结论交你拍板。

最终你得到的不是空话，而是能直接用的交付物——一份有数据支撑的市场分析、一份可开发的 PRD、一套可点击的原型、一份落地的技术方案。

## 核心能力

**总入口 `/cmm-pm-skills`** 让你一句话上手：从头做整套，或只做某一块（如只写 PRD）。它统筹项目状态台账（跨会话不丢）、按阶段守门（风险结论→你拍板）、领航下一步。下面是它统筹的各阶段——按产品研发实际顺序排列，前面是决定"做不做、怎么做"的关键阶段，后面是落地与迭代。

| 阶段 | 命令 | 输出结果 |
|---|---|---|
| ① 市场分析 | `/market-analysis` | 市场/用户/买单人/竞品/颠覆机会（数据定） |
| ② 需求洞察 | `/insight` | 真需求 + 风险结论 + 一手验证计划 |
| ③ 产品战略 | `/strategy` | 定位/壁垒/商业模式/定价/打法 |
| ④ PRD | `/write-prd` | 完整可开发 PRD（需求+功能+流程+交互+数据+边界） |
| ⑤ 界面设计 | `/wireframe` | Mermaid 流/态 + 可点击 HTML 原型 + 规格 |
| ⑥ 用户故事 | `/write-stories` | 故事 + 验收（可追溯） |
| ⑦ 技术方案 | `/tech-design` | 选型/架构/数据/解 spike/冲突检查 |
| ⑧ 测试 | `/test-scenarios` | 测试用例（happy/边界/错误） |
| ⑩ 上线 | `/plan-launch` 等 | GTM 计划 |
| ⑪ 数据/迭代 | `/analyze-cohorts` 等 | 指标 → 回到 ② |

> 完整说明见 [PIPELINE.md](./PIPELINE.md)；统一纪律见 [CONVENTIONS.md](./CONVENTIONS.md)。⑦技术方案实现/⑨研发属工程，不在本套件。

## 平台兼容性

Claude Code 支持命令 + 技能；Codex CLI 支持技能（以自然语言描述触发）；其他 Agent（Cursor / Gemini CLI 等）可复制 `skills/` 目录使用技能。

## 安装

本套件是**单个** Claude Code 插件，两行装好：

```bash
claude plugin marketplace add chemny/cmm-pm-skills
claude plugin install cmm-pm-skills@cmm-pm-skills
```

安装后开一个新的 Agent 会话，让它重新扫描插件。

## 快速开始

装完只需记**一个**命令——对 Agent 说：

```text
/cmm-pm-skills
```

预期结果：

```text
它会问你想怎么开始（从头做整套，还是只做某一块，比如只写 PRD），
按你说的直接动手；每个阶段结尾给风险结论、由你拍板再进下一步。
不用看说明书。老手也可直接敲单个命令，如 /write-prd 你的想法。
```

## 使用示例

端到端真实案例见 [`_runs/`](./_runs)：

```text
_runs/voice-ime/   —— "sayit"（个性化语音输入法）从市场分析到 PRD/原型/技术方案的全过程
```

```text
_runs/natgeo-video/  —— "英文文章转视频学习工具"的市场分析与需求洞察
```

## 工作原理

- **总入口 `/cmm-pm-skills`** 一句话分流：整套领航，或单块直奔；
- **命令 = 阶段动作**，继承上游产出、也能单独调用（§0d）；
- **统一纪律**写在根 `CONVENTIONS.md`（母版），插件内置同步副本，安装即继承；
- 每个阶段：先研究/搜证 → 给结论与风险 → 决定权交用户。

## 仓库结构

```text
cmm-pm-skills/
├── CONVENTIONS.md          统一纪律（母版）
├── PIPELINE.md             全链路总览
├── sync_conventions.sh     母版→插件同步
├── validate_plugins.py     契约校验
├── cmm-pm-skills/          单插件（46 命令 + 70 技能 + 内置 CONVENTIONS 副本）
├── _design/                方法论蓝图 / 清单
└── _runs/                  端到端示例
```

## 运行要求

- Claude Code 或 Codex CLI；
- 部分命令需联网搜索（市场/竞品研究）；
- 可选：用于发布的 GitHub CLI（`gh`）。

## 协议

MIT。见 [LICENSE](./LICENSE)。本项目改编自 [phuryn/pm-skills](https://github.com/phuryn/pm-skills)（MIT），原作者版权已在 LICENSE 中保留。
