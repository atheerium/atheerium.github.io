# BLOG.md — Content Standards & Publishing Philosophy

> **Purpose:** Standardize how content is written so every agent produces useful, rankable, non-duplicate articles that serve real people.
>
> **First rule:** Read `INDEX.md` before writing anything. Verify the topic hasn't been published.

---

## Content Philosophy (The Mental Model)

**Don't explain tools. Solve problems.**

Most blogs write: "Introducing Tool X — here's what it does."

This blog writes: "I had problem Y — here's how I solved it, and here's the tool that made it possible."

The tool is incidental. The problem and solution are the content.

**Three audiences, one question:** What real problem do they have right now?

| Audience | Problem | Article angle |
|----------|---------|---------------|
| Domain investors | "I buy domains that sit forever" | How to evaluate buyer demand before registering |
| Freelancers | "I can't get clients outside my country" | Remote selling systems that work without a reputation |
| Small business owners | "I lose money on operational chaos" | Simple tools that replace spreadsheets and WhatsApp chaos |

If an article wouldn't help you (the site owner) if you were in their shoes, don't write it.

---

## SEO Standards (for Google)

### On-Page SEO

- **Title:** Include primary keyword naturally. 50-60 chars. Format: "Solve Problem X: [Solution]"
- **Meta description:** 150-160 chars. One sentence that makes someone want to click.
- **URL:** Short, keyword-rich, no dates. `/articles/solve-problem-x/`
- **H1:** Same as title (auto from frontmatter)
- **H2/H3:** Include question phrases ("How do I...", "Why...", "What...")
- **Internal links:** Every article links to 2-3 other articles on this site
- **External links:** Link to authoritative sources (NameBio, Cloudflare docs, Astro docs)

### Keyword Strategy

- Target **long-tail keywords** (3-5 words) with clear search intent
- One primary keyword per article. Don't keyword-stuff.
- Use related terms naturally in body text
- Include the keyword in: title, H1, first paragraph, one H2

### Formatting for Readability

- Short paragraphs (2-4 sentences max)
- Subheadings every 200-300 words
- Lists, tables, or bold text for key takeaways
- Code blocks only when they illustrate a point (not walls of code)
- Keep reading level accessible — high school level, not PhD

---

## GEO Standards (for ChatGPT, Claude, Perplexity)

AI engines extract and cite content differently than Google. To rank there:

### 1. Answer Questions Directly

- Include a **FAQs section** or Q&A format in every article
- Put the answer in the first sentence after the question heading
- Use `### Q: What is X?` — `A: X is...` pattern

### 2. Structure for Extraction

- Use **clear H2/H3 headings that work as standalone answers**
- AI models scan headings to find relevant sections. If your heading is "Challenges," they skip it. If your heading is "Why Domain Cold Emails Get Ignored," they cite it.
- Use **bold** for key terms and definitions
- Include **numbered lists** — AI cites list items frequently

### 3. Cite Data and Sources

- AI engines favor content with specific numbers, dates, and statistics
- "I sent 3,000 emails" > "I sent many emails"
- Link to original data (NameBio, GitHub, your own research)

### 4. Depth Over Length

- Articles should be **800-1500 words** — deep enough to be authoritative, short enough to be readable
- Cover the topic comprehensively: what, why, how, when not to, alternatives
- Include a "when this doesn't work" section — shows balanced thinking, which AI favors

### 5. Semantic URLs

- `/articles/domain-cold-emails-get-ignored/` not `/articles/post-3/`
- Descriptive URLs get 11.4% more AI citations

### 6. Freshness Signals

- Update `updatedDate` in frontmatter when revising
- Link to recent sources (last 1-2 years)
- AI engines prefer recent content for time-sensitive topics

---

## Article Structure Template

```markdown
---
title: "Problem-Focused Title: With Solution Hint"
description: "One sentence. Includes keyword. Makes someone click."
pubDate: YYYY-MM-DD
tags: ["audience-tag", "topic-tag", "solution-tag"]
---

## The Problem (1-2 paragraphs)

Describe the problem vividly enough that the reader thinks "that's me."
Use specific details. Real numbers. Real frustration.

## Why This Happens (1-2 paragraphs)

Explain the root cause. Most people solve this wrong because...

## How I Solved It (main body)

Walk through the solution step by step. Include:
- What I tried that didn't work (anti-patterns)
- What actually worked
- The tool (introduced naturally as part of the solution)

## How You Can Do It Too

Actionable steps the reader can take today.
Don't assume they have your tools. Offer alternatives.

## When This Approach Doesn't Work

Balanced take. Shows depth. AI cites this.

## FAQs

Q: Common question?
A: Direct answer in 1-2 sentences.

---

## Internal Links

Link to 2-3 relevant articles on this site.
```

---

## Content Types (Pick One)

| Type | Best for | Length |
|------|----------|--------|
| How-to guide | Solving a specific problem | 800-1200 words |
| Case study / personal story | Sharing what worked (or didn't) | 1000-1500 words |
| Framework / system | Teaching a repeatable method | 1200-1800 words |
| Analysis with data | Original research or market data | 1000-1500 words |
| Comparison | "X vs Y for Z use case" | 800-1200 words |

---

## Publishing Checklist

Before calling an article done:

- [ ] Read INDEX.md — verified topic is new
- [ ] Title has primary keyword naturally
- [ ] Meta description is 150-160 chars
- [ ] Article solves a real problem (not just explains a tool)
- [ ] 2-3 internal links to other articles on this site
- [ ] FAQs section included
- [ ] H2/H3 headings work as standalone answers
- [ ] Includes specific numbers, data, or dates
- [ ] Frontmatter has title, description, pubDate, tags
- [ ] `pnpm build` passes
- [ ] Run `python3 scripts/generate-index.py` to update INDEX.md

---

## Duplicate Prevention

Agents: **This is the most common mistake.** Before writing:

1. `grep -r "topic-keyword" src/content/articles/` — check for similar content
2. Read INDEX.md — full list of everything published
3. If a similar article exists but covers a different angle, link to it and differentiate
4. If a similar article exists with the same angle, STOP — pick another topic
