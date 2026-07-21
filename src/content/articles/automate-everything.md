---
title: "I Automate Everything That Doesn't Need Human Judgment -- Here's What That Looks Like"
description: "Cold email sending, domain appraisal, content posting, delivery price calculation. If a human doesn't need to think about it, a script should be doing it."
pubDate: 2026-07-21
tags: ["automation", "business", "domains", "freelancing", "productivity"]
---

I run three lines of work: domain investing, freelance web development, and an e-commerce business. None of these are "passive." But I've automated enough of them that I spend my time on decisions, not execution.

Here's the philosophy: if a task takes less than 30 seconds of human thinking, it should be automated. Not because I'm lazy, but because every minute spent on predictable work is a minute I'm not selling, creating, or improving.

## What I Automate and How

**Domain appraisals.** I used to check each domain manually: DNS, Wayback, NameBio. 5 minutes per domain. I processed 20 domains a day. That's 100 minutes. Now my daily pipeline script checks DNS, scores domains, looks up comparable sales, and ranks them. I review the output in 5 minutes.

**Cold email sending.** Writing and sending 50 personalized emails used to take 2 hours. Now I have templates per domain with variable fields, a contact dedup system, and a rotary sender that rotates between email providers. I spend 10 minutes verifying the contact list, the script sends over an hour.

**Content posting.** I used to copy-paste between Twitter, Bluesky, and Dev.to. Now OmniPost generates content, posts on schedule, and cross-platforms automatically. I review the queue once a day.

**Delivery price calculation.** Every time we quoted a delivery price, someone had to look it up. Now it's calculated instantly from a lookup table. 30 seconds per order saved, 30+ orders a day, that's 15 minutes daily.

## The Automation Decision Tree

Before I automate anything, I ask three questions:

**1. Does this task require human judgment?** A cold email template doesn't. Reading a reply does. Appraising a domain doesn't (I've encoded the criteria). Deciding whether to register it does.

**2. How much time does it consume weekly?** Less than 30 minutes? Don't automate. More than 2 hours? Automate immediately. In between? Calculate the setup time and build the automations with the highest ROI first.

**3. Will the automation break often?** If the data source changes weekly, the automation will need constant maintenance. That's not automation, that's a second job. Only automate things that stay stable.

## What NOT to Automate

Some things I deliberately keep manual:

- **Client conversations.** Automated outreach is fine. Once a human replies, the conversation is human-only.
- **Portfolio decisions.** Which domain to buy, which project to take, which wilaya to expand to. These are judgment calls that should consider factors no script can capture.
- **Strategy adjustments.** What's working this month? What changed? Automation handles execution. Strategy is a human function.
- **Content ideas.** I generate content concepts manually. The writing and posting can be automated, but the "what should I write about" question is human.

## The Tools

Here's my actual automation stack:

- **Cron jobs** (Hermes cron): Schedules all recurring tasks. Daily pipeline at 8 AM, content posting hourly, database backup at 3 AM.
- **Python scripts**: Heavy lifting. Domain appraisal, email sending, contact management, data analysis.
- **MCP servers**: API access for agents. Domain sales DB, email infrastructure, GitHub.
- **Google Sheets API**: Connects the e-commerce team's operational data to my automation layer.
- **GitHub Actions**: Deploys the site, runs scheduled exports, validates data.

All free-tier. All glue code I wrote in an afternoon each.

## How You Can Do It Too

**Start with one 30-minute task you hate.** Not the most important task, the one you dread doing. The one you put off.

For me, it was checking domain availability. I hated opening 5 tabs per domain. I automated that first. The momentum from that one automation made me look for the next one.

**Write the script, don't buy the tool.** Most "automation platforms" (Zapier, Make) cost money and have limits. A Python script costs $0, runs on your machine, and does exactly what you need.

**Set it and monitor it.** Every automation breaks eventually. Set up monitoring (I use cron notification) so you know when it fails.

*Related: [Automation 200 Lines](/articles/automation-200-lines/)*

##s

### Q: How much time do automations actually save me?
A: About 10-15 hours per week across all three businesses. But the bigger benefit is consistency -- the automation never forgets, never procrastinates, never makes typos.

### Q: What's the most valuable automation I've built?
A: The domain daily pipeline. It processes 20,000 domains, filters to the top 5, and presents them to me in 45 seconds. Finding one good domain pays for a year of automation maintenance.

### Q: Do I need to know how to code?
A: Yes, for custom automations. But AI coding agents can build them with guidance. Describe what you want, review the code, test it.

### Q: What's the biggest automation mistake?
A: Automating something that's broken. If the manual process is wrong, automation makes it faster to produce wrong results. Fix the process first, then automate.

---

*Related: [How I Use AI Agents as My Coding Partner](/articles/ai-agents-coding-partner/) -- the agent layer above automation. [Building OmniPost](/articles/building-omnipost/) -- a specific automation in detail.*
