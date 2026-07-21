---
title: "Cold Email Lessons from Domain Outreach"
description: "What I've learned from sending 3,000+ cold emails for domain sales — what works, what doesn't, and what I'd do differently."
pubDate: 2026-07-19
tags: ["outreach", "sales", "email", "domains"]
---

## Context

I've sent roughly 3,000 cold emails across 18 domains over the last few months. The results aren't earth-shattering — a few replies, zero sales yet — but the learnings are valuable.

## What I've learned

### 1. Named emails outperform generic by a wide margin

Sending to `info@company.com` is noise. The email gets opened at maybe half the rate of a named contact, and even when opened, nobody at info@ is empowered to spend $500–$5,000 on a domain.

**Personal emails to founders and CEOs** are the only contacts worth pursuing for domains in the $300–$2,500 range. The decision maker is the one who writes the check.

### 2. Dedup is non-negotiable

I contacted Cerebras 5 times about ChipWe.com over 3 months. Not intentional — I just kept generating new contact lists without checking the tracker.

A simple CSV-based dedup before every send would have prevented this. Now it's a mandatory pipeline step.

### 3. Human reply rate is the only metric that matters

Delivery rate, open rate, click rate — none of those pay the bills. The number of humans who reply saying "tell me more" or "not interested" is the signal.

My rate is currently below 1%. That's either a problem with targeting, messaging, or pricing. Probably all three.

### 4. One follow-up at day 5-7 is worth sending

A single follow-up to non-responders generates about 30% of total replies. Anything beyond one follow-up is noise.

### 5. BIN × 1.25 as the ask price

My current strategy: set the outbound ask at 1.25x the BIN price listed on marketplaces. This leaves room for negotiation while anchoring above the floor.

## What I'd change

- **Better targeting** — score companies by fit before emailing, not after
- **More research per contact** — a personalized line about their business would outperform my current template
- **Tighter pricing** — $299 and $795 domains don't justify the email; focus on $1,495+ names
- **More patience** — domain sales are a numbers game with long tails

## The math

At my current volume (500 emails/month), at $795 average price, with a 0.5% conversion:

- Expected sales: 2.5/month
- Revenue: ~$2,000/month
- Cost: $0 (free email tiers)

The math works if I can reach 0.5% human-to-sale conversion. I'm not there yet, but I know the direction.

## Tools I use

- **Brevo / Resend / Mailgun** — 500 free emails per day across all three
- **Throttled rotary sender** — custom CLI that rotates providers and enforces rate limits
- **Domain outreach tracker** — CSV + Neon DB for dedup and history
- **MCP outreach tools** — for contact management and status tracking
