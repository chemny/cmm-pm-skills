# CLAUDE.md

Guidance for AI agents (Claude Code, Cowork, and others) working in this repository. This file is the single source of truth for how the project is structured and maintained.

## Project Overview



## ⚠️ Conventions (read first)

**Every command/skill must follow [`CONVENTIONS.md`](CONVENTIONS.md)** — the repo-wide, product-agnostic work discipline: §0 top principle (truth > completeness), how to ask for inputs (Class A/B, echo-then-request, plain language, no popup), atomic keyword integrity, classify competitors by category, search-engine + source-tier discipline, depth bar, objectivity (risk + opportunity, giants ≠ kill), methodology-stays-backstage, no-fabrication, segment-not-aggregate, and a pre-delivery provenance/red-team check. Individual commands only encode their **stage-specific** logic and inherit the rest — do not re-write these rules per command.

**Distribution (important):** the repo-root `CONVENTIONS.md` is the **master (edit only here)**. Because a plugin installs by directory, the root file does NOT ship with it — so the plugin carries a **synced copy** at `cmm-pm-skills/CONVENTIONS.md`, and commands point to `../CONVENTIONS.md` (plugin-local). **After editing the master, run `./sync_conventions.sh`** to propagate.

## Repo Structure

```
cmm-pm-skills/                       <- repo root (marketplace)
├── .claude-plugin/marketplace.json  <- marketplace manifest (lists the single plugin)
├── CLAUDE.md                        <- this file (agent guidance, single source of truth)
├── AGENTS.md                        <- pointer to CLAUDE.md (for non-Claude agents)
├── CONVENTIONS.md                   <- master discipline (edit here, then sync)
├── PIPELINE.md                      <- full-pipeline overview
├── README.md / README.en.md         <- public documentation (GitHub)
├── LICENSE                          <- MIT
├── sync_conventions.sh              <- copy master CONVENTIONS into the plugin
├── validate_plugins.py              <- plugin validator
├── _design/                         <- methodology blueprints / checklists
├── _runs/                           <- end-to-end examples (+ per-project _state.yaml)
└── cmm-pm-skills/                   <- THE single plugin (whole suite)
    ├── .claude-plugin/plugin.json   <- plugin manifest
    ├── CONVENTIONS.md               <- synced copy (ships with the plugin)
    ├── README.md                    <- plugin documentation
    ├── commands/{command}.md        <- 46 commands (one file each)
    └── skills/{skill}/SKILL.md      <- 70 skills (one folder each)
```

### Single plugin: `cmm-pm-skills`

The whole suite is now **one plugin** (`cmm-pm-skills`) — 46 commands + 70 skills. Earlier it was 10 separate `pm-*` plugins; they were merged so users install once (`cmm-pm-skills@cmm-pm-skills`) and get everything, with `/cmm-pm-skills` as the single entry command. Because everything is one plugin, all command↔skill references are intra-plugin (the old "no cross-plugin references" caution no longer constrains the suite).

Capability groups inside the plugin: orchestration (`/cmm-pm-skills` + `pipeline-orchestration`), market research, product discovery, product strategy, execution (PRD/wireframe/tech-design/stories/tests/OKRs/roadmap…), go-to-market, data analytics, marketing/growth, AI-shipping, and a PM toolkit.

## Key Design Rules

- **Skills = nouns/concepts.** Frameworks and analytical knowledge Claude auto-loads when the topic matches (`lean-canvas`, `pre-mortem`, `market-sizing`).
- **Commands = verbs.** User-triggered workflows that chain one or more skills (`/write-prd`, `/discover`, `/plan-launch`).
- **No cross-plugin references.** Commands suggest follow-ups in natural language only ("Want me to design growth loops?"). Never hard-reference a command from another plugin — plugins install independently, so a hard reference can break.
- **Intra-plugin "Uses" references are fine** — skills and commands in the same plugin always ship together.
- Commands use a single `$ARGUMENTS` placeholder. Skills need no placeholders (they read context from the conversation).
- **Frontmatter required:** Skills need `name` + `description`; commands need `description` + `argument-hint`.
- **Frontmatter recommended (better triggering + discoverability):** skills add `scenarios:` (≈3 example user utterances, inline YAML list) to sharpen auto-loading; commands add `outputs:` (and `uses:` when they apply a named skill). Coverage is tracked in `CATALOG.md` (`覆盖率` line); roll out across all components incrementally — these are inline-flow YAML lists so the validator parses them.
- A skill's `name` **must match its directory name**.
- Skills can be force-loaded with `/plugin-name:skill-name` or `/skill-name`.
- Keep frontmatter lean (always loaded); put detail in the SKILL.md body (loaded when triggered) — progressive disclosure.

## What's Visible Where

| Location | Visible in | Notes |
|----------|-----------|-------|
| `marketplace.json` → `description` | Cowork marketplace browser, Claude Code | One-liner for the whole marketplace |
| `plugin.json` → `description` | Cowork plugin list, Claude Code | Per-plugin summary; concise and functional |
| `SKILL.md` frontmatter → `description` | Cowork skill list, Claude auto-loading | Include trigger phrases so Claude loads the skill at the right time |
| Command frontmatter → `description` + `argument-hint` | Cowork and Claude Code (typing `/`) | Short and actionable |
| `README.md` (repo root) | GitHub only | Full docs; not loaded by Claude at runtime |

Descriptions in `plugin.json` and the repo `README.md` should stay aligned (identical text).

## Versioning

- All versions are currently **2.0.0** — `marketplace.json` and all 9 `plugin.json` files.
- **Keep every version in sync.** There is no independent per-plugin versioning.
- Bump any `plugin.json` → also bump `marketplace.json`, and vice-versa (bump all 9 to match).

## Article Links in Skills (Further Reading)

- **Tone must stay neutral** — no promotional language, no CTAs, no "subscribe"/"check out". Just the article title and URL.
- Claude surfaces these links based on conversational relevance, not on every response.
- Posts whose title contains "Masterclass" or "Course" are video courses — tag them `(video course)`.

## Operational Procedures

### After editing CONVENTIONS.md (the master)
- Run `./sync_conventions.sh` to copy it into the plugin (`cmm-pm-skills/CONVENTIONS.md`), so the installed plugin stays self-contained. Never hand-edit the plugin's copy — edit the master and sync.

### After any skill/command change
1. Run `python3 validate_plugins.py` from the repo root to check all plugins.
2. Run `python3 generate_catalog.py` to refresh `CATALOG.md` (component counts auto-update there — single source of truth for "what's in the suite").
3. If skills/commands were added or removed, update the counts in `README.md` and the `marketplace.json` description to match `CATALOG.md`.
4. Bump versions across all manifests (see Versioning).

### After a description change
- A `plugin.json` description changed → check whether `README.md` needs the same edit (they stay aligned).
- A `SKILL.md` description changed → no other sync needed (it's the single source for that skill).

## Validation

`validate_plugins.py` checks: `plugin.json` required fields / name match / semver / author / keywords; skill frontmatter and name-matches-directory; command frontmatter (`description` + `argument-hint`); README presence; and intra-plugin command→skill references.

```
python3 validate_plugins.py
```

## What to Suggest After Completing Work

Offer relevant follow-ups:
- After structural changes: "Want me to run the validator?"
- After adding/removing skills or commands: "Should I update the counts in README.md and marketplace.json?"
- After editing descriptions: "Should I sync this to README.md / plugin.json?"
- After any repo change: "Want me to bump the version?"
