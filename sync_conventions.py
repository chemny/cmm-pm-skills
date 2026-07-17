#!/usr/bin/env python3
"""Sync the repository conventions into the distributable plugin."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "CONVENTIONS.md"
TARGETS = (ROOT / "cmm-pm-skills" / "CONVENTIONS.md",)


def main() -> None:
    content = SOURCE.read_text(encoding="utf-8")
    plugin_content = content.replace(
        "](cmm-pm-skills/skills/",
        "](skills/",
    )
    for target in TARGETS:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(plugin_content, encoding="utf-8")
        print(f"synced -> {target.relative_to(ROOT)}")
    print(f"done: synced {len(TARGETS)} plugin(s)")


if __name__ == "__main__":
    main()
