# atheerium.github.io — Operating Manual for AI Agents

> **First thing:** Read `STATE.md` for the current site inventory and what's pending. This file covers conventions and workflow.

## Project Philosophy

- **Knowledge-first.** Every page should be useful weeks after it's written. No filler.
- **Markdown-native.** Content lives in `src/content/<collection>/`. Write in Markdown, Astro renders it.
- **Fast and minimal.** No unnecessary JS, no CSS frameworks, no client-side complexity.
- **Build in public.** Write as if readers are watching.

## Tech Stack

- **Framework:** Astro 7 (`"astro": "^7.1.3"`)
- **Package manager:** pnpm 11 (CI uses `pnpm install --frozen-lockfile`)
- **Node:** `>=22.12.0`
- **Hosting:** GitHub Pages (via `actions/deploy-pages@v4`)
- **Integrations:** `@astrojs/sitemap` (auto-generates sitemap), `@astrojs/rss` (used at `/rss.xml`)
- **TypeScript:** `astro/tsconfigs/strict`

## Content Collections (5)

```
src/content/
├── articles/     # Evergreen writing — domain investing, freelancing, automation
├── research/     # Original analysis — market studies, keyword reports, data
├── domains/      # Domain portfolio, sales, case studies
├── projects/     # Tools and systems I've built
└── notes/        # Quick notes, observations, how-to guides
```

Collection schema is in `src/content.config.ts` (NOT `src/content/config.ts`).

## Frontmatter

All collections share these required fields:

```yaml
---
title: "Page Title"
description: "One sentence — appears in listings and SEO."
pubDate: YYYY-MM-DD
tags: ["tag1", "tag2"]
draft: false  # hides from production
---
```

**Optional on articles, research, domains, projects:** `updatedDate: YYYY-MM-DD`  
**Projects only also accept:**
```yaml
status: "active" | "archived" | "planned"
url: "https://..."
```

Notes collection does NOT have `updatedDate` or `status`/`url`.

## URL Conventions (Critical)

- `trailingSlash: 'always'` in `astro.config.mjs` — all internal links MUST end with `/`
- `build.format: 'directory'` — detail pages generate `/section/slug/` directories
- Slugs are derived from filenames (kebab-case) with `.md` stripped: `my-post.md` → `.../my-post/`
- All `[...slug].astro` pages use the same pattern: `getCollection()` → filter drafts → `getStaticPaths()` → `render()`

## Layout.astro Props

When creating pages, pass these to `<Layout>`:

| Prop | Required? | Notes |
|---|---|---|
| `title` | yes | Renders as "Title — Atheerium" |
| `description` | no | Defaults to site description |
| `image` | no | OG image path, default `/og-default.png` |
| `pubDate` | no | Triggers BlogPosting JSON-LD if present |
| `tags` | no | Rendered as `<meta keywords>` |

## Navigation

**Nav bar** (top): Home · articles · research · projects · domains [23 for sale] · notes · services · contact · about
**Footer**: adds services, contact, tools, resources, now

When adding a section, update BOTH nav (in `Layout.astro`) and footer.

## SEO (All Auto — Just Provide Correct Frontmatter)

- Title renders as "Title — Atheerium"
- Canonical URL, OG tags, Twitter card, keywords meta — all derived from frontmatter in `Layout.astro`
- JSON-LD structured data (BlogPosting or WebPage) generated automatically
- RSS feed at `/rss.xml` includes articles + research + notes
- `robots.txt` allows all, points to `/sitemap-index.xml`
- **Site is NOT yet submitted to Google Search Console** — do not claim it's indexed

## Writing Guidelines

- Write in plain, direct English. No marketing fluff, no AI-isms.
- Em dashes break the Astro YAML frontmatter parser — use `--` (two hyphens) inside `---` blocks instead.
- Categories are broad (see STATE.md). Tags are specific and grow organically.
- Every article should link to 2-3 other pages internally.
- Preferred reading level: clear enough for a domain investor, technical enough for a developer.

## Initialization Checklist for New Agents

When starting work on this repo for the first time in a session:

1. Read this file (AGENTS.md) for project conventions
2. Read STATE.md for current site inventory and pending work
3. Read the relevant content collection(s) before editing
4. Run `pnpm build` before committing to verify no errors

## Commands

```bash
pnpm dev           # dev server
pnpm build         # production build (only verification check — no linter/formatter/typecheck scripts exist)
pnpm preview       # preview production build locally
```

There are NO lint, format, or typecheck scripts. `pnpm build` is the sole verification step.

## Content Workflow

1. Write Markdown in `src/content/<collection>/`
2. `pnpm dev` to preview
3. Commit and push to `main`
4. Site auto-deploys via GitHub Actions (build → deploy to Pages)

Never commit `dist/`, `.astro/`, or `node_modules/`.

## How to Add a New Content Section

1. Add collection in `src/content.config.ts` with its loader and schema
2. Create `src/pages/<section>/index.astro` — listing page
3. Create `src/pages/<section>/[...slug].astro` — detail page (follow existing pattern)
4. Add nav link in `src/layouts/Layout.astro` (both `<nav>` and `<footer>`)
5. Add homepage section in `src/pages/index.astro` if desired

## Misc

- `src/components/` is empty — there are no shared components. Layout and pages handle everything.
- `pnpm-workspace.yaml` is NOT a monorepo config — it only disables esbuild builds and pins a minimum release age for astro.
- Design: system font stack, #1a1a2e on #fafafa, max-width 720px, no dark mode, no animations.
- No CSS framework — all styles are in `Layout.astro`'s `<style>` tag.

## What NOT to Change Without Approval

- The layout system (`Layout.astro`)
- The color scheme or typography
- The build and deploy workflow
- Content collection schemas (without corresponding page changes)
