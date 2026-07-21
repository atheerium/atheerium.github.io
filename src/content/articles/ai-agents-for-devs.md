---
title: "AI Agents for Developers: What I Actually Use"
description: "My daily workflow with AI coding agents, MCP servers, and automation tools -- including what works and what doesn't."
pubDate: 2026-07-21
tags: ["ai", "agents", "mcp", "automation", "development"]
---

I use AI agents as my primary coding partner. Not for generating boilerplate -- for actual architecture, implementation, and debugging. Here's what my stack looks like and why I chose each piece.

## The Stack

**Hermes Agent** (Nous Research) -- The orchestrator. Handles research, planning, tool orchestration, and delegation. It's the "architect" that understands the full system and decides what to build next.

**OpenCode + Omo** -- My primary coding agent. Takes specs from Hermes and implements them. Handles the actual file writing, testing, and refactoring.

**Claude Code** -- Fallback for specific tasks where Claude's reasoning is better.

**Flow:** Discuss → Hermes architects → Hermes writes spec → Delegates to OpenCode → OpenCode implements → Hermes verifies.

## MCP Servers (The Game Changer)

MCP (Model Context Protocol) is what makes agents actually useful beyond chat. It lets agents interact with real tools and data. I run several MCP servers:

**Domain OS** -- A unified interface for the domain investing toolkit. Agents can appraise domains, check trademarks, find comparable sales, manage my portfolio, and even send cold emails. All through MCP tool calls instead of me running CLI commands.

**Domain Sales DB** -- A 19,000-record sales database queryable via MCP. Agents search for comps during appraisal without me switching contexts.

**Blog MCP Server** -- Writes articles to my GitHub Pages blog by creating markdown files, committing, and pushing. I tell the agent "publish this," it handles the entire pipeline.

## What I've Learned

**1. Agents are best at implementation, not requirements.**

I've stopped asking agents "what should I build?" They're bad at that. I define the goal, they figure out the code.

**2. Specs are better than prompts.**

When I need something built, I write a brief spec (BLUEPRINT.md) with the architecture, data flow, and constraints. The agent implements from the spec. This produces far better results than conversational back-and-forth.

**3. MCP replaces API documentation.**

Instead of reading API docs, I configure an MCP server and let the agent call it directly. The agent discovers the tools available and uses them. This is faster and more reliable than implementing API calls from documentation.

**4. Free tier is enough.**

All my AI usage is on free tiers: DeepSeek, GROQ for content generation, Gemini for classification. The paid models (Claude, GPT-4) are better for some tasks but not 10x better. For 80% of coding work, free models suffice.

## The Gap

The biggest missing piece is reliable agent-to-agent communication. MCP solves tool access, but there's no standard way for agents to hand off context. I've hacked around this with spec documents and shared files, but it's fragile.

The second gap is agent memory. Every session starts fresh. I've mitigated this with AGENTS.md, STATE.md, and TASKS.md files in each repo that give agents instant context, but it's a workaround, not a solution.

## Why This Matters for Developers

The AI agent stack is where Rails was in 2005 -- powerful but unopinionated. The developers who figure out workflows and tooling now will have a massive advantage in 2 years.

My advice: pick one orchestrator agent, one coding agent, and build MCP servers for your most common tools. The setup cost is real (~2 days per MCP server), but the leverage compounds every week.
