---
description: Run a rigorous market analysis using the Five Looks framework (五看) — intake gating, industry/market/competition/self/opportunity scan, with source-credibility discipline and a mandatory bear case. Front half of Five Looks & Three Decisions (五看三定).
argument-hint: "<product or market idea>"
uses: [competitor-analysis, market-sizing, user-personas]
outputs: ["市场/用户/买单人/竞品/颠覆机会（数据定）"]
---

> **Capability loading:** For each capability named in `uses`, use its visible Skill when present; otherwise read `../skills/main/references/capabilities/<name>.md` completely before applying it.

# /market-analysis -- Market Analysis (Five Looks / 五看)

Produce a stereoscopic, decision-grade market analysis for **$ARGUMENTS**.
This is stage ① of the pipeline (describe the world). It feeds discovery (②) and strategy (③).
Framework: **Five Looks (五看)** — the research half of Huawei's Five Looks & Three Decisions (五看三定).

> Golden rule: this command DESCRIBES the world (industry, market, competitors, our own position). It does NOT decide our moat, pricing, or go-to-market — those are Three Decisions (三定), handled in `/strategy`.

> **Follow [`CONVENTIONS.md`](../CONVENTIONS.md) for all cross-cutting discipline** (how to ask for inputs, atomic keyword, classify-by-category, search/source rules, depth bar, honesty/bear-case, methodology-backstage, red-team self-check). This file only adds the **market-analysis-specific** structure below.
> **Research gate (mandatory):** Before searching, read and execute [`Deep Research Contract`](../skills/main/references/contracts/deep-research-contract.md) at `standard` or `full` intensity. Create the research ledger, classify market maturity, and do not deliver while `research_gate=revise/blocked`.

## Invocation

```
/market-analysis A voice input method for office workers
/market-analysis [upload a brief, deck, or competitor list]
/market-analysis                 # will run the intake gate first
```

---

## Step 0 — Intake Gate (准入闸门) · DO THIS FIRST

A vague brief produces a vague report. Before research, **split fields into two classes and handle each correctly** — this is a universal rule.

**Class A — User-knowledge fields (ASK the user; never guess, never fabricate answers):** only the user knows these.
| Field | What to pin down |
|---|---|
| Product definition | the exact product term (treat it atomically) + its category/form |
| Target user (specific) | which segment + usage scenario |
| Geography | target market region |
| Commercial intent | how it makes money / who pays |
| Constraints | budget / team / timeline / existing tech or channels (best-effort) |

**Class B — Research-determined fields (DO NOT ask the user; derive from data):** the user's opinion is not the source of truth here.
| Field | How it's determined |
|---|---|
| Benchmark / best-in-class | by **market data — size, usage, reputation, rankings** — NOT by user fiat or model guess. "Who is the best" is a research output, not an intake question. |
| Competitor set | enumerated by research (Look 3) |
| Market size & trends | searched (Look 1) |

**How to ask for Class A:** follow CONVENTIONS.md §1 (echo-then-request, plain language, example options not forced, no popup, no filler). For Class B, never ask — research it (§1).

**Gating rule:** if any Class A field (constraints excepted — best-effort) is missing, ask — do not proceed on assumptions. If the user volunteers an aspiration ("I want it like X"), treat it as one input, but still independently establish the real benchmark from data.

---

## Step 1 — The Five Looks (五看)

Each Look = a set of targeted searches + a conclusion. Describe reality; do not insert our decisions yet.

> **Before searching, build a research plan (CONVENTIONS §4):** list the concrete data fields each Look must fill — including the **target sub-market** size/growth (not just the broad market), per-competitor fields, and per-segment scenario data. Fill every field; triangulate (≥3 sources / ≥2 classes per key claim). **Before delivering, do a gap scan and loop back with delta-queries** to fill anything missing/single-source (CONVENTIONS §8). Coverage is by design, not luck.

For `emerging/frontier` markets, missing authoritative TAM/share data is not an automatic failure. Follow the contract's evidence ladder and `pass-emerging` gate: use multiple strong proxies, expose uncertainty, and prevent downstream claims from becoming stronger than the evidence.

### Look 1 — Industry / Trend (看行业)
- Is the market rising or falling? Growth rate, drivers, lifecycle stage, technology and policy shifts.
- **Sizing:** TAM / SAM / SOM — **state the calculation assumptions for every number.**
- **Disruption vectors (mandatory — incumbents ≠ no opportunity):** where is the market *shifting*? A tech reset (AI/LLM neutralizing old moats), areas incumbents underinvest in, emerging user groups / changing behavior, innovator's-dilemma blind spots, and real signals from new entrants (funding, rankings, growth). Giants being present is NEVER a kill reason — find where they're slow/weak and the market is moving.

