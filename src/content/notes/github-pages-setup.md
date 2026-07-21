---
title: "GitHub Pages Setup Notes"
description: "How I set up this site — Astro + GitHub Pages with automatic deployment."
pubDate: 2026-07-21
tags: ["meta", "astro", "github-pages"]
---

## Stack

- **Framework:** Astro 7
- **Hosting:** GitHub Pages (free)
- **Deployment:** GitHub Actions (automatic on push to main)
- **Domain:** atheerium.github.io

## Setup steps

1. Create repo named `atheerium.github.io`
2. Scaffold Astro project
3. Install `@astrojs/sitemap`
4. Configure for GitHub Pages (`site: 'https://atheerium.github.io'`)
5. Create GitHub Actions workflow
6. Enable Pages → GitHub Actions in repo settings

## Key config

In `astro.config.mjs`:
- `site` set to the GitHub Pages URL
- `trailingSlash: 'always'` for cleaner URLs
- `build.format: 'directory'`

## Deployment

Every push to `main` triggers the workflow, builds the site, uploads the artifact, and deploys to Pages. No manual steps.
