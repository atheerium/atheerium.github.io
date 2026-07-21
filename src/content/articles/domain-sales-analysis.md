---
title: "How I Analyze Domain Sales Data"
description: "My process for tracking and analyzing domain sales -- from data collection to identifying patterns that inform acquisition and pricing decisions."
pubDate: 2026-07-21
tags: ["domains", "data", "analysis", "methodology"]
---

## Why track domain sales

Domain valuation is subjective until you ground it in data. I maintain a database of 19,000+ domain sales records to:

- **Price my portfolio** — comparable sales tell me what buyers actually pay, not what sellers hope for.
- **Identify trends** — which prefixes, suffixes, and keywords command premiums.
- **Avoid overpaying** — at auction, knowing the comp range keeps bidding disciplined.

## My data sources

| Source | Records | Coverage |
|--------|---------|----------|
| NameBio | ~11,000 | 2015–2026 |
| NamePros | 893 | 1997–2026 |
| DNJournal | ~400 | 2002–2023 |
| TLDI | ~100 | 2020–2025 |
| Dynadot | ~160 | 2024–2025 |

The combined database sits at just over 19,000 unique domains. Not NameBio-scale, but enough for meaningful comparisons on short brandables and common patterns.

## How I use it

### Comparable sales lookups

When evaluating a domain, I check:

1. **Same keyword pattern** — e.g., `[Word]Hub.com`, `Get[Word].com`
2. **Same TLD** — .com comps are most relevant
3. **Similar length** — 5-7 letter brandables cluster in certain price bands
4. **Recency** — last 12 months preferred

A single comp is interesting. Three+ comps in a narrow price range is actionable.

### What the data tells me

Consistent findings from 19K+ records:

- **5-6 letter .com brandables**: $2K–$8K range, higher with trending keywords
- **Geo + service domains**: $1K–$5K, slower to sell
- **Hyphenated domains**: significant discount vs unhyphenated
- **Non-.com TLDs**: .ai and .io hold value; others are thin

## Practical example

I recently evaluated **ChipWe.com**. Comparable sales for `[Word]We.com`:

- NameWe.com — $2,188
- GameWe.com — $2,250
- DealWe.com — $1,988

Three data points within $300 of each other. That's a reliable band. Without the database, I'd be guessing.

## Tools I use

- **Domain Sales DB** — my own SQLite/MCP database with 19K+ records
- **NameBio** — public API for additional lookups
- **GoDaddy Auctions** — real-time market data via their API

## Bottom line

19,000 records is enough to spot patterns, not enough to be authoritative on niche domains. I'm adding 200–500 records per month. Over time, the database becomes the most valuable asset in my toolkit — more useful than any single domain in the portfolio.

---

*Related:* [NameBio Workflow: Finding Comparable Domain Sales](/articles/namebio-workflow/), [The Daily Domain Pipeline: How I Process 20,000 Expired Domains in 45 Seconds](/articles/expired-domains-pipeline/), [Your Domain Portfolio Is Too Big -- How to Focus and Actually Sell Something](/articles/portfolio-too-big/), [How I Evaluate .com Domains: The 3-Criteria Framework](/articles/evaluate-dot-com-domains/)
