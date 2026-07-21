---
title: "100 Pages: What I Learned Building This Site (And How You Can Build Your Own)"
description: "This site went from 3 articles to 100 pages in one day. Here's the stack, the workflow, and the lessons from building a content-driven website with AI agents."
pubDate: 2026-07-21
tags: ["blog", "building", "astro", "ai-agents", "web-development", "meta"]
---

This site started as a simple 3-article blog. In one focused session, it grew to 100 pages with 46 articles spread across 5 content categories.

Here's what I learned building it, the exact stack I used, and how you can build your own without spending money.

## The Stack

- **Framework:** Astro 7 (static site generator)
- **Hosting:** GitHub Pages (free, with custom domain support)
- **Database/backend:** Not needed (static site, content in markdown files)
- **Content:** Markdown files in content collections (articles, domains, research, projects, notes)
- **Deployment:** GitHub Actions (auto-deploys on push to main)
- **Agents:** Hermes Agent + OpenCode for content generation

**Total cost:** $12/year for the domain. Everything else is free.

## The Workflow

1. Write article as markdown file in `src/content/articles/`
2. Add frontmatter (title, description, date, tags)
3. Commit and push to main
4. GitHub Actions builds with Astro and deploys to GitHub Pages
5. Site updates in 60 seconds

The entire pipeline takes 2 minutes from writing to publishing.

## What I Learned About Content

1. **Solve real problems.** The articles that get the most engagement are the ones about specific problems: delivery costs, cold email failures, portfolio management. Generic "how to be productive" articles don't perform.

2. **Internal linking matters.** Every article links to 2-3 related ones. This keeps readers on the site longer and helps search engines understand the content structure.

3. **SEO is about structure.** Semantic headings (H1 → H2 → H3), clear meta descriptions, FAQ sections, and clean URLs. Skip the keyword stuffing.

4. **AI answers need explicit structure.** FAQ sections, clear definitions in opening paragraphs, and step-by-step processes help AI models (ChatGPT, Claude, Perplexity) extract and cite your content.

5. **Write for yourself first.** Every article on this site is something the author actually needed to know. That authenticity shows in the writing.

## How You Can Build Your Own

**Step 1:** Create a GitHub repo called `yourusername.github.io`
**Step 2:** Scaffold with Astro (`pnpm create astro`)
**Step 3:** Set up GitHub Pages deployment (static build, push to main)
**Step 4:** Organize content in collections (articles, projects, notes)
**Step 5:** Write your first 3 articles. Publish one, see how it feels, iterate.
**Step 6:** Add more collections as you expand.

The hardest part is starting. The first article takes the longest. By article 10, you have a system. By article 50, you have a resource.

## What Makes a Site Worth 100 Pages

Not all pages are equal. The 23 domain listing pages each took 2 minutes to generate. The 46 articles each took 5-10 minutes to research and write. The core pages (start, browse, about, services, contact) define the site's structure.

Quality over volume. But volume with quality beats either alone.

## FAQs

### Q: How long does it take to write a good article?
A: 5-10 minutes if you know the topic well. 20-30 minutes if you need to research.

### Q: How do you avoid duplicate content across 46 articles?
A: Each article addresses a specific problem with a specific solution. If two articles overlap, they link to each other rather than repeating.

### Q: Should I use AI to write articles?
A: AI is good for structure and first drafts. The examples, specific experiences, and honest mistakes should be yours.

### Q: What's the one thing that makes a site grow?
A: Publishing consistently. One article every day for 100 days beats 100 articles published in one day for long-term growth. But for starting, a big launch builds momentum.

---

*Related: [How I Use GitHub to Run My Business](/articles/github-for-business/) -- the infrastructure behind this site. [GitHub for Business](/articles/github-for-business/) -- all the tools I use.*
