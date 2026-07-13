---
description: Turn a PRD into a UI spec + clickable HTML prototype — Mermaid screen-flow/state diagrams, a self-contained clickable HTML prototype, and per-screen interaction specs with full state coverage. Hands off to user stories.
argument-hint: "<the PRD / feature>"
outputs: ["Mermaid流/态 + 可点击HTML原型 + 规格"]
---

> **Capability loading:** For each capability named in `uses`, use its visible Skill when present; otherwise read `../skills/main/references/capabilities/<name>.md` completely before applying it.

# /wireframe -- UI Spec & Clickable Prototype

Stage ⑤ of the pipeline. Turns the **④ PRD** into two artifacts:
1. **界面规格 (markdown)** — Mermaid screen-flow + state diagrams + per-screen element/interaction/state specs.
2. **可点击原型 (self-contained .html)** — each screen rendered, click to navigate between screens; open in any browser.

> **It really is visual + clickable.** The HTML is generated as plain code (no external design tool) and renders a real, navigable prototype in the browser. Styling stays **clean and simple** (layout & flow first, not pixel-perfect visuals) — fine-grained visual design is a later step. But this is a working prototype, not just text.
> **Right tool for each job:** **Mermaid** for screen-flow & state machines (it's best at logic/transitions); **HTML** for what each screen looks like and how it clicks through; **text** for the precise element/interaction/state specs.
> **Inherit, don't invent (§0b).** Screens, features and flows come from the **④ PRD**; every screen/element traces to a PRD feature. If the PRD is missing, ask for it.
> **Collaborate (§0a/§0c).** You're the assistant; the user decides. Confirm the screen list before detailing all of them; flag risks, bring solutions.
> **Follow [`CONVENTIONS.md`](../CONVENTIONS.md)** for cross-cutting discipline (plain output, no-fabrication, coverage, red-team).

## Step 1 — Inherit & list the screens
From the PRD's user flow + features, derive the **screen list** (each screen = a distinct thing the user sees). Restate it and confirm with the user before building all of them.

## Step 2 — Coverage discipline (the depth a PRD section lacks)
For **every** screen, cover **all states** — missing a state = incomplete:
- 默认 / 加载中 / 空 / 错误 / 边界(超长/无权限/断网/失败)
- Every interactive element's behavior (click / 快捷键 / 手势 → result).

## Step 3 — Produce both artifacts

**A. 界面规格 `UI-Spec-[product].md`**
```
# 界面规格：[产品]
## 1. 屏幕流（Mermaid flowchart：屏与屏怎么跳，箭头标触发动作）
## 2. 状态机（Mermaid stateDiagram：关键状态流转，如录音→处理→插入）
## 3. 每屏规格（逐屏）
### 屏：[名称] ← PRD 功能 [F?]
- 元素清单：元素 = 作用 + 状态
- 状态覆盖：默认/加载/空/错误/边界
- 交互：触发(点击/快捷键/手势) → 行为
- 文案要点
## 4. 全局组件与规范（复用组件、快捷键总表、提示/反馈/角标规范）
## 5. 交接说明（给视觉/研发的待补点）
```

**B. 可点击原型 `Prototype-[product].html`**（单文件自包含，浏览器直接开）
- 每屏一个"画面"，顶部一排导航/或屏内按钮**点击切换屏**（简单 JS show/hide）。
- 体现关键状态（默认/空/错误可做成可切换的变体）。
- 每屏标题标注对应 PRD 功能，便于追溯。

## Step 4 — Review
- 多角色红队（CONVENTIONS §8）：**有没有漏屏、漏态、点不通的跳转**。
- 下一步：`/write-stories`（把界面+功能拆成用户故事）。

## Conventions
**Mermaid**：屏幕流用 `flowchart LR/TD`（节点=屏，箭头=动作）；状态用 `stateDiagram-v2`。
**Mermaid 必须可视化（别只丢 .md）**：图除写进 .md 外，**还要给一个用 mermaid.js 渲染好的 HTML**（浏览器直接看到图），文件内注明"若图不显示，把 mermaid 代码贴到 mermaid.live"。纯 .md 里的 mermaid 是代码、用户看不懂。
**HTML 原型**：
- 单个自包含 `.html`（内联 CSS/JS），无外部依赖，浏览器可直接打开。
- 用 JS show/hide 在屏间跳转，做成**可点击**原型；导航清晰。
- 样式**干净中性**（浅灰描边、留白为主），桌面端用窗口/悬浮框示意，移动端用手机外框；**重布局与流程，不追求好看**。
- 每屏必标题 + PRD 追溯；关键状态可切换查看。

## Notes
- 漏一个屏或一个状态 = 不合格（覆盖是这个 skill 的价值）。
- 原型服务于"看得见、点得通、追得到需求"，不是视觉终稿。
- 每个界面元素都要追溯到 PRD 某条需求，不凭空加。
