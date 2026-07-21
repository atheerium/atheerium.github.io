# atheerium.github.io — Operating Manual for AI Agents

## Project Philosophy

- **Knowledge-first.** Every page should be useful weeks after it's written. No filler, no fluff.
- **Markdown-native.** Content lives in `src/content/`. Write in Markdown, Astro renders it.
- **Fast and minimal.** No unnecessary JavaScript, no CSS frameworks, no client-side complexity.
- **Build in public.** This is a public knowledge base — write as if readers are watching.

## Content Structure

```
src/content/
├── articles/    # Evergreen writing — domain investing, freelancing, automation
├── research/    # Original analysis — market studies, keyword reports, data
├── domains/     # Domain investing — portfolio, sales, case studies
├── projects/    # Tools and systems I've built
└── notes/       # Quick notes, observations, how-to guides
```

## Frontmatter Format

Every content file **must** start with:

```yaml
---
title: "Title Here"
description: "One sentence summary — appears in listings and SEO."
pubDate: YYYY-MM-DD
tags: ["tag1", "tag2"]
draft: false  # Set true to hide from production
---
```

Projects also accept:
```yaml
status: "active" | "archived" | "planned"
url: "https://..."
```

## Naming Conventions

- Files: `kebab-case.md`
- Slugs match filenames (Astro auto-derives from filename)
- Tags: lowercase, single words or hyphenated

## Deployment

- Every push to `main` triggers GitHub Actions
- Builds with `pnpm build` → deploys `dist/` to GitHub Pages
- Never commit `dist/`, `.astro/`, or `node_modules/`
- Verify locally: `pnpm build` before pushing

## SEO Requirements

Every page must have:
1. Unique `title` (will render as "Title — Atheerium")
2. `description` tag
3. Canonical URL (auto-configured)
4. Open Graph metadata (auto-from frontmatter)
5. Tags as keywords (auto-from frontmatter)

The `Layout.astro` component handles all of the above. Just provide correct frontmatter.

## Design Principles

- System font stack — no custom fonts, no web font loading
- Black text on light background (#1a1a2e on #fafafa)
- Max content width: 720px
- No dark mode toggle (keep it simple)
- No animations or transitions
- Responsive by default

## How to Add a New Section

1. Create a new collection in `src/content/config.ts`
2. Create `src/pages/<section>/index.astro` (listing page)
3. Create `src/pages/<section>/[...slug].astro` (detail page)
4. Add navigation link in `src/layouts/Layout.astro`
5. Add to homepage sections in `src/pages/index.astro`

## What NOT to Change Without Approval

- The layout system (Layout.astro)
- The color scheme or typography
- The build and deploy workflow
- Content collection schemas (without corresponding page changes)

## Tech Stack

- **Framework:** Astro 7
- **Package manager:** pnpm
- **Hosting:** GitHub Pages
- **Integrations:** @astrojs/sitemap

## Content Workflow

1. Write Markdown in `src/content/<collection>/`
2. Run `pnpm dev` to preview
3. Commit and push
4. Site auto-deploys via GitHub Actions

## Contact

- X: @Atheerium
- GitHub: @atheerium
