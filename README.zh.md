# cmm-pm-skills

中文 | [English](./README.md)

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

| 能力 | 它能帮你做什么 |
|---|---|
| 市场分析（`/market-analysis`） | 用证据梳理市场、用户、买单人、竞品与颠覆机会。 |
| 需求洞察（`/insight`） | 区分真实需求与假设，并形成一手验证计划。 |
| 产品战略（`/strategy`） | 明确定位、壁垒、商业模式、定价和关键取舍。 |
| PRD（`/write-prd`） | 产出覆盖功能、流程、交互、数据和边界的可开发需求。 |
| 界面设计（`/wireframe`） | 生成流程、状态、可点击 HTML 原型和实现规格。 |
| 用户故事（`/write-stories`） | 把需求拆成可追溯的用户故事和验收标准。 |
| 技术方案（`/tech-design`） | 梳理选型、架构、数据、技术验证与实现冲突。 |
| 测试（`/test-scenarios`） | 覆盖正常路径、边界条件和异常情况。 |
| 上线（`/plan-launch`） | 制定聚焦的市场进入与发布计划。 |
| 数据迭代（`/analyze-cohorts`） | 把产品指标带回下一轮需求发现。 |

> 完整说明见 [PIPELINE.md](./PIPELINE.md)；统一纪律见 [CONVENTIONS.md](./CONVENTIONS.md)。⑦技术方案实现/⑨研发属工程，不在本套件。

## 平台兼容性

兼容 Claude Code、Codex 和 OpenClaw。Claude Code 提供命令与 Skills；Codex 下拉菜单显示包括 `CMM PM Skills: Main` 在内的 13 个一级 Skills；OpenClaw 可将 `main` 识别为模型可见、可作为命令调用的 Skill。其余 58 个专业方法由内部路由按需调用。

## 安装

把下面这句话发给你当前使用的 Agent，让它自行判断客户端、安装并验证：

```text
请为我当前使用的 Agent 客户端安装 https://github.com/chemny/cmm-pm-skills 的完整插件包，不要只安装某一个 `skills/` 子目录。自动判断正确的插件位置，完成安装，并验证 CMM PM Skills: Main 可以读取内置的 `references/CONVENTIONS.md`、`references/commands/market-analysis.md` 和 `references/commands/write-prd.md`，最后报告结果。
```

## 快速开始

安装后从总入口开始。Codex 选择 Skill，Claude Code 使用命令：

```text
Codex：CMM PM Skills: Main
Claude Code：/cmm-pm-skills
```

预期结果：

```text
它会问你想怎么开始（从头做整套，还是只做某一块，比如只写 PRD），
按你说的直接动手；每个阶段结尾给风险结论、由你拍板再进下一步。
不用看说明书。老手也可直接敲单个命令，如 /write-prd 你的想法。
```

`main` Skill 同时在自身 `references/` 中内置了阶段规则和统一纪律。即使某个宿主只安装 Skills 层、没有按完整插件安装，完整流程也不会悄悄降级成叶子模板。

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
├── sync_conventions.py     跨平台母版→插件同步
├── sync_conventions.sh     可选 POSIX 包装脚本
├── validate_plugins.py     契约校验
├── cmm-pm-skills/          单插件（Codex + Claude 双清单）
│   ├── commands/           46 个原生阶段命令
│   └── skills/             13 个一级 Skills；main 内置阶段命令兜底
├── _design/                方法论蓝图 / 清单
└── _runs/                  端到端示例
```

## 运行要求

- Claude Code 或 Codex CLI；
- 部分命令需联网搜索（市场/竞品研究）；
- 可选：用于发布的 GitHub CLI（`gh`）。
- 仅维护者需要：Python 3，用于校验、目录生成和约定同步；Windows 可使用 `py -3` 启动器。

## 协议

MIT。见 [LICENSE](./LICENSE)。本项目改编自 [phuryn/pm-skills](https://github.com/phuryn/pm-skills)（MIT），原作者版权已在 LICENSE 中保留。
