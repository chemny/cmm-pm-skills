# cmm-pm-skills

[中文](./README.zh.md) | English

cmm-pm-skills is a product-manager workflow skill suite for PMs, founders, solo builders, and agent users. It turns every stage from market to launch into a callable command, and turns scattered ideas and research into real, usable deliverables (market analysis, PRD, prototype, tech design…) so later design, engineering, testing, and launch have a clearer starting point.

It supports market analysis, demand insight, product strategy, PRD, and UI/tech design, and it can run all the way through user stories, testing, launch, and data iteration — with every stage sharing one work discipline.

## Who Is This For?

This suite is designed for:

- **PMs, founders, and solo builders** using Claude Code / Codex;
- Anyone who wants an idea → PRD → prototype pipeline where **every step is evidence-based and won't be hand-waved by the AI**;
- Individuals or small teams who need scattered research distilled into deliverable, traceable artifacts.

## What It Does

Generic AI gives you fluent text that is often shallow, prone to fabrication, and drifts off-target. This suite turns each PM stage into a command that follows one discipline: inherit upstream (no re-invention), research and triangulate its own facts, never fabricate, and hand the decision to you.

What you get is not talk but usable deliverables — a data-grounded market analysis, a buildable PRD, a clickable prototype, a grounded tech design.

## Capabilities

**The entry command `/cmm-pm-skills`** gets you started in one line: run the whole pipeline, or just one stage (e.g. only a PRD). It keeps a per-project state ledger (no loss across sessions), gates each stage (risk verdict → you decide), and navigates the next step. The stages it coordinates are listed below in real product-development order: the stages that decide "whether and how to build" come first; delivery and iteration come later.

| Capability | What it helps you do |
|---|---|
| Market analysis (`/market-analysis`) | Ground market, users, buyers, competitors, and disruption opportunities in evidence. |
| Demand insight (`/insight`) | Separate real needs from assumptions and define a primary-validation plan. |
| Product strategy (`/strategy`) | Decide positioning, moat, business model, pricing, and strategic trade-offs. |
| PRD (`/write-prd`) | Produce buildable requirements covering features, flow, UX, data, and edge cases. |
| UI design (`/wireframe`) | Create flows, states, clickable HTML prototypes, and implementation-ready specs. |
| User stories (`/write-stories`) | Break requirements into traceable stories and acceptance criteria. |
| Tech design (`/tech-design`) | Ground stack, architecture, data, spikes, and implementation conflicts. |
| Testing (`/test-scenarios`) | Cover happy paths, boundaries, and failure cases. |
| Launch (`/plan-launch`) | Build a focused go-to-market plan. |
| Data iteration (`/analyze-cohorts`) | Turn product metrics into the next discovery cycle. |

> Full overview in [PIPELINE.md](./PIPELINE.md); shared discipline in [CONVENTIONS.md](./CONVENTIONS.md). ⑦ technical proposal / ⑨ engineering are out of scope.

## Platform Compatibility

Compatible with Claude Code, Codex, and OpenClaw. Claude Code exposes commands and skills; Codex exposes 13 focused skills, including `CMM PM Skills: Main`; OpenClaw discovers `main` as a model-visible, command-ready skill. The other 58 specialist methods stay available through internal routing.

## Install

Ask your current Agent to install and verify the repository for the client you are using:

```text
Install https://github.com/chemny/cmm-pm-skills for my current Agent client. Detect the correct plugin or skill location, install the suite, verify that CMM PM Skills: Main is discoverable, and report the result.
```

## Quick Start

Start with the main entry. In Codex, select the skill; in Claude Code, use the command:

```text
Codex: CMM PM Skills: Main
Claude Code: /cmm-pm-skills
```

Expected result:

```text
It asks how you want to start (run the whole pipeline, or just one stage like a PRD),
then gets to work; each stage ends with a risk verdict for you to approve before moving on.
No manual needed. Power users can also call a single command directly, e.g. /write-prd your idea.
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

- **Entry `/cmm-pm-skills`** routes you in one line: guide the whole pipeline, or jump straight to one stage;
- **Commands = stage actions**, inheriting upstream output and also callable standalone (§0d);
- The **shared discipline** lives in the root `CONVENTIONS.md` (master); the plugin carries a synced copy, so it's inherited on install;
- Every stage: research → conclusion + risks → the decision is yours.

## Repository Structure

```text
cmm-pm-skills/
├── CONVENTIONS.md          shared discipline (master)
├── PIPELINE.md             full-pipeline overview
├── sync_conventions.sh     master → plugin sync
├── validate_plugins.py     contract validation
├── cmm-pm-skills/          single plugin (46 commands + 13 visible skills + 58 internal capabilities)
├── _design/                methodology blueprints / checklists
└── _runs/                  end-to-end examples
```

## Requirements

- Claude Code or Codex CLI;
- Some commands need web search (market / competitor research);
- Optional: GitHub CLI (`gh`) for publishing.

## License

MIT. See [LICENSE](./LICENSE). Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); the original copyright is retained in LICENSE.
