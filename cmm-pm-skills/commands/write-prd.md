---
description: Turn the validated need + strategy (①②③) into an engineering-ready PRD — or, if the need isn't validated yet, into a Validation-MVP PRD that tests the leap-of-faith cheaply. Inherits upstream; requirements traced to evidence, not invented.
argument-hint: "<feature / the strategy conclusion>"
uses: [create-prd]
outputs: ["可开发PRD（需求/功能/流程/交互/数据/边界）"]
---

> **Capability loading:** For each capability named in `uses`, use its visible Skill when present; otherwise read `../skills/main/references/capabilities/<name>.md` completely before applying it.

# /write-prd -- Product Requirements Document (execution)

Stage ④ of the pipeline. Turns the validated need + positioning/strategy from ①②③ into an engineering-ready spec: **what to build, to what bar, in what phases.**

> **Inherit, don't re-gather.** The user problem, persona, buyer, success context, positioning, strategy, moat and pricing all come from ①②③. **Don't re-ask or re-invent them — pull them in.** Only ask/research what's genuinely missing for the *spec*.
> **Confirm core elements FIRST (CONVENTIONS §0c).** Before writing, confirm WITH THE USER: **product name, the main user flow, scope (in/out), and key decisions.** Never autopilot a PRD the user never shaped — that's how you write the wrong thing.
> **Risk flag, not a veto (CONVENTIONS §0c).** If ②'s need is still unvalidated, **say so and recommend** validating first (or scoping a validation MVP) — but **the decision is the user's.** If the user has chosen to proceed, **write the full PRD they want**, with risks noted. Never refuse, and never silently downgrade "full" to "validation-only."
> **Whatever you write, make it buildable:** concrete feature list, end-to-end user flow, detailed functional requirements per feature, data & deployment, non-functional bars, **testable** acceptance criteria. A PRD an engineer can't build from is not a PRD. Narrow the SCOPE if scoping down, never the DETAIL.
> **Do your own research + don't fabricate.** For feasibility, compliance specs, and competitor feature benchmarks, search + **triangulate (≥3 sources/≥2 classes)** (CONVENTIONS §4/§8). **Every requirement traces to the validated need + strategy, or is marked 〔assumption/to-validate〕** — no orphan/invented features.
> **Follow [`CONVENTIONS.md`](../CONVENTIONS.md)** for all cross-cutting discipline.
> **Research gate (mandatory):** Read [`Deep Research Contract`](../skills/main/references/contracts/deep-research-contract.md) and pick `standard` or `full` intensity based on launch/business risk. Check upstream `research_gate` and freshness before inheritance. Run incremental research for every new, expired, or load-bearing external fact; `create-prd` is only the structure template and cannot waive this gate.

## Step 1 — Inherit context (don't re-gather)
Pull from upstream and restate briefly: validated need + JTBD (②), persona/buyer (①), positioning + strategy + moat + pricing (③), **research_gate + evidence maturity + freshness**, and the **validation status** (②). Only ask the user for genuinely missing spec inputs (technical constraints, timeline, team). If upstream is missing, **say so — don't fabricate a need or persona.** `pass-emerging/pass-with-gaps` claims remain assumptions/experiments; inheritance never upgrades confidence.

## Step 2 — Pick the PRD mode by validation status and user intent
- **Need validated** → full PRD.
- **Need UNVALIDATED + user has not specified full product** → default to **Validation-MVP PRD**: spec only what's needed to test the leap-of-faith, with an explicit success threshold. Title it **"验证版·非完整产品"**. The PRD's job here is to spec the *validation*, not the dream.
- **Need UNVALIDATED + user explicitly wants the full product PRD** → write the full PRD they asked for, but title/status must clearly say **"需求未验证·完整产品草案"**, and risk sections must carry the unvalidated assumptions. Do not silently downgrade to validation-only.
- **Need UNVALIDATED + user has not made the mode clear and both paths are plausible** → ask one direct question: "要验证版 MVP PRD，还是完整产品 PRD 草案？" Then continue from the chosen mode.

