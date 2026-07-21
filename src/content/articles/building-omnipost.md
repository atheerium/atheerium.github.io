---
title: "Building OmniPost: A Multi-Platform Content Bot"
description: "How I built an automated bot that posts to Twitter, Bluesky, and Dev.to from a single content pipeline."
pubDate: 2026-07-21
tags: ["projects", "automation", "bots", "twitter", "bluesky"]
---

I run a content bot called OmniPost that posts to Twitter/X, Bluesky, and Dev.to every hour from 6 AM to 11 PM. It's fully automated, costs nothing to run, and took about 3 days to build. Here's how it works.

## The Problem

I wanted a consistent online presence without spending time on social media. Posting the same content to multiple platforms manually is tedious. Each platform has a different API, different rate limits, and different content formats.

## Architecture

OmniPost is a Python project at ~/dev/omnipost with a simple pipeline:

```
Content generation (GROQ API)
  → Twitter (Cloak Browser)
  → Bluesky (atproto/API)
  → Dev.to (REST API)
  → Cron (every hour)
```

Each platform is a separate module in bot/platforms/. The core loop in post.py generates content once, then dispatches to all platforms.

## Twitter (The Hard Part)

Twitter's API is expensive and restrictive for automation. The free tier won't let you post programmatically, and even the paid API has tight limits. So I went browser-based.

I use **Cloak Browser** (a Python headless browser with anti-detection) to post tweets through the actual Twitter web interface. It handles:
- Login with session persistence
- Post composition via Draft.js keyboard input
- Rate limiting (one post per hour per account)
- Retry logic on failures

The tricky part was Draft.js -- Twitter's editor doesn't accept standard input. I had to use page.keyboard.type() with humanize=False, then wait for the post button to become active.

```python
# Simplified version of the Twitter poster
page.goto("https://twitter.com/compose/tweet")
page.keyboard.type(content, delay=10)
page.click('[data-testid="tweetButton"]')
```

## Bluesky (The Easy Part)

Bluesky has a clean AT Protocol that works immediately. The official atproto Python library handles auth and posting in a few lines. No browser needed, no anti-detection, no rate limit headaches.

```python
from atproto import Client

client = Client()
client.login(handle, app_password)
client.send_post(text)
```

## Dev.to (Also Easy)

Dev.to has a REST API with a simple endpoint. One POST request with the article content in markdown, and it publishes. Auto-detects tags from content keywords.

## Content Pipeline

Content is generated using GROQ's API (free tier) with strict prompts:
- 280 characters max (Twitter limit)
- No first-person pronouns
- Must include a real source URL
- Simple English, factual, no AI-isms
- Topics limited to: AI, agents, SaaS, programming, domains, IT

Each hour produces 2 tweets + 1 bluesky post with the same text. Once per day at 12:00, a full Dev.to article goes out.

## Cost

Zero. GROQ has a generous free tier. Cloak Browser is open-source. The bot runs on my Linux machine via Hermes cron jobs. No API subscriptions, no server costs.

## Lessons

1. **Browser automation breaks constantly.** Twitter changes their DOM every few weeks. I've had to update selectors 4 times. Using data-testid attributes helps.
2. **Rate limits are the real bottleneck.** Not technical limits -- platform policies. Going too fast triggers spam detection. One post per hour is sustainable.
3. **Content quality matters more than volume.** The bot posts hourly, but I curate the prompts carefully. Generic AI content gets ignored. Specific facts and numbers get engagement.

The full source is available on my GitHub.

---

*Related:* [Building a Daily Domain Pipeline](/articles/domain-daily-pipeline/), [How I Use Twitter as a Business Tool (Not a Distraction)](/articles/twitter-business-tool/), [How I Use AI Agents as My Coding Partner (Not Just a Chatbot)](/articles/ai-agents-coding-partner/), [How I Use GitHub to Run My Entire Business (For Free)](/articles/github-for-business/)
