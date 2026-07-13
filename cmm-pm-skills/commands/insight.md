---
description: Run demand insight (需求洞察) — frame the real job-to-be-done, analyze concrete scenarios/segments, grade evidence, name the leap-of-faith assumption, and produce a PRIMARY-research validation plan. Desk research yields a graded HYPOTHESIS, never a validated GO.
argument-hint: "<need / market-analysis conclusion / product idea>"
uses: [opportunity-solution-tree]
outputs: ["真需求(JTBD)+风险结论+一手验证计划"]
---

> **Capability loading:** For each capability named in `uses`, use its visible Skill when present; otherwise read `../skills/main/references/capabilities/<name>.md` completely before applying it.

# /insight -- 需求洞察 (Demand Insight)

Stage ② of the pipeline. It answers: **what does the user really need — and what would it actually take to KNOW it's real?** Input: the market-analysis conclusion (or a raw idea). Output: a graded need hypothesis + a primary-research validation plan.

> **Core rule — desk research cannot validate a need.** Searching the web yields a HYPOTHESIS plus secondhand analogs; it can NEVER prove that *your* target users have this need and will pay. Only **primary evidence** — real user interviews (Mom Test), observed behavior, paid experiments — validates a need. So this command's default verdict is **"strong hypothesis — UNVALIDATED"**, never a GO. Dressing up desk data as a validated need is the #1 failure mode; do not do it.

> **Collaborate + don't block (CONVENTIONS §0c).** Confirm core framing (the need statement, the target) **with the user**, don't autopilot. Grade evidence honestly and flag what's unvalidated, but **if the user has decided to proceed, help them — surface risks, never refuse or stall the pipeline.** The decision is theirs.
> **Do your OWN research — don't just expand ①.** Inheriting ①'s persona ≠ skipping fresh fact-checking. This stage must run its own searches for need evidence (real user complaints/reviews, ToB pricing/payment signals, how rivals' users actually behave), **triangulate (≥3 sources/≥2 classes), and loop back to fill gaps** (CONVENTIONS §4/§8). Expanding the upstream report without new verification is a fail.
> **Follow [`CONVENTIONS.md`](../CONVENTIONS.md)** for all cross-cutting discipline (how to ask, plain language, depth, honesty, methodology-backstage, red-team). This command adds only the **insight-specific** logic.

## Step 1 — Frame the real job (JTBD)
- The functional job + the emotional/social job. Not the feature — the job.
- State it: *"When ___ (situation/trigger), I want to ___ (motivation), so I can ___ (outcome)."*
- Capture the current workaround and the **struggling moment** (when/why it hurts today).
- Optionally apply the **opportunity-solution-tree** skill to connect the job to the outcome.

## Step 2 — Segment path: inherit if available, intake if standalone
Preferred path: inherit the data-grounded **user persona, typical scenarios, buyer/willingness-to-pay, and viable target segment** from `/market-analysis` (①). **Insight consumes them — it does not re-invent who the user is.**

Standalone path (§0d): if ① is missing, do **not** stop by default. Enter a short intake and ask only the Class A fields needed for this stage:
- target user / segment;
- concrete usage situation;
- geography;
- commercial direction / who may pay.

Then proceed with a clear caveat: **"缺少 ① 市场分析，上游画像/市场证据不足；本次只产出需求假设与一手验证计划。"** Any segment or scenario from the user is treated as user-provided input, not validated market fact. If the user cannot provide these fields, ask and wait; do not fabricate.

If you have ①, **restate the inherited segment + scenario in one line** as the basis, then drill into the specific need below. Optional refinements must be **sourced**, not invented, and flagged as a refinement of ①'s finding.

A fabricated persona/scenario, or silently "discovering" the user from scratch while pretending it came from ①, is a fail.

## Step 3 — Need hypothesis with graded evidence
Apply the 4 tests, but **grade every claim** — do not assert:
| Test | Grade each as → |
|---|---|
| ① Painful enough (workaround / pays / complains) | 〔primary 一手〕 real users/behavior · 〔secondary 二手〕 analog/overseas · 〔unverified 未验证〕 none |
| ② Frequent / urgent | same grading |
| ③ Nameable, sized segment | same grading |
| ④ Willing to pay / switch | same grading |

**Grading rule:** a test counts as *passed* only with **〔一手〕** evidence. **〔二手/未验证〕 means hypothesis only.** Desk-only research therefore caps the verdict at **"强假设（待一手验证）"** — never "validated / GO".

## Step 4 — Name the leap-of-faith assumption
- The single belief that, if false, kills the whole thing. State it sharply.
- Apply **identify-assumptions-new/existing** + **prioritize-assumptions** to surface and rank it.

## Step 5 — Primary-research validation plan (the main deliverable)
- **Interviews (Mom Test):** ask about **past concrete behavior**, never hypotheticals ("would you pay?"). Who to talk to, how many, what to learn. Apply the **interview-script** skill.
- **Behavioral signals:** what existing usage/data would (dis)confirm the need.
- **Experiments:** fake-door / landing page, concierge MVP, pricing test — each with an explicit **success threshold**. Apply **brainstorm-experiments-new/existing**.
- Sequence cheapest-first; state how long to a signal.

## Output (methodology backstage, plain headings — CONVENTIONS §7)
Save as markdown. Use result-oriented headings, no framework jargon:
```
# 需求洞察：[主题]
日期 · 输入来源

## 真需求（要做的事 / JTBD）        当___，用户想___，以便___
## 目标场景与人群（具体）            一个滩头人群 + 1–2 个真实场景
## 需求假设与证据分级                四关，每条标〔一手/二手/未验证〕
## 生死假设                          若它为假，整个方向就垮的那一条
## 一手验证计划                      访谈(Mom Test)/行为信号/实验 + 成功阈值
## 结论                              默认「强假设·未验证」；写清"验证到什么程度才可 GO / PIVOT / KILL"
## 定位假设（给 PRD，标注"待验证"）  为[人群]的[任务]，提供[价值]——不同于[替代]，因为[理由]
```

## Next Steps
- "Run the validation plan first. Once the leap-of-faith assumption is confirmed by primary evidence → `/write-prd`."
- "Decide how we'd win (moat, model, pricing)? → `/strategy`. (Best after validation.)"

## Notes
- The deliverable people value here is the **validation plan**, not a confident verdict. Honesty > optimism.
- If the input is a market-analysis "PIVOT", run insight on the *pivoted* need, not the rejected one.
