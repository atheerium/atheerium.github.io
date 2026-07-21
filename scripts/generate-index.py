#!/usr/bin/env python3
"""Regenerate INDEX.md from content files. Run after adding/removing content."""
import os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(REPO, "src", "content")
COLLECTIONS = ["articles", "research", "domains", "projects", "notes"]

LABELS = {
    "articles": "Articles",
    "research": "Research",
    "domains": "Domains",
    "projects": "Projects",
    "notes": "Notes",
}

def parse_field(frontmatter, key):
    # Try quoted first
    m = re.search(rf'{key}:\s*"([^"]*)"', frontmatter)
    if m: return m.group(1)
    m = re.search(rf"{key}:\s*'([^']*)'", frontmatter)
    if m: return m.group(1)
    m = re.search(rf'{key}:\s*(.+?)$', frontmatter, re.MULTILINE)
    if m: return m.group(1).strip().strip('"').strip("'")
    return ""

def parse_frontmatter(filepath):
    """Extract frontmatter section between --- delimiters."""
    with open(filepath) as f:
        fm = ""
        in_fm = False
        for line in f:
            if line.strip() == "---":
                if not in_fm:
                    in_fm = True
                    continue
                break
            if in_fm:
                fm += line
    return fm

def build_index():
    lines = [
        "# INDEX.md -- Site Content Index",
        "",
        "> **Purpose:** Both humans and agents use this to see what content exists and avoid duplicates.",
        "> **When to update:** Run `python3 scripts/generate-index.py` after adding new content.",
        "> **Format:** Section, File, Path, Title, Date, Tags, Description",
        "",
    ]

    for col in COLLECTIONS:
        col_dir = os.path.join(CONTENT, col)
        if not os.path.isdir(col_dir):
            continue
        files = sorted(f for f in os.listdir(col_dir) if f.endswith(".md"))
        if not files:
            continue
        lines.append(f"## {LABELS.get(col, col)}")
        lines.append("")
        for fname in files:
            fpath = os.path.join(col_dir, fname)
            fm = parse_frontmatter(fpath)
            title = parse_field(fm, "title")
            desc = parse_field(fm, "description")
            pubdate = parse_field(fm, "pubDate")
            tags = parse_field(fm, "tags")
            slug = fname.replace(".md", "")
            url = f"/{col}/{slug}/"
            lines.append(f"- `{url}` -- {title}")
            if desc:
                lines.append(f"  - {desc[:200]}")
            if pubdate or tags:
                bits = []
                if pubdate: bits.append(pubdate)
                if tags: bits.append(f"[{tags}]")
                lines.append(f"  - {' / '.join(bits)}")
            lines.append("")

    # Static pages
    lines.append("---")
    lines.append("")
    lines.append("### Static Pages")
    lines.append("")
    lines.append("| Path | Description |")
    lines.append("|------|-------------|")
    static = [
        ("/", "Homepage"),
        ("/start/", "Curated entry point"),
        ("/about/", "Bio"),
        ("/contact/", "Contact info"),
        ("/services/", "Freelance offerings"),
        ("/now/", "Current focus"),
        ("/tools/", "Utilities"),
        ("/resources/", "Links and datasets"),
        ("/browse/", "Full site index"),
        ("/rss.xml", "RSS feed"),
    ]
    for path, desc in static:
        lines.append(f"| [{path}](https://atheerium.github.io{path}) | {desc} |")
    lines.append("")

    index_path = os.path.join(REPO, "INDEX.md")
    with open(index_path, "w") as f:
        f.write("\n".join(lines))
    print(f"INDEX.md regenerated: {len(lines)} lines, {len(files)} files indexed")

if __name__ == "__main__":
    build_index()
