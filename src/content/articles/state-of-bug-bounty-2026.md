---
title: "The State of Bug Bounty in 2026: AI Agents Are Finding Everything and Breaking Everything"
description: "AI agents found 34 vulnerabilities in TON in 3 days, 22 in Firefox in 2 weeks. Programs are drowning in reports. Here's what's happening and who's actually getting paid."
pubDate: 2026-07-22
tags: ["security", "bug-bounty", "ai", "agents", "hackerone", "claude-code", "automation", "review"]
draft: false
---

If you follow bug bounty in 2026, you've seen two completely opposite stories. One says AI agents are finding vulnerabilities faster than humans can patch them. The other says bug bounty is drowning in AI-generated slop and programs are shutting down.

Both are true.

This is the state of bug bounty in mid-2026. The real question you asked — is anyone actually getting paid? — has a concrete answer.

## The Flood by the Numbers

HackerOne reported a **76% jump in submissions** year-over-year through March 2026. The share of reports flagging real vulnerabilities held at 25%. That means the 76% increase is almost entirely noise.

Bugcrowd's inbox swelled more than fourfold during a three-week stretch in March. Most of what came in was unusable.

Before AI tools, a popular open-source project might get two or three bug reports in a week. Now some projects get hundreds at a time, and the majority cite non-existent code paths, imaginary patches, or vague theoretical attacks.

## Programs That Shut Down or Paused

| Project / Platform | Action | Date | Reason |
|---|---|---|---|
| HackerOne (Internet Bug Bounty) | Paused submissions | March 27, 2026 | Discovery outpacing remediation |
| Curl | Killed bounty payments | January 31, 2026 | <5% legitimate reports |
| Google | Raised quality bar for AI reports | May 2026 | Quality threshold not met |
| Node.js | Paused bug bounty | April 2026 | Lost HackerOne funding |
| Django | Modified submission process | Q1 2026 | Overwhelming volunteer team |
| Nextcloud | Shut down bounty program | April 2026 | Unsustainable workload |

Curl's Daniel Stenberg was blunt: fewer than 5% of submitted reports in 2025 were legitimate. His updated security.txt now reads: "We will ban you and ridicule you in public if you waste our time on crap reports."

Curl returned to HackerOne without monetary rewards. By April, Stenberg said the slop situation was no longer a problem — the confirmed vulnerability rate was back above 15%. Removing the financial incentive worked for Curl.

## Linus Torvalds on AI Bug Reports

"If you found a bug using AI tools, the chances are somebody else found it too."

The Linux kernel's security mailing list is now "almost entirely unmanageable, with enormous duplication due to different people finding the same things with the same tools."

A dozen independent researchers each feed the same Linux kernel source into Claude or GPT, find the same buffer overflow, and each submit a separate report. The maintainers receive twelve versions of the same finding, each padded with AI-generated analysis that needs to be triaged individually.

## The Other Side: AI Is Also Finding Real Zero-Days

CVE disclosures in 2026 tell the other story:

| Product | CVE Disclosure Change (YoY 2026) |
|---|---|
| Chrome | **+563.2%** |
| GitHub products | **+476.1%** |
| VMware | **+180.9%** |
| Apache | **+170.3%** |
| Mozilla Firefox | **+156.9%** |
| HPE | **+132.3%** |
| F5 | **+113.8%** |
| Palo Alto Networks | **+37.0%** |

These are real. Chrome's CVE disclosures are up 563%. Mozilla confirmed it's now using frontier AI models internally to find and fix latent browser vulnerabilities.

Anthropic's Project Glasswing (April 2026) made Claude Mythos available to AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks specifically for defensive vulnerability hunting. Anthropic stated Mythos "identified thousands of zero-day vulnerabilities across every major operating system and web browser."

## Did Anyone Actually Get Paid Using AI Agents?

Yes. Multiple verified cases.

### Case 1: Claude Code + TON Blockchain (March 2026)

Researcher "Masa" used Claude Code (Opus 4.6) as his primary tool for TON Blockchain's consensus bug bounty challenge. **Result: 34 vulnerabilities discovered, 6 dynamically confirmed, 3 ASAN-verified memory safety crashes — in under 3 days. 24 out of 25 commits were co-authored with Claude Code.**

The bugs included a systemic root cause connecting 7+ distinct vulnerabilities — coroutine rollback failures in the Simplex BFT consensus implementation. Claude Code traced the liveness failure through to DeFi protocols on TON, calculating potential cascade losses of $4-10M from oracle staleness and liquidation failures. Each vulnerability got a structured report: root cause, trigger condition, reproduction steps, impact assessment, and suggested fix.

