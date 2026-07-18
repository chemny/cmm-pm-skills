# Contributing


## How to Contribute

- **Bugs and small fixes** — open a PR directly.
- **New skills, commands, or larger changes** — open an issue first so we can discuss the approach.

## Guidelines

- Keep PRs focused — one change per PR.
- Follow existing patterns: skills are nouns (domain knowledge), commands are verbs (workflows).
- Every skill needs frontmatter with `name` and `description`. Every command needs `description` and `argument-hint`.
- Skill `name` must match its directory name.
- No cross-plugin references in commands. Suggest follow-ups in natural language only.
- Every contributor will be listed publicly.
- Python 3 is required for repository maintenance scripts (not for using the installed skills).
- Run the validator before submitting: `python3 validate_plugins.py` on macOS/Linux or `py -3 validate_plugins.py` on Windows.
- After editing the master `CONVENTIONS.md` or any file under `cmm-pm-skills/commands/`, run `python3 sync_conventions.py` on macOS/Linux or `py -3 sync_conventions.py` on Windows. This refreshes the skill-only runtime fallback.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