## Step 3 — Generate the PRD
Apply the **create-prd** skill. **A complete PRD = 需求 + 功能 + 流程 + 交互 + 数据 + 边界条件.** Background & users inherit from ①②; objectives tie to ③; every requirement traces to evidence (no invented features). Full structure:
```
## 产品需求文档：[名称]    〔需求未验证时：验证版·非完整产品〕

### 0. 文档信息          状态/版本/作者/干系人/更新日期/输入来源(①②③)/相关文档
### 1. 引言与术语        文档目的 + 名词/术语解释
### 2. 目标与背景        业务目标 + 问题/机会 + 为何现在（继承①②，带血缘）
### 3. 目标用户与场景    画像/persona + 使用场景(use cases) + 竞品（继承①，不重造）
### 4. 成功指标          可量化（现状/目标/测量方式）
### 5. 范围             明确 in-scope / out-of-scope（非目标）
### 6. 功能清单与产品结构 全部功能逐条 + 功能地图/脑图（一眼看清产品骨架）
### 7. 用户流程与业务逻辑 端到端主流程图 + 关键业务规则 + 状态流转
### 8. 详细功能需求      每个功能：输入/行为/输出/业务规则/**边界与异常**/优先级(P0/P1/P2)/**可测验收标准(AC)**
### 9. 交互与界面(UX)    关键界面/布局/交互说明 + 原型/线框图（或占位待补）
### 10. 数据需求         数据模型/实体 + **埋点与统计指标**
### 11. 非功能需求       性能/准确率/延迟/安全/合规（量化）
### 12. 假设、风险、待解问题  假设 + 风险 + 真未决项(owner/deadline)
### 13. 排期与依赖       里程碑/估算/跨团队依赖（验证版则=验证 MVP 最小切口；完整草案则标注未验证依赖）
### 14. 附录            相关文档/参考/版本记录
```
> 缺了 **流程图、交互/界面、数据/埋点、边界异常** 中任意一块，PRD 就不可开发——窄范围可省"广度"，但每块该有的"深度"不能省。
> **再按 `create-prd` 的「条件性章节」补全(达大厂就绪 bar)**：成本/单元经济性、隐私与数据、护栏+反向指标、实验与灰度、安全/滥用、发布就绪与签字、无障碍、以及带 owner+deadline 的待解项与带缓解的风险——**逐条按触发条件判断，成立才补、不触发可略**(通用规则，不绑具体产品)。

## Step 4 — Review (own research + red-team)
- For feasibility/compliance requirements, **search + triangulate** — don't assert.
- Run the **multi-persona red-team** (CONVENTIONS §8) on the PRD: 怀疑实践者/对抗评审/落地工程师.
- Offer: `/wireframe`(⑤ 出界面规格/线框), `/red-team-prd`, `/write-stories`(拆故事), `/pre-mortem`, `/sprint`.
- Save as markdown.

## Step 5 — 交付前自检（后台执行，不展示给用户）

交 PRD 之前，逐条核对这些 **PRD 专属失败模式**；**任一不过就就地改了再交**。这是 agent 的内部体检，**不要把清单或"我在自检"讲给用户**，用户只该看到更扎实的 PRD（最多结尾一句"已过交付前自检"）。

- □ **每条需求可溯源**到 ①②③，或显式标〔假设·待验证〕——出现无来源的功能 = 凭空发明，删除或降级为假设。
- □ **上游Research Gate已检查**：不存在把 `pass-emerging/pass-with-gaps` 静默升级为事实；新增/过期/承重事实已有本阶段增量研究账本。
- □ **每条验收标准可测**：有明确通过/失败条件。出现"流畅/友好/丝滑/体验好"等不可测词，必须改写成可观测条件（如"错误密码显示提示且不锁死"）。
- □ **写了 out-of-scope（非目标）**：没有非目标 = 范围必蔓延。
- □ **覆盖边界与异常路径**，不只 happy path（空态/超限/失败/并发/权限）。
- □ **指标可量化**：现状 → 目标 → 测量方式；禁止"提升留存"这类无基线无口径的说法。
- □ **需求未验证时**：按 Step 2 的用户意图选择模式；验证版标题挂"验证版·非完整产品"，完整草案标题挂"需求未验证·完整产品草案"。不得把验证版假装成完整产品，也不得把用户明确要的完整草案静默降级。
- □ **主流程图 + 数据/埋点齐全**：缺流程、缺交互、缺数据/埋点、缺边界，任一缺 = 不可开发，补上。
- □ **范围可缩、深度不可省**：窄切口可以，但留下的每块该有的细节不能省（§5）。
- □ **条件性章节就位（大厂 bar）**：凡触发条件成立——有按量外部成本 / 碰用户数据·录音·PII / 规模上线 / 产出可滥用 / 有界面——却漏写对应章节，补上；指标含 正向+护栏+反向；待解项与风险各带 owner（见 `create-prd` 3.5）。不触发的不强求。

> 自检是把"框架的常见翻车点"变成交付前的硬关卡，强化 §8 红队、保持产出纯执行。

## Notes
- Tight scope, opinionated; non-goals matter as much as goals.
- Metrics specific ("NPS 32→45 within 90 days", not "improve NPS").
- **If unvalidated, default to spec the validation; write a full-product draft only when the user explicitly chooses that mode.**
- Requirements grounded in ①②③ evidence — never fabricated to look complete.
