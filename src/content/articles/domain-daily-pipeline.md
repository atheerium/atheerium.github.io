---
title: "Building a Daily Domain Pipeline"
description: "How I automate expired domain discovery — fetching 20,000 domains per day, filtering, scoring, and ranking in under 60 seconds."
pubDate: 2026-07-20
tags: ["domains", "automation", "pipeline", "tools"]
---

## The problem

Expired domains drop every day. Finding the good ones means:

1. Getting a fresh list
2. Filtering out noise
3. Checking availability
4. Estimating value

Do this manually and you spend 30 minutes a day on a mechanical task. Automate it and you spend 30 seconds reviewing results.

## The pipeline

My daily pipeline runs as a cron job each morning. Here's the flow:

### 1. Source data

A GitHub repository publishes ~20,000 new domain deletions daily (via WhoisFreaks data). I fetch this at 8am every day.

### 2. Static filters

Before any DNS check, I filter on:

- **.com only** — my market
- **≤ 12 characters** — longer names are harder to sell
- **English words or pronounceable** — no random letter strings
- **No hyphens or numbers** — these kill resale value

This cuts 20,000 → ~1,500 candidates.

### 3. DNS availability check

Parallel DNS lookups on all survivors. Any domain with existing NS records is taken — skip it. This is the fastest availability check available (no WHOIS throttle).

~1,500 → ~200 available domains.

### 4. Comparable sales lookup

Every surviving domain gets checked against my 19K-record sales database. Domains with comparable sales get a score bump.

### 5. Scoring and ranking

A weighted formula combines:
- Length (shorter = better)
- Dictionary value
- Commercial intent
- Comparable sales (if any)
- Keyword trend score

The output is a ranked markdown report.

## The tech stack

All CLI tools, no web UI:

- **Python stdlib** for HTTP, DNS, and text processing
- **SQLite** for the sales DB
- **Domain Sales MCP server** for comparable lookups
- **Cron** for daily scheduling

Total pipeline time: ~45 seconds for 20,000 domains.

## What I look for

After running this daily for months, my sweet spot targets are:

- **5-7 letter .com domains**
- **Clear commercial meaning** (logistics, fintech, SaaS)
- **Broad buyer pool** (not hyper-niche)
- **Aged registration** (2000s era with backlinks)
- **No trademark conflicts**

## The output format

A typical daily report:

```
## Top Picks

1. DomainX.com — 6 letters, logistics meaning, 3 comps avg $2,100
2. DomainY.com — 7 letters, fintech, aged 2001
3. DomainZ.com — 5 letters, brandable, broad buyer pool
...
```

## Why this matters

Before automation, I'd miss 80% of the good drops. Now I see them all. The pipeline doesn't replace judgment — it surfaces candidates I'd never find manually.

The code is at [domain-daily-pipeline](https://github.com/atheerium/domain-daily-pipeline) on GitHub.
