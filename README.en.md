# cmm-pm-skills

> A **product-manager workflow** skill suite: every stage from market to launch becomes a callable command that produces a real, usable deliverable — all sharing one work discipline.
> 🌐 中文：[`README.md`](README.md)

> **Upstream credit**: This project is built on [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — it reworks each stage command on top of that plugin skeleton and adds a shared discipline `CONVENTIONS.md` plus UI-design (⑤) and tech-design (⑥) stages. Original copyright is retained in [`LICENSE`](LICENSE).

## Who it's for
- **PMs, founders, and solo builders** using Claude Code / Codex;
- Anyone who wants an idea → PRD → prototype pipeline where **every step is evidence-based and won't be hand-waved by the AI**.

## What it solves
Generic AI gives you fluent text that is **shallow, prone to fabrication, and drifts off-target**. This suite turns each PM stage into a command that **inherits upstream (no re-invention), researches and triangulates its own facts, never fabricates, and hands the decision to you** — producing deliverables you can actually use.

## Core capabilities (end-to-end pipeline)
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

> Full overview in [`PIPELINE.md`](PIPELINE.md); shared discipline in [`CONVENTIONS.md`](CONVENTIONS.md). ⑥ implementation / ⑨ engineering are out of scope.

## Platform compatibility
| Platform | Support |
|---|---|
| Claude Code | ✅ commands + skills |
| Codex CLI | ✅ skills (trigger workflows via natural language) |
| Others (Cursor / Gemini CLI…) | skills only (copy the `skills/` folders) |

## Install (Claude Code)
```bash
claude plugin marketplace add chemny/cmm-pm-skills && \
for p in pm-market-research pm-product-discovery pm-product-strategy pm-execution \
         pm-go-to-market pm-data-analytics pm-marketing-growth pm-ai-shipping pm-toolkit; \
do claude plugin install $p@cmm-pm-skills; done
```

## Quick start
```text
/market-analysis one-line description of your product idea
```
It first **confirms the core inputs with you** (product / segment / market / monetization), then runs a data-driven market analysis, ends with a risk verdict, and asks whether to proceed. Move stage by stage.

## Usage examples
Real end-to-end cases in [`_runs/`](_runs):
- `_runs/voice-ime/` — "sayit" (a personalized voice input method) from market analysis to PRD / prototype / tech design;
- `_runs/natgeo-video/` — an "English-article-to-video learning tool" market analysis and demand insight.

## How it works
- **Commands = stage actions**, inheriting upstream output and encoding only stage-specific logic;
- The **shared discipline** lives in the root `CONVENTIONS.md` (master); each plugin carries a synced copy, so it's **inherited on install**;
- Every stage: research → conclusion + risks → **the decision is yours**.

## Repository structure
```
CONVENTIONS.md          shared discipline (master)
PIPELINE.md             full-pipeline overview
sync_conventions.sh     master → per-plugin sync
validate_plugins.py     contract validation
pm-*/                   9 plugins (commands/ + skills/ + bundled CONVENTIONS copy)
_design/                methodology blueprints / checklists
_runs/                  end-to-end examples
```

## Requirements / configuration
- Claude Code or Codex CLI;
- Some commands need web search (market / competitor research).

## Maintenance
- Edit discipline → edit root `CONVENTIONS.md` → run `./sync_conventions.sh`;
- Edit commands/skills → run `python3 validate_plugins.py`.

## License
MIT, see [`LICENSE`](LICENSE) (retains original author phuryn's copyright + CMM modifications).
