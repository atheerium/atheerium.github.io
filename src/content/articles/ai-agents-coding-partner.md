---
title: "How I Use AI Agents as My Coding Partner (Not Just a Chatbot)"
description: "Most developers use ChatGPT to generate code snippets. I use AI agents to architect, implement, and ship entire features. Here's the exact workflow."
pubDate: 2026-07-21
tags: ["ai", "agents", "development", "workflow", "automation"]
---

There are two ways to use AI for coding:

1. Ask ChatGPT to write a function, copy-paste it, fix the inevitable bugs, repeat
2. Treat AI agents as engineering partners who handle architecture, implementation, and testing

I started with #1. It saved me 20% of my time. I switched to #2. It doubled my output.

## The Problem: Chatbots Are Not Engineering Partners

ChatGPT and Claude in chatbot mode are great for answering questions and generating snippets. But they lack context, forget what you discussed, and can't execute anything.

A typical session looks like:

1. "Write a Python function to parse this CSV" → works
2. "Now add error handling" → writes it, but conflicts with the first version
3. "Can you also add logging?" → adds it, but the structure is getting messy
4. "Actually, can we refactor this into a class?" → generates a completely different structure

Each request is isolated. The bot doesn't remember the architecture decisions from step 1. You become the integrator, stitching together outputs and fixing inconsistencies.

## How I Fixed It: Agent-Based Development

I shifted to a workflow where AI agents own entire features, not just functions. Here's the stack and the process.

**The stack:**
- **Hermes Agent** — orchestrator. Defines what to build, creates specs, delegates
- **OpenCode** — primary coder. Takes specs and implements them end-to-end
- **Claude Code** — fallback for specific hard problems
- **MCP servers** — tools that agents call directly (domain sales DB, GitHub API, email)

**The workflow:**

1. **I define the goal.** Not the implementation. "I need a tool that tracks domain renewal dates and emails me 30 days before expiry."

2. **Hermes creates a spec.** A markdown file with: what we're building, why, data flow, constraints, what NOT to do.

3. **OpenCode implements from the spec.** It creates files, installs dependencies, runs tests. If it hits a wall, it reports back with options.

4. **I review and approve.** The spec was clear enough that 90% of what OpenCode produces is correct. I fix the remaining 10%.

This shifted my role from "writing code" to "specifying outcomes." The agents handle the implementation layer.

## MCP Servers Changed Everything

The breakthrough was MCP (Model Context Protocol). Instead of describing APIs to agents in prompts, I connect MCP servers that the agents call directly.

Example: instead of saying "search NameBio for comparable sales of FedZip.com," I connect the Domain Sales MCP server. The agent calls `mcp_domain_sales_comparable_sales(domain="FedZip.com")` and gets real data.

This eliminates:
- The "I can't access external APIs" limitation
- The "you described the API wrong" errors
- The context wasted on API documentation

Every agent I run has access to the same MCP servers. They discover tools autonomously and use them when needed.

## How You Can Do It Too

**Start small:** Pick one repetitive task you do every week. Build an MCP server or script that an agent can run. Let the agent handle it next week.

**Write specs, not prompts.** Instead of "write a login page," write:
- What the login page needs to do
- Which auth provider to use
- What happens after login
- Error states to handle
- Design constraints (responsive, RTL support)

**Give agents tools.** If your agent can't access your database or APIs, it's working blind. Set up read-only access to your data so agents can make informed decisions.

**Review, don't rewrite.** Trust the agent's implementation unless it's wrong. Most agents write code that's 80% correct. Fixing 20% is faster than writing 100% yourself.

## When This Doesn't Work

If you're writing throwaway scripts or one-off data transformations, agent-based development is overkill. Use ChatGPT in chatbot mode.

If your project has strict security or compliance requirements, agent access to production data may not be appropriate.

## FAQs

### Q: How much time do agents actually save?
A: For me, about 40-50% on implementation tasks. Less on architecture and debugging.

### Q: Which AI coding agent is best?
A: Depends on the task. OpenCode is best for Python/Linux tools. Claude Code for complex reasoning. Use the right agent for the job.

### Q: Do I need to know how to code to use agents?
A: Yes, at least enough to review the output. Agents generate code, they don't eliminate the need for understanding.

### Q: What's the best MCP server to build first?
A: Whatever connects to your most frequently used tool. If you run a business, start with an MCP server for your database or your email provider.

---

*Related: [AI Agents for Developers](/articles/ai-agents-for-devs/) — my full agent stack and recommendations. [Building OmniPost](/articles/building-omnipost/) — a concrete example of agent-built automation.*