### Look 2 — Users, Buyer & Demand (看市场/客户) — data-grounded, this is the backbone
This block decides whether a viable "who" exists, so the next stages can even start. Everything here is **established from data and competitors — never invented (CONVENTIONS §9).**
1. **Actual user persona + typical scenarios** — by SEARCH, *who actually uses this kind of product, for what, how often, in what contexts.* Find the typical/high-volume scenarios, not a convenient niche. Apply **user-personas**, **market-segments**.
2. **Reconcile with the user's stated target** — the user's asserted segment (Class A) is a hypothesis; if data shows the real users differ, **say so explicitly** (e.g. "you said 白领, data shows mostly young social-chat users").
3. **The buyer & willingness-to-pay** — **who actually pays** (may differ from the user!). Is there evidence anyone pays? For free-dominated categories, flag "users ≫ buyers". This gates the business model.
4. **Market-level demand evidence** — do competitors already serve this need? **Competitors existing = the need objectively exists in the market** (a grounded signal, not a guess). Absence of anyone serving it = either no demand or a real gap — investigate which.
- Output: a data-grounded persona + typical scenarios + buyer/WTP verdict + the viable target segment(s) — this is **inherited by `/insight` (②)**, which then validates the specific need with primary research.

### Look 3 — Competition (看竞争)
- **GLOBAL BY DEFAULT (mandatory):** even when the target market is domestic, you MUST also cover overseas products — they are reference-worthy and often ahead. Present **two sub-tables: 国内 (domestic) + 海外 (overseas)**. Skipping overseas is a fail.
- **Be exhaustive, not "top 5":** enumerate the full known set of relevant players. Run multiple search angles (by category, by "best X 2025 测评/ranking", by named incumbents) so you don't miss major entrants. Missing a heavyweight (e.g. a BigTech entrant) invalidates the analysis.
- **Classify by product CATEGORY, not merely by the shared job-to-be-done (universal rule).** Two products can serve the same job yet belong to different categories (different form factor, integration depth, or buyer). **Direct competitors = same category as the target product;** same-job-but-different-category products = indirect/reference only. Conflating categories invalidates the analysis. *(Illustrative: an input method / IME and an on-demand dictation utility both turn speech to text, but are different categories — don't list one as a direct competitor of the other.)*
- Identify direct / indirect / substitute competitors, share, and white space (**and verify the white space is genuinely empty, not just unsearched**).
- Apply the **competitor-analysis** skill, and for each competitor capture three observation sub-items:
  - **a. Tech / product approach** — cloud ASR? on-device? end-to-end model? LLM post-processing?
  - **b. Marketing play** — acquisition, pricing, messaging
  - **c. Product-design signature** — interaction highlights, UX choices
- Apply **sentiment-analysis** on reviews where available.

### Look 4 — Ourselves (看自己)
- Our capabilities, resources, strengths/weaknesses, and the **gap vs incumbents.**
- Apply the **self-assessment** skill. Be honest: why might we win, and where are we short?
- (This Look is what most market analyses skip — do not.)

### Look 5 — Opportunity (看机会)
- Strategic opportunity points, market space, and trade-offs.
- Output a **positioning hypothesis** that hands off to discovery (②).

### Monetization scan (light)
- How do competitors make money? Price bands? Has anyone validated paid demand?
- **Scan only** — full business-model design belongs to strategy (③), not here.

---

## Cross-cutting discipline
All cross-cutting rules — atomic keyword, search engines + source tiers, depth bar, honesty/**bear case**, **red-team self-check** before delivery — are in **[`CONVENTIONS.md`](../CONVENTIONS.md)**. They apply here in full; not repeated.

---

## Output

Methodology stays backstage (CONVENTIONS.md §7) — no "Look 3 / 看③ / Class A" labels in the output; plain result-oriented headings only.

Produce the report with these sections (plain headings, in the user's language), then **save as markdown** (`Market-Analysis-[topic].md`):

```
# 市场分析：[主题]
日期 · 调研范围（产品 / 人群 / 市场 / 盈利方向 / 现有条件）

## 市场趋势与规模    (升/降 + 规模估算与假设)
## 实际用户与买单人    (数据定的画像+典型场景；谁用≠谁买；付费意愿；竞品存在=需求客观存在)
## 竞争格局          (国内+海外表；各家技术/营销/设计；空白；**标杆——由数据定，非假设**)
## 市场态势与颠覆机会 (市场在怎么变、巨头弱在哪、技术重置/新用户/新入局者动向——有数据)
## 我们的位置与差距  (能力、与头部的差距)
## 机会与定位        (定位假设)
## 盈利模式          (对手怎么赚钱 + 可行模式)
## 风险与挑战        (为什么这事可能是坑)
## 结论与建议        (权衡"巨头强项 vs 颠覆向量"后给倾向；**不得因"有巨头"就否定**)
### 数据来源          (含可信度标注)
### 研究状态          (as-of日期 / 市场成熟度 / Research Gate / 关键缺口；不暴露冗长后台过程)
```

## Next Steps
- "Validate the riskiest assumptions? → run `/insight`."
- "Decide how we win (moat, business model, pricing)? → run `/strategy` (Three Decisions / 三定)."
- "Deep-dive one competitor into a battlecard? → run `/battlecard`."

## Notes
- **PIVOT GATE (CONVENTIONS §0b):** if the conclusion recommends changing the user's stated product / segment / form (a pivot), **STOP — do not silently feed the pivoted premise into ②/③.** Present the problem + options (keep the original at a new angle / pivot / redefine) and get the user's explicit decision first. You may strongly recommend, but the user owns the pivot.
- This command describes the world; it does not commit us to anything. Decisions live in `/strategy`.
- The same topic (tech, marketing, design) appears here as "what competitors do" (observation) and again in `/strategy` as "what we do" (decision) — that is by design, not duplication.
