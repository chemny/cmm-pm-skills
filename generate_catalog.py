#!/usr/bin/env python3
"""生成 CATALOG.md —— cmm-pm-skills 插件的命令/技能全表（自动盘点，计数永不漂）。
用法：在 repo 根跑 `python3 generate_catalog.py`。改了命令/技能后重跑即可。
只读取，不修改命令/技能本身；唯一产物是 CATALOG.md。
"""
import os, re, glob

PLUGIN = "cmm-pm-skills"
ROOT = os.path.dirname(os.path.abspath(__file__))


def frontmatter_field(path, field):
    """取 markdown frontmatter 里某字段的值（取首行、去引号）。取不到返回空串。"""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return ""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return ""
    fm = m.group(1)
    fm = re.sub(r"^description:\s*>-?\s*$\n((?:\s+.*\n?)+)", lambda x: "description: " + x.group(1).strip().split("\n")[0] + "\n", fm, flags=re.M)
    fmm = re.search(rf"^{field}:\s*(.+)$", fm, re.M)
    if not fmm:
        return ""
    val = fmm.group(1).strip().strip('"').strip("'").strip()
    return val


def main():
    cmd_dir = os.path.join(ROOT, PLUGIN, "commands")
    skill_dir = os.path.join(ROOT, PLUGIN, "skills")

    cmds = []
    for p in sorted(glob.glob(os.path.join(cmd_dir, "*.md"))):
        name = os.path.basename(p)[:-3]
        if name.lower() == "readme":
            continue
        desc = frontmatter_field(p, "description")
        cmds.append((name, desc))

    skills = []
    for d in sorted(glob.glob(os.path.join(skill_dir, "*/"))):
        name = os.path.basename(d.rstrip("/"))
        desc = frontmatter_field(os.path.join(d, "SKILL.md"), "description")
        skills.append((name, desc))

    def clip(s, n=100):
        s = s.replace("|", "\\|").replace("\n", " ")
        return s if len(s) <= n else s[: n - 1] + "…"

    lines = []
    lines.append("# CATALOG — cmm-pm-skills 组件全表")
    lines.append("")
    lines.append("> 本文件由 `generate_catalog.py` 自动生成，**请勿手改**。改了命令/技能后重跑 `python3 generate_catalog.py`。")
    lines.append("")
    lines.append(f"**总览**：插件 `{PLUGIN}` ｜ 命令 {len(cmds)} ｜ 技能 {len(skills)} ｜ 合计 {len(cmds)+len(skills)} 个组件。")
    lines.append("")
    sc = sum(1 for p in sorted(glob.glob(os.path.join(skill_dir, "*/"))) if frontmatter_field(os.path.join(p, "SKILL.md"), "scenarios"))
    uo = sum(1 for p in sorted(glob.glob(os.path.join(cmd_dir, "*.md"))) if os.path.basename(p)[:-3].lower() != "readme" and frontmatter_field(p, "outputs"))
    full = sc == len(skills) and uo == len(cmds)
    tail = "（已全覆盖）" if full else "（其余为长尾，逐批补全）"
    lines.append(f"**覆盖率**：技能含 `scenarios` {sc}/{len(skills)} ｜ 命令含 `outputs` {uo}/{len(cmds)}{tail}。")
    lines.append("")
    lines.append(f"## 命令（{len(cmds)}）")
    lines.append("")
    lines.append("| 命令 | 说明 |")
    lines.append("|---|---|")
    for name, desc in cmds:
        lines.append(f"| `/{name}` | {clip(desc)} |")
    lines.append("")
    lines.append(f"## 技能（{len(skills)}）")
    lines.append("")
    lines.append("| 技能 | 说明 |")
    lines.append("|---|---|")
    for name, desc in skills:
        lines.append(f"| `{name}` | {clip(desc)} |")
    lines.append("")

    out = os.path.join(ROOT, "CATALOG.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✓ 已生成 CATALOG.md：命令 {len(cmds)} + 技能 {len(skills)} = {len(cmds)+len(skills)} 个组件")


if __name__ == "__main__":
    main()
