# cmm-pm-skills

[中文](./README.md) | English

cmm-pm-skills is a product-manager workflow skill suite for PMs, founders, solo builders, and agent users. It turns every stage from market to launch into a callable command, and turns scattered ideas and research into real, usable deliverables (market analysis, PRD, prototype, tech design…) so later design, engineering, testing, and launch have a clearer starting point.

It supports market analysis, demand insight, product strategy, PRD, and UI/tech design, and it can run all the way through user stories, testing, launch, and data iteration — with every stage sharing one work discipline.

> Upstream credit: built on [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — it reworks each stage command on top of that plugin skeleton and adds a shared discipline `CONVENTIONS.md` plus UI-design (⑤) and tech-design (⑥) stages. Original copyright is retained in [LICENSE](./LICENSE).

## Who Is This For?

This suite is designed for:

- **PMs, founders, and solo builders** using Claude Code / Codex;
- Anyone who wants an idea → PRD → prototype pipeline where **every step is evidence-based and won't be hand-waved by the AI**;
- Individuals or small teams who need scattered research distilled into deliverable, traceable artifacts.

## What It Does

Generic AI gives you fluent text that is often shallow, prone to fabrication, and drifts off-target. This suite turns each PM stage into a command that follows one discipline: inherit upstream (no re-invention), research and triangulate its own facts, never fabricate, and hand the decision to you.

What you get is not talk but usable deliverables — a data-grounded market analysis, a buildable PRD, a clickable prototype, a grounded tech design.

## Capabilities

Listed in real product-development order: the stages that decide "whether and how to build" come first; delivery and iteration come later.

| Stage | Command | Output |
|---|---|---|
| ① Market analysis | `/market-analysis` | market / users / buyer / competitors / disruption (data-grounded) |
| ② Demand insight | `/insight` | real need + risk verdict + primary-validation plan |
| ③ Strategy | `/strategy` | positioning / moat / business model / pricing / play |
| ④ PRD | `/write-prd` | buildable PRD (need + features + flow + UX + data + edge cases) |
| ⑤ UI design | `/wireframe` | Mermaid flow/state + clickable HTML prototype + spec |
| ⑥ Tech design | `/tech-design` | stack / architecture / data / spike resolution / conflict check |
| ⑦ User stories | `/write-stories` | stories + acceptance criteria (traceable) |
| ⑧ Testing | `/test-scenarios` | test cases (happy / edge / error) |
| ⑩ Launch | `/plan-launch` etc. | GTM plan |
| ⑪ Data/iterate | `/analyze-cohorts` etc. | metrics → back to ② |

> Full overview in [PIPELINE.md](./PIPELINE.md); shared discipline in [CONVENTIONS.md](./CONVENTIONS.md). ⑥ implementation / ⑨ engineering are out of scope.

## Platform Compatibility

Claude Code supports commands + skills; Codex CLI supports skills (triggered via natural language); other agents (Cursor / Gemini CLI, etc.) can use the skills by copying the `skills/` folders.

## Install

This repo is a multi-plugin Claude Code marketplace. One command installs all 9 plugins:

```bash
claude plugin marketplace add chemny/cmm-pm-skills && \
for p in pm-market-research pm-product-discovery pm-product-strategy pm-execution \
         pm-go-to-market pm-data-analytics pm-marketing-growth pm-ai-shipping pm-toolkit; \
do claude plugin install $p@cmm-pm-skills; done
```

After installing, start a fresh agent session so it can rescan plugins.

## Quick Start

Ask your agent:

```text
/market-analysis one-line description of your product idea
```

Expected result:

```text
It first confirms the core inputs with you (product / segment / market / monetization),
then runs a data-driven market analysis, ends with a risk verdict, and asks whether to
proceed. Move stage by stage.
```

## Usage Examples

Real end-to-end cases in [`_runs/`](./_runs):

```text
_runs/voice-ime/   — "sayit" (a personalized voice input method): market analysis → PRD / prototype / tech design
```

```text
_runs/natgeo-video/  — an "English-article-to-video learning tool": market analysis and demand insight
```

## How It Works

- **Commands = stage actions**, inheriting upstream output and encoding only stage-specific logic;
- The **shared discipline** lives in the root `CONVENTIONS.md` (master); each plugin carries a synced copy, so it's inherited on install;
- Every stage: research → conclusion + risks → the decision is yours.

## Repository Structure

```text
cmm-pm-skills/
├── CONVENTIONS.md          shared discipline (master)
├── PIPELINE.md             full-pipeline overview
├── sync_conventions.sh     master → per-plugin sync
├── validate_plugins.py     contract validation
├── pm-*/                   9 plugins (commands/ + skills/ + bundled CONVENTIONS copy)
├── _design/                methodology blueprints / checklists
└── _runs/                  end-to-end examples
```

## Requirements

- Claude Code or Codex CLI;
- Some commands need web search (market / competitor research);
- Optional: GitHub CLI (`gh`) for publishing.

## Maintenance

- Edit discipline → edit root `CONVENTIONS.md` → run `./sync_conventions.sh`;
- Edit commands/skills → run `python3 validate_plugins.py`.

## License

MIT. See [LICENSE](./LICENSE) (retains original author phuryn's copyright + CMM modifications).
