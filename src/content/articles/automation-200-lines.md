---
title: "I Automated Half My Business With 200 Lines of Python -- Here's What I Learned"
description: "Most people think automation means complex systems. My most impactful automation is a 200-line Python script that runs daily and saves me 5 hours a week."
pubDate: 2026-07-21
tags: ["automation", "python", "business", "productivity", "beginner"]
---

The most valuable automation I've built is a 200-line Python script called `domain-daily-pipeline`. It checks 20,000 expired domains, filters them by quality, appraises the top candidates, and emails me a report.

It takes 45 seconds to run. It runs automatically every morning at 8 AM. It saves me about 5 hours of manual checking per week.

The code isn't clever. It doesn't use AI or machine learning. It's simple: fetch a list, check each domain against filters, score the survivors, rank them, output the result. That's it.

## The Problem: Automation Feels Like Engineering

Most people think automation requires:
- Complex infrastructure (Docker, Kubernetes, cloud deployments)
- Expensive tools (Zapier, Make, n8n)
- Deep technical knowledge (APIs, microservices, webhooks)

The reality: most useful automations are simple scripts that:
- Read a file
- Process each line
- Write the result somewhere
- Run on a schedule

That's it. 50-200 lines of code, a cron job, and you've eliminated a weekly chore.

## What My 200-Line Script Does

1. Fetches expired domain list from a GitHub repo (WhoisFreaks, 20K domains)
2. Filters by: .com only, no hyphens/numbers, 12 chars max, English words
3. Checks DNS (fast, 20-30 at a time)
4. Scores each domain using the 3-criteria framework
5. Ranks by score
6. Writes a markdown report
7. Saves to cache

That's it. No database, no API calls to paid services, no machine learning. Just a for loop and some if statements.

The hardest part was the first hour: fetching the domain list and parsing it. Everything else was adding one filter at a time.

## The Second Best Script: Email Deduplication

Another 100-line script: checks a list of companies against my outreach tracker (3,600+ records) and removes duplicates before sending.

Before I wrote this, I emailed the same company 5 times about the same domain because I didn't remember contacting them. After, I can't accidentally duplicate because the script checks and blocks it.

This script doesn't look impressive. It reads a CSV, compares columns, writes a filtered CSV. But it saved me from looking unprofessional to dozens of companies.

## How You Can Do It Too

**Pick one task you do that's:**
- Repetitive (same steps every time)
- Rule-based (no judgment required)
- Takes 15+ minutes per week

**Write a script that:**
1. Reads input (file, API, clipboard)
2. Does the processing (filters, calculations, lookups)
3. Writes output (file, email, notification)

**Schedule it:**
- `crontab -e`
- `0 8 * * * /usr/bin/python3 /home/you/scripts/daily-task.py`

**For non-technical people:** Describe your manual process to an AI agent and ask it to write the script. You don't need to be a developer to automate your workflow.

## When This Doesn't Work

If your task involves human judgment (deciding which client to call first, which domain name is better), a script can't replace you. Use it to prepare data, not make decisions.

If the data source changes format every month, the script will break constantly. Only automate stable inputs.

*Related: [Build Your Own Tools](/articles/build-your-own-tools/)*

##s

### Q: What's the easiest first automation?
A: A daily email report. Fetch data from a source, format it, send it to yourself. One less thing to remember.

### Q: Do I need to know Python?
A: Python is the easiest for this kind of thing. But bash scripts work too. Pick what you know.

### Q: How do I make sure the script doesn't crash silently?
A: Add notifications. Cron sends errors by email by default. Or have the script send a Telegram message when it finishes.

### Q: What's the best automation you haven't built yet?
A: Automated invoice reconciliation. Still manual, still painful, still on the list.

---

*Related: [I Automate Everything That Doesn't Need Judgment](/articles/automate-everything/) -- the broader automation philosophy. [Building OmniPost](/articles/building-omnipost/) -- a more complex automation example.*
