---
title: "NameBio Workflow: Finding Comparable Domain Sales"
description: "How I use a 19,000-record domain sales database to price domains and spot market patterns."
pubDate: 2026-07-21
tags: ["domains", "namebio", "data", "pricing", "research"]
---

Comparable sales are the closest thing domain investing has to a pricing floor. If similar domains have sold for $X, your domain is worth roughly $X -- not $10X because "it's a great name."

I maintain a database of 19,000+ domain sales records aggregated from NameBio, DNJournal, NamePros, and other sources. Here's how I use it.

## The Database

The data lives in a SQLite file (~/dev/domain_sales_full.db) with a single unified schema:

- Domain name
- Sale price
- Sale date
- Venue (NameBio, DNJournal, NamePros, etc.)
- TLD

19,111 unique domains spanning 1997-2026. The MCP server at ~/dev/domain-sales-mcp exposes it as searchable tools that any agent can query.

## How I Search

When evaluating a domain, I run three queries:

**1. Exact category match.** Find domains with the same keyword sold in the last 12 months. If I'm pricing OilHeal.com, I search for "oil," "heal," "wellness," "health" keyword domains.

**2. Pattern match.** Same prefix or suffix structure. "Feed" + noun, "go" + verb, "get" + noun. These patterns have consistent price ranges regardless of the specific word.

**3. Length and structure.** 5-7 letter .com domains with English words vs made-up brandables. The market prices them differently.

## What the Data Shows

After analyzing 19,000 records, a few patterns stand out:

**Short domains (4-5 letters) command a premium.** Average sale price is 2-3x longer domains, but volume is lower because fewer exist.

**Category matters more than the word.** A 6-letter .com in the AI space sells for more than a 5-letter .com in a dead category. Recent sales of AI-related domains show consistent $500-$2,000 pricing regardless of length.

**The "refresh effect" is real.** Domains in trendy categories (crypto 2021, AI 2024-2026) see a price bump that lasts 12-18 months before settling. Catching a category early matters more than the name quality.

## My Confidence Framework

| Signal | Confidence | Action |
|--------|-----------|--------|
| 3+ comps in 12 months, same keyword | Strong | Price confidently, list at BIN |
| 1-2 comps in 12 months | Moderate | Price cautiously, test market |
| Similar keyword comps only | Weak | Add margin for uncertainty |
| No comps at all | None | Skip or auction |

## How I Pull Data

I have an MCP tool call for this, but the manual method is just as good:

1. Go to NameBio.com
2. Search for your keyword
3. Filter by TLD (.com)
4. Filter by date (last 12 months)
5. Sort by relevance, scan the prices

The key is not to cherry-pick. If the top result is $5,000 but the next 10 are $200-$400, the $5,000 is an outlier. Average the cluster, not the spike.

## Why This Matters

Without comparable sales, domain pricing is guessing. With a database, it's research. The confidence level is transparent -- "3 strong comps at $400-$600" is a statement you can defend. "I think it's worth $2,000" is a feeling.

I update the database monthly with new sales. Patterns shift, categories cool down, new ones heat up. The data keeps my pricing grounded.
