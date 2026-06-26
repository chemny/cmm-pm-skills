---
description: Turn the PRD + UI spec + backlog into a technical design — tech stack (researched, not guessed), architecture (Mermaid), data model, key technical decisions, and resolution of the backlog's spikes. A grounded proposal; final architecture is engineering's call.
argument-hint: "<the PRD / feature / spike to resolve>"
outputs: ["选型/架构/数据/解spike/冲突检查"]
---

# /tech-design -- Technical Design (⑥)

Stage ⑥ of the full pipeline (between ⑤ design and ⑦ stories / before engineering builds). Turns **④ PRD + ⑤ UI spec + ⑦ backlog** into a technical design: how it gets built, and **resolution of the spike-gated unknowns** so the team can estimate and start.

> **Scope honesty.** Technical design is traditionally engineering-owned. This skill produces a **grounded technical proposal** (a document) — enough to resolve spikes and let the team estimate. **Final architecture is engineering's call**; flag what needs a real POC.
> **Research, don't guess (CONVENTIONS §4/§8).** Tech-stack / model / third-party choices (e.g. ASR, LLM) must be **searched and triangulated with real data** (capability, price, latency, limits) — never assert "use X" without evidence. Benchmarks/prices get sources or are marked 〔待 POC 验证〕.
> **Inherit, don't invent (§0b/§9).** Architecture serves the PRD's features + the UI spec's flows; don't design for requirements that don't exist.
> **Collaborate (§0a/§0c).** Key technical decisions (stack, build/buy, the spike resolution) are presented with options + a recommendation; **the user/team decides**. Surface risks, bring solutions.
> **Follow [`CONVENTIONS.md`](../CONVENTIONS.md)**.

## Step 1 — Inherit & frame
Pull from ④PRD (features, non-functional bars), ⑤UI spec (flows/screens), ⑦backlog (esp. the `?(spike)` items). Restate the **technical problems to solve** — including each spike.

## Step 2 — Resolve the spikes (the main value)
For **every spike-gated item** in the backlog, produce a concrete technical approach: options (with researched evidence), a recommendation, the measurable validation it still needs (POC), and the rough effort it unlocks. This is what turns "?(spike)" into estimable work.
- **Don't overclaim resolution.** A spike is *resolved* only with a **buildable approach + a defined validation**. If it's only directional, say "方向已给，仍需设计 spike" — don't mark it estimable when it isn't.
- **Naming ≠ designing.** A core component/engine isn't designed by naming it — **specify its actual logic/algorithm** (how the routing decides, how the profile is extracted, how the detection works) or flag that logic as a sub-spike.
- **Flag the unknowns the design itself introduces.** A chosen approach usually creates its own new hard problem — surface it, don't let it hide.

## Step 3 — Design (coverage)
Cover: tech stack, architecture, data model, key decisions, interfaces, non-functional implementation, risks. Don't skip a layer.

## Step 3.5 — Mandatory checks (don't skip — these are where tech designs quietly fail)
- **Conflict check: architecture vs the product's differentiation & non-functional bars.** Verify the chosen architecture **doesn't undermine the product's own selling points or NFR targets** (CONVENTIONS §8 卖点守护). A cloud dependency can break a "local/privacy" moat; a heavy runtime can break a "fast/light" bar; per-call cost can break a "free" model. **If there's a tension, surface it explicitly and give options (e.g. local vs cloud, with the trade-off)** — never bury it.
- **Non-functional & cost must drive the architecture, not be an afterthought:**
  - **Latency budget** — for anything with per-action external calls (LLM/API/cloud), state the real latency and whether it meets the UX bar; if not, redesign (local/streaming/caching).
  - **Offline / network dependency** — what works offline vs needs network? Is that acceptable for this product?
  - **System-level cost model** — cost **per active user / per action**, tied to the **business model** (e.g. does the freemium tier survive the per-call cost?). Unit prices alone are not enough.

## Step 4 — Output (plain headings, methodology backstage)
Save as markdown. Use Mermaid for architecture/data-flow; **render diagrams to a viewable HTML** too (CONVENTIONS — don't leave Mermaid only in .md).
```
# 技术方案：[产品]
> 承接 ④PRD + ⑤界面 + ⑦backlog；这是技术提案，最终架构由工程定。

## 1. 技术选型        平台/语言/框架/关键第三方(ASR/LLM…)，每项带对比依据/价格/限制
## 2. 系统架构        模块/组件/数据流（Mermaid 架构图）
## 3. 数据模型与存储  实体/关系/存储位置/加密
## 4. 关键技术决策    方案A vs B 的权衡与选择(为什么)
## 5. 难点 / SPIKE 解决  逐个 backlog spike：方案+证据+待POC验证+解锁的估算
## 6. 接口 / API      (若有)关键接口契约
## 7. 非功能 + 冲突检查  延迟预算/网络依赖/**系统级成本(对齐商业模式)**；安全/隐私落地；**架构有无与卖点/NFR 打架——有则给"本地 vs 云"等选项+权衡**
## 8. 风险/依赖/未决  技术风险+解法、外部依赖、待定技术问题
## 9. 实施要点        给研发的落地建议、模块拆分、优先级
```

## Step 5 — Review
- 多角色红队（§8），尤其落地工程师视角："这方案真能建吗?哪里还虚?"。
- 下一步：把解决了 spike 的 backlog 回填估算 → `/sprint`；或 `/write-stories` 补拆 spike 解决后的子故事。

## Conventions
- 架构/数据流用 Mermaid（`flowchart`/`graph`），并产一份渲染好的 HTML（别只丢 .md）。
- 选型必须有据：能力/价格/延迟/限制要搜真实数据并三角验证；厂商宣称标〔厂商宣称〕。
- 不确定就标〔待 POC 验证〕，不假装已知。

## Notes
- 这一环的核心价值 = **把 ⑦ 里 `?(spike)` 的未知变成可估算的方案**。
- 它是提案不是定稿；凡需实测的(性能/可行性)标 POC，不替工程拍最终板。
- 每个技术决策都要追溯到 PRD 的某条需求或非功能指标。