15 submission-ready Telegram reports. TON paid bounty rewards for confirmed findings.

### Case 2: Claude + Mozilla Firefox (March 2026)

Anthropic and Mozilla announced a two-week security collaboration. Claude Opus 4.6 scanned 6,000 C++ files across Firefox's codebase. **Result: 22 genuine vulnerabilities found, 14 classified as high-severity by Mozilla's security team.** That's nearly one-fifth of all high-severity Firefox vulnerabilities remediated across the entire previous year.

Claude submitted 112 reports with a ~20% signal rate — substantially higher than typical automated scanning tools. Mozilla confirmed and patched. Mozilla paid.

### Case 3: Claude Code + TON Blockchain (Developer Report, March 2026)

Another developer wrote: "I found 34 vulnerabilities in TON Blockchain's consensus algorithm — Claude Code did 95% of the work." The researcher verified findings with ASAN/UBSAN builds. Claude Code built a Byzantine fault injection test matrix showing that a 10% database failure rate causes complete network halt — zero blocks produced.

The developer's key insight: "Claude Code didn't just grep for memcpy. It understood the entire consensus protocol flow — leader election, vote aggregation, certificate creation, block acceptance — and identified architectural flaws, not just surface bugs."

### Case 4: Researchers Hacked Claude, Gemini, and Copilot (April 2026)

Security researchers demonstrated full secret exfiltration from all three AI coding agents via prompt injection. They reported through official channels. **All three companies (Anthropic, Google, Microsoft) paid bug bounties.** None issued CVEs. None notified users.

The vulnerability is architectural — you cannot train a model to reliably distinguish trusted from untrusted instructions when both arrive as natural language text. The companies know this. That's why they paid the bounties without issuing fixes.

### Case 5: AI-Assisted Hunters Earning $50K+ Monthly

Multiple reports confirm bug bounty hunters using Claude, Grok, and GPT are earning $50K+ monthly on HackerOne and Bugcrowd. The workflow combines Burp Suite + MCP integration, JS analysis, recon automation, payload iteration, and AI-powered report writing.

A HackerOne survey found that researchers using AI-assisted tools submitted **28% more valid reports per month than non-users**, with severity distributions skewing higher. The best performers use AI as a force multiplier, not a replacement.

## The Open-Source Tooling Explosion

Several open-source bug bounty frameworks for AI agents launched in 2026:

- **BugHunter** (June 2026) — Full bug bounty hunting toolkit built on Claude Code, now supporting Ollama and Groq. Automates vulnerability discovery and reporting pipeline.
- **Pentest Agent Suite** (May 2026) — 50 specialized security agents, 26 slash commands, 19 CLI tools, cross-IDE installer across 7 AI coding platforms.
- **bountyforge** — Smart contract audit skill for Claude Code. Parallelized agents for EVM, Move, Solana, TRON; submission-ready reports for HackerOne, Bugcrowd, Intigriti, Immunefi.
- **claude-bug-bounty** — Recon, 20 vulnerability classes, autonomous hunting, report generation. All inside Claude Code.

## The Takeaway

Bug bounty in 2026 is a tale of two realities.

The low end: AI slop has made bug bounty **harder** for small projects. Curl, Django, and Nextcloud all shut down or paused because maintainers couldn't process the flood. If you're running a small open-source project, AI-generated reports are a net negative.

The high end: AI agents have made vulnerability discovery **dramatically more effective** for researchers who know what they're doing. 34 bugs in TON in 3 days. 22 high-severity Firefox bugs in 2 weeks. $50K+ monthly earners. These are real.

The pattern that works: **human + AI, not AI alone.** The TON researcher didn't just run Claude Code unattended. He pointed it at the right targets, asked the right questions, verified with ASAN/UBSAN, and compiled submission-ready reports. The HackerOne survey confirms this: AI-assisted researchers produce more valid reports with higher severity, but they're still researchers — they just have a better tool.

If you want to use AI agents for bug bounty:
- **Target programs with infrastructure to handle AI reports** (HackerOne's larger programs, dedicated bug bounty challenges like TON's)
- **Verify every finding** — AI hallucinates bugs in non-existent code paths
- **Expect duplicates** — everyone is feeding the same code to the same models
- **Focus on complex logic flaws** — surface-level bugs (buffer overflows, XSS) are saturated; architectural bugs (coroutine rollback, state machine flaws) are where AI adds the most value

The window where AI-assisted bug hunting is profitable is open. It won't stay that way.
