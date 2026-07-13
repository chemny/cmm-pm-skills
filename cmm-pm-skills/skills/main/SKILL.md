---
name: main
description: "CMM PM Skills 总入口与总控。用于从产品想法开始完整产品经理流程、继续已有项目、查看状态或下一步，也用于用户只想完成 PRD、市场分析、战略、复盘、WWA 工作项等某一个单项任务，或不知道该选择哪个 CMM PM 子 Skill 时。"
---

# CMM PM Skills Main

作为统一入口，先判断用户要完整流程、单项直达，还是继续已有项目。遵循插件根目录的 `CONVENTIONS.md`。

## 分流

- 目标不清楚：说明可以做完整流程或单项任务，只问最关键的问题。
- 要完整规划：读取内部能力 [`pipeline-orchestration`](references/capabilities/pipeline-orchestration.md)，从合适阶段开始，按台账和阶段守门推进。
- 明确只做一项：只完成该任务；不要强迫补齐上游，不要自动扩展为完整流程。
- 要 `status` 或 `next`：读取项目台账或已有产物，只报告真实进度。

## 一级 Skills

用户可以直接调用以下高频能力：

- 市场竞品：`competitor-analysis`
- 用户访谈：`interview-script`
- 产品战略：`product-strategy`
- PRD：`create-prd`
- 功能优先级：`prioritize-features`
- 用户故事：`user-stories`
- Sprint 规划：`sprint-plan`
- 测试场景：`test-scenarios`
- GTM：`gtm-strategy`
- 定价：`pricing-strategy`
- Cohort 分析：`cohort-analysis`
- 复盘：`retro`

用户明确指定这些 Skill 时直接使用，不改换方法。

## 内部能力路由

其余专业方法位于 `references/capabilities/`。需要时先读取对应 Markdown 文件的完整内容，再执行其中的方法。不要一次加载全部能力。

常见路由：

- WWA 工作项 → [`wwas`](references/capabilities/wwas.md)
- Job Stories → [`job-stories`](references/capabilities/job-stories.md)
- 失败预演 → [`pre-mortem`](references/capabilities/pre-mortem.md)
- Lean Canvas → [`lean-canvas`](references/capabilities/lean-canvas.md)
- 市场规模 → [`market-sizing`](references/capabilities/market-sizing.md)
- 北极星指标 → [`north-star-metric`](references/capabilities/north-star-metric.md)
- 增长飞轮 → [`growth-loops`](references/capabilities/growth-loops.md)
- 用户画像 → [`user-personas`](references/capabilities/user-personas.md)
- 价值主张 → [`value-proposition`](references/capabilities/value-proposition.md)
- 战略红队 → [`strategy-red-team`](references/capabilities/strategy-red-team.md)

其他明确点名的方法，将名称规范化为小写连字符，并查找 `references/capabilities/<name>.md`。找不到时再询问用户，不要编造不存在的能力。

## 执行边界

- 尊重“只做这一项”“其他不要”等范围限制。
- 有上游材料就继承；没有时只询问当前任务必需的信息。
- 未经用户要求，不连续执行后续阶段。
- 完整流程每个重要阶段结束后给出风险结论，等待用户拍板。
- 完成后只给一个轻量、明确的下一步，不强推完整流程。
