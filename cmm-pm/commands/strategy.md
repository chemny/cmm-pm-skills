---
description: Decide how we win — positioning, moat, business model, pricing, growth, key tasks. Built on the persona/market from ① and the validated need from ②; grounded not invented; marked provisional if the need isn't validated yet.
argument-hint: "<product / the insight conclusion>"
uses: [pricing-strategy, monetization-strategy]
outputs: ["定位/壁垒/商业模式/定价/打法"]
---

# /strategy -- Product Strategy (how we win)

Stage ③ of the pipeline. It decides **"how we win"**: our positioning, moat, business model, pricing, growth, and the key tasks to execute. It turns the evidence from ①② into a defensible plan.

> **Inherit, don't invent.** Build on ①'s persona / buyer / willingness-to-pay / competition / disruption vectors, and ②'s need + leap-of-faith assumption. Every choice must trace to that evidence, or be marked **〔assumption / to-validate〕** (CONVENTIONS §9). The same topic ①② described as "the world" becomes here "our decision" — grounded in that evidence, not made up.
> **Risk flag, not a veto (CONVENTIONS §0c).** If ②'s need is still unvalidated, **note the risk** and which bets hinge on what ② must confirm — **but the decision is the user's.** Once the user has chosen this direction, **deliver a real, usable strategy** to help them win; surface risks, don't hedge every line into "暂定" or refuse. Confirm core choices (positioning, beachhead, model) **with the user**, don't autopilot.
> **Do your OWN research — don't just expand ①②.** Inheriting upstream ≠ skipping fresh fact-checking. This stage must search and **triangulate (≥3 sources/≥2 classes)** its own facts — rivals' real business models & pricing, ASR/LLM/deployment costs, moat/case evidence, market sizing — and **loop back to fill gaps** (CONVENTIONS §4/§8). A strategy written by expanding the upstream report without new verification is a fail.
> **Follow [`CONVENTIONS.md`](../CONVENTIONS.md)** for all cross-cutting discipline (truth>completeness, grounding/evidence-grade, objectivity, plain output, no-fabrication, red-team).

## Inputs (inherit from upstream)
- From ① market-analysis: persona, buyer & willingness-to-pay, competition, disruption vectors, market-level demand evidence.
- From ② insight: the validated (or hypothesized) need, the leap-of-faith assumption, and the validation status.
- If these are missing, **ask for them — don't fabricate** a persona or a validated need.

## Coverage checklist (internal — don't skip a dimension; OUTPUT uses plain headings, no jargon)
Each item must be **grounded in ①② or marked 〔assumption / to-validate〕**. Quality (rigor, data, sound conclusion) comes from this discipline, not from the framework name.
1. **Positioning & trade-offs** — who we serve, explicitly who we don't, the one-line position.
2. **Differentiation & moat** — what makes it hard to copy; **honest "no real moat yet" if so** — never invent one.
3. **Business model** — how we make money, who pays (C-end / ToB), a unit-economics sketch.
4. **Pricing** — model and price logic (apply **pricing-strategy** / **monetization-strategy** skills).
5. **Growth engine** — how we acquire & expand, specifically against free incumbents.
6. **Key metrics** — north star + a few input levers + guardrails.
7. **Core capabilities & key tasks** — build / buy / partner → hands off to ④ execution.
8. **Strategic risks** — what would invalidate this (carry ①'s bear case forward).

*(Optional light grouping for the author only, NOT shown in output — 定控制点=1,2 · 定打法=3,4,5,6 · 定关键任务=7. Use only if it aids clarity; never drop a dimension for it.)*

## Output (methodology backstage, plain result-oriented headings — CONVENTIONS §7)
Save as markdown. Plain headings; no "canvas / 三定 / Section N" labels. If the need is unvalidated, mark the title "条件性·暂定".
```
# 产品战略：[主题]    〔需求未验证时：条件性·暂定〕
日期 · 输入来源（①②的结论）

## 定位与取舍        为谁做、明确不为谁做、一句话定位
## 差异化与壁垒      凭什么赢、能不能被抄；没有真护城河就老实说
## 商业模式          怎么赚钱、谁买单（C端/ToB）、单位经济
## 定价              定价逻辑与价位
## 增长引擎          怎么获客与扩张（尤其面对免费巨头）
## 关键指标          北极星 + 输入指标 + 护栏
## 核心能力与关键任务  要建/买/合作什么 → 交给执行
## 战略风险          哪些会让这套战略失效（含①的看空）
## 结论              战略成立的前提；哪些取决于②的验证（未验证就写清"待验证才成立"）
### 来源/血缘        每条关键判断标注依据，或标〔假设/待验证〕
```

## Next Steps
- "If the need isn't confirmed yet, validate the open assumptions first (back to `/insight` ②)."
- "Turn the key tasks into a PRD / roadmap → `/write-prd`."
- "Pressure-test with a macro scan or Porter's Five Forces?"

## Notes
- Most early products have no real moat — acknowledge it honestly, don't manufacture one.
- The framework is just a coverage checklist; rigor and honesty come from CONVENTIONS, not from the headings.
