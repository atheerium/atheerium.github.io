---
title: "Your Domain Cold Emails Are Going to Spam -- Here's Why"
description: "After sending 3,000 cold emails for domain sales with a sub-1% reply rate, here's what I learned about deliverability, targeting, and getting humans to respond."
pubDate: 2026-07-21
tags: ["domains", "outreach", "sales", "email", "cold-email"]
---

I've sent roughly 3,000 cold emails across 18 domains. My human reply rate was under 1%. Most replies were auto-responses from Zendesk. The few humans who replied either had no budget or weren't the right decision-maker.

After 3,000 emails and zero sales, I stopped and asked: what's actually broken?

## The Problem: Three Layers of Failure

Cold email for domain sales fails at three levels, and they compound:

**Layer 1: Delivery.** Your email never reaches a human inbox. It bounces, lands in spam, or hits a catch-all address that auto-responds.

**Layer 2: Targeting.** The person who receives it doesn't care about domains. They're in customer support, not business development.

**Layer 3: Offer.** Even if the right person reads it, the offer isn't compelling enough to act on.

Here's how I fixed each layer.

## Layer 1: Delivery Infrastructure

Most domain investors send from personal Gmail accounts. Gmail limits you to 500 emails/day. Send more, and your account gets flagged. Send from a new domain without warmup, and everything lands in spam.

**What I changed:**

- **Use transactional email providers, not regular email.** Brevo (300/day free), Resend (100/day free), and Mailgun (100/day free). These are built for programmatic sending and have better deliverability than Gmail or Outlook.

- **Rotate between providers.** I send 20 emails through Brevo, then 20 through Resend, then 20 through Mailgun. This keeps me under per-provider rate limits and prevents any single provider from seeing a "burst" pattern that triggers spam filters.

- **Use a real sending domain.** Sending from atheerium.com (or whatever domain you own with proper SPF, DKIM, and DMARC records) is better than sending from a personal Gmail.

- **Warm up new domains.** If you're using a fresh domain for sending, send 5-10 emails/day for the first week before ramping up.

**The result:** Almost no bounces. Delivery rate went from ~70% to ~95%.

## Layer 2: Getting to the Right Person

This was the bigger problem. I was sending to info@company.com and contact@company.com. Those go to ticket systems, not decision-makers.

**What I changed:**

- **Only named individuals.** Founders, CEOs, CTOs, and heads of business development. If I can't find a name, I don't send.

- **Use LinkedIn and company "about" pages** to find the right person. Most startups list their team. Most founders have a LinkedIn profile with their email or a "contact" button.

- **Verify emails before sending.** I use a combination of hunter.io and manual pattern detection (firstname@company.com, firstinitiallastname@company.com). Testing a few patterns against known-good emails helps.

**The test:** If you can't find the name of the person who makes decisions about technology or branding at a company, you're not ready to email them.

## Layer 3: The Offer

Even with perfect delivery and the right person, the offer needs to work.

**What I changed:**

- **Price at BIN x 1.25, not BIN x 3.** The outbound ask should be slightly above the buy-it-now price, not 3x. You're starting a negotiation, not making a demand.

- **Lead with the problem, not the domain.** "I see you're in logistics. We have FedZip.com -- it's a 6-letter .com brand for shipping platforms." This is still weak. Better: "I noticed your current domain is hard to spell over the phone. We have FedZip.com -- it's shorter and clearer."

- **One follow-up on day 5-7, then stop.** Most people who reply do so within the first week. If they don't reply to the first email or the follow-up, they're not going to buy.

- **Track everything.** Keep a list of who you contacted, when, and what they said. Never email the same company twice about the same domain. It looks desperate.

## How You Can Do It Too

1. Set up accounts on Brevo, Resend, and Mailgun (all free tiers)
2. Configure SPF and DKIM for your sending domain
3. Build a list of 50 named decision-makers for your best domain -- not your fifth-best, your absolute best
4. Write a personalized email that mentions something specific about their company
5. Send 25 emails through provider A, 25 through provider B
6. Wait 5-7 days
7. Send one follow-up to non-responders
8. After 30 days with zero human replies, move the domain to auction

## When This Doesn't Work

Some domains have no natural buyer. No amount of email infrastructure will sell a domain nobody wants. The cold email fix only helps if the underlying asset has demand.

Also, avoid industries that use aggressive email filters -- law firms, government agencies, and large enterprises (1000+ employees) often have systems that block cold email entirely.

## FAQs

### Q: How do I find email addresses for decision-makers?
A: Hunter.io, Apollo.io, or manual pattern testing. For startups, check their "team" or "about" page. For larger companies, LinkedIn Sales Navigator.

### Q: What if the company uses a ticket system?
A: If you're emailing info@ or contact@, you're hitting a ticket system. Named individual emails (firstname@company.com) bypass most of these.

### Q: Is cold email worth it for domain sales?
A: With a sub-1% reply rate, no -- unless you can improve delivery and targeting. My reply rate improved to ~5% after fixing delivery and targeting named individuals. At that rate, 100 emails = 5 conversations. One of those might buy.

### Q: Should I mention the price in the first email?
A: No. Start the conversation. Mention the domain, why it fits their business, and ask if they're open to discussing it.

---

*Related: [Cold Email Lessons from Domain Outreach](/articles/cold-email-lessons/) -- the earlier lessons that taught me what was broken. [Selling Domains: 12 Months of Lessons](/articles/selling-domains-lessons/) -- the full scoreboard.*
