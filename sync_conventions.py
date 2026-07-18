#!/usr/bin/env python3
"""Sync portable runtime resources into the distributable plugin skills."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
PLUGIN_ROOT = ROOT / "cmm-pm-skills"
SOURCE = ROOT / "CONVENTIONS.md"
PLUGIN_CONVENTIONS = PLUGIN_ROOT / "CONVENTIONS.md"
SKILL_REFERENCES = PLUGIN_ROOT / "skills" / "main" / "references"
SKILL_CONVENTIONS = SKILL_REFERENCES / "CONVENTIONS.md"
SOURCE_COMMANDS = PLUGIN_ROOT / "commands"
SKILL_COMMANDS = SKILL_REFERENCES / "commands"


def main() -> None:
    content = SOURCE.read_text(encoding="utf-8")
    plugin_content = content.replace(
        "](cmm-pm-skills/skills/",
        "](skills/",
    )
    skill_content = plugin_content.replace(
        "](skills/main/references/",
        "](",
    )

    for target, target_content in (
        (PLUGIN_CONVENTIONS, plugin_content),
        (SKILL_CONVENTIONS, skill_content),
    ):
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(target_content, encoding="utf-8")
        print(f"synced -> {target.relative_to(ROOT)}")

    SKILL_COMMANDS.mkdir(parents=True, exist_ok=True)
    command_count = 0
    for source_command in sorted(SOURCE_COMMANDS.glob("*.md")):
        command_content = source_command.read_text(encoding="utf-8").replace(
            "../skills/main/references/",
            "../",
        )
        target_command = SKILL_COMMANDS / source_command.name
        target_command.write_text(command_content, encoding="utf-8")
        command_count += 1

    print(f"synced -> {SKILL_COMMANDS.relative_to(ROOT)} ({command_count} commands)")
    print("done: plugin root and skill-only fallback are aligned")


if __name__ == "__main__":
    main()
