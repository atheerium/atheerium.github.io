---
title: "The Daily Domain Pipeline: How I Process 20,000 Expired Domains in 45 Seconds"
description: "Automated expired domain discovery -- fetching, filtering, DNS-checking, scoring, and ranking at scale."
pubDate: 2026-07-21
tags: ["domains", "automation", "pipeline", "expired-domains", "tools"]
---

Every morning at 8 AM, a cron job runs on my machine that processes ~20,000 expired domains, checks which ones are still available, scores them, and outputs a ranked report. It takes 45 seconds. Here's how it works.

## The Source

The pipeline fetches from WhoisFreaks' GitHub feed, which publishes ~20,000 expiring domains daily. These are domains that are about to drop or have just been deleted. The feed updates every 24 hours.

Alternative sources I use for manual triage:
- **ExpiredDomains.net** -- when I want to paste a specific list
- **Freshdrop** -- for recently dropped domains

## The Pipeline

The code lives at ~/dev/domain-daily-pipeline/ and runs in 5 stages:

### Stage 1: Fetch (5 seconds)

Download the daily feed from WhoisFreaks. Raw data: 20,000+ domains with basic metrics (length, score, age, backlinks).

### Stage 2: Static Filters (2 seconds)

Keep only domains that pass:
- **TLD: .com** only (everything else goes straight to discard)
- **Length: ≤12 characters**
- **No hyphens or numbers** (pure alpha)
- **English words** (basic dictionary check)
- **Pronounceable** (CVCV pattern check for short domains)

This typically cuts the list from 20,000 to ~300-500 candidates.

### Stage 3: DNS Check (20 seconds)

For each candidate, run a DNS lookup to see if it's registered or available. Registered = still taken (someone renewed). Available = ready to backorder or register. Use `host -t NS` for speed (fast, parallel).

### Stage 4: Comparable Sales (10 seconds)

Cross-reference against the 19,000-record domain sales database. Check if any of the candidates or similar names have sold before. This identifies domains with proven market demand.

### Stage 5: Scoring and Ranking (5 seconds)

Each candidate gets scored on:
- **Pronounceability** (0-10)
- **Commercial intent** (0-10) -- does it sound like a business name?
- **Buyer pool size** (0-10) -- how many companies could use it?
- **Comparable sales** (0-10) -- has similar sold?
- **Length bonus** (0-5) -- shorter = better

Total out of 45 points, normalized to 0-10. Only domains scoring 8.0+ make it to the final report.

## The Output

The pipeline writes a markdown report to cache/reports/YYYY-MM-DD.md with:
- Top 15 ranked domains with scores and reasoning
- DNS availability status
- Comparable sales data (if found)
- Estimated price range and recommendation

## Why 45 Seconds Matters

Domains drop from the registry throughout the day. When a good one drops, someone else can backorder it within minutes. Speed determines whether you catch it or someone else does. I don't waste time on Wayback Machine history or deep research -- if it's 8.0+ and available, I decide in seconds.

## Going Deeper

All of this is automated via a Hermes cron job. The skill at domain-flipping/domain-daily-pipeline has the full deployment details.

The same pipeline accepts custom input files. If I find a list on ExpiredDomains.net that looks promising, I can paste it directly: `daily-domains --input-file my-list.txt`.

## Future Improvements

- Add GoDaddy API integration for instant backordering
- Expand to .io and .ai TLDs (growing markets)
- Auto-categorize domains by buyer type (fintech, health, logistics)
