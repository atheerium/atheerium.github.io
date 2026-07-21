---
title: "How to Build an MCP Server for Your Domain Portfolio (And Sell to AI Agents)"
description: "AI agents are discovering products through MCP servers. Here's how I built one for my 23-domain portfolio — and how you can do it too."
pubDate: 2026-07-21
tags: ["domains", "ai", "agents", "mcp", "tutorial", "automation", "selling"]
---

## The Insight

I wrote about [AI agents starting to spend money](/articles/ai-agents-buying-domains/) and how $8 billion in agentic commerce is flowing in 2026. One reader asked: "OK, but how do I actually sell domains to agents?"

The answer is an MCP server.

Anthropic's Model Context Protocol (MCP) is the standard that lets AI agents discover and call external tools. Think of it as an API designed specifically for agents. When an agent needs to find a domain, it can query an MCP server that knows your portfolio.

I built one for my 23 domains in about an hour. Here's exactly how.

## What an MCP Server Does for Domain Sales

Normally, when someone wants to buy a domain, they:
1. Browse Afternic or a registrar
2. Search by keyword
3. Browse results
4. Click through to evaluate
5. Make an offer or buy

An MCP server compresses steps 1-4 into a single agent query. The agent asks: "Find me available .com domains related to logistics under $500." The MCP server returns structured results. The agent evaluates and decides.

The seller (you) gets:
- **Direct discovery** -- agents find your domains without browsing marketplaces
- **Structured queries** -- agents search by keyword, price, category
- **No negotiation** -- agents either buy or don't
- **First-mover advantage** -- almost no domain investors have this yet

## What You Need

- A domain portfolio (any size from 1 to 100+)
- A server to run the MCP server (a $5 VPS or even the free tier of Render/Fly.io)
- Python 3.10+ and basic Python skills
- 30 minutes

## Step 1: Structure Your Portfolio Data

Create a JSON file with your domains. This is what the MCP server will serve to agents.

```json
{
  "domains": [
    {
      "name": "FedZip.com",
      "price": 299,
      "currency": "USD",
      "category": "logistics",
      "keywords": ["shipping", "delivery", "zip", "courier"],
      "description": "Short brandable for logistics and shipping startups",
      "available": true
    },
    {
      "name": "FinerPay.com",
      "price": 1495,
      "currency": "USD",
      "category": "fintech",
      "keywords": ["payments", "finance", "pay", "fintech"],
      "description": "Premium fintech brand for payment platforms",
      "available": true
    }
  ]
}
```

Include every domain with: name, price, category, keywords (critical for agent search), description, availability.

## Step 2: Create the MCP Server

The server needs to expose tools that an agent can call. The two essential tools are `search_domains` and `get_domain_details`.

Here's a minimal Python MCP server using the official MCP SDK:

```python
# server.py
import json
from mcp.server import Server, stdio_server
from mcp.types import TextContent, Tool

PORTFOLIO = json.load(open("portfolio.json"))
DOMAINS = PORTFOLIO["domains"]

app = Server("domain-portfolio")

@app.list_tools()
async def list_tools():
    return [
        Tool(
            name="search_domains",
            description="Search available domains by keyword, category, or max price",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search keyword"},
                    "category": {"type": "string", "description": "Filter by category"},
                    "max_price": {"type": "number", "description": "Maximum price in USD"},
                    "limit": {"type": "number", "default": 10}
                }
            }
        ),
        Tool(
            name="get_domain_details",
            description="Get full details for a specific domain",
            inputSchema={
                "type": "object",
                "properties": {
                    "domain": {"type": "string", "description": "Domain name"}
                },
                "required": ["domain"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "search_domains":
        results = DOMAINS
        query = arguments.get("query", "").lower()
        category = arguments.get("category", "").lower()
        max_price = arguments.get("max_price", 0)
        limit = arguments.get("limit", 10)
        
        if query:
            results = [d for d in results 
                      if query in d["name"].lower() 
                      or query in d["description"].lower()
                      or any(query in k for k in d["keywords"])]
        if category:
            results = [d for d in results if d["category"] == category]
        if max_price:
            results = [d for d in results if d["price"] <= max_price]
            
        return [TextContent(type="text", text=json.dumps(results[:limit], indent=2))]
    
    elif name == "get_domain_details":
        domain_name = arguments.get("domain", "").lower()
        result = [d for d in DOMAINS if d["name"].lower() == domain_name]
        if result:
            return [TextContent(type="text", text=json.dumps(result[0], indent=2))]
        return [TextContent(type="text", text=json.dumps({"error": "Domain not found"}))]

if __name__ == "__main__":
    app.run(stdio_server())
```

## Step 3: Deploy and Connect

Run the server with stdio transport (for direct agent connection) or SSE (for HTTP access):

```bash
# Install the MCP SDK
pip install mcp

# Run with stdio (agents connect directly)
python server.py
```

To expose it as an HTTP endpoint (so remote agents can reach it):

```python
# sse_server.py
from mcp.server import Server, sse_server
import asyncio

# Use the same app from server.py
# ...

async def main():
    async with sse_server("0.0.0.0", 8000, app) as server:
        await server.serve()

asyncio.run(main())
```

Then configure your agent to use the MCP server. In Claude Code or OpenClaw, you add it to your config file:

```json
{
  "mcpServers": {
    "domain-portfolio": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

Or if you deployed it as an HTTP endpoint:

```json
{
  "mcpServers": {
    "domain-portfolio": {
      "url": "https://your-server.com/mcp"
    }
  }
}
```

## How Agents Actually Use This

Once your MCP server is live, agents can interact with it naturally. Here's what an agent session looks like:

**Human:** "I need a domain for my new payment processing startup. Budget is $2,000."

**Agent:** *queries MCP server* → "I found 3 domains matching 'payments' under $2,000 in your portfolio. FinerPay.com at $1,495 looks like the best fit. It's a short, brandable .com in the fintech category."

**Human:** "Check FinerPay.com details."

**Agent:** *queries MCP server* → "FinerPay.com, $1,495, fintech category. Keywords include payments, finance, pay. Available now. Would you like me to proceed with purchase?"

This is already happening. The agent does the filtering, comparison, and recommendation. The human just confirms.

## What This Means for Your Portfolio

Building an MCP server gives you:

1. **Agent discovery channel** -- most domain portfolios are invisible to agents. Yours won't be.
2. **Structured data advantage** -- agents love clear, machine-readable data. Your competitors who only use Afternic listings don't have this.
3. **Direct connection to buyers** -- no marketplace fees, no broker commissions. The agent finds you directly.
4. **Future-proofing** -- if the projections are right and agent commerce hits $1.5 trillion by 2030, the sellers with MCP servers today will be the established ones.

## When This Doesn't Matter Yet

If your domain portfolio is all expired crap nobody wants, an MCP server won't fix it. The agent still needs good domains to find.

If you only sell on Afternic and don't want direct buyer relationships, keep using Afternic. Agents will find your listings there too -- but they'll compare you against every other listing, and Afternic takes 15-20%.

If you're not comfortable with Python or server management, wait 6 months. Someone will launch a no-code MCP builder for domain portfolios. But by then, everyone will have one.

## The Bottom Line

MCP is to agents what websites were to humans in the 1990s. Having an MCP server for your domain portfolio is the equivalent of having a website when most businesses were still in the Yellow Pages.

I built mine in an hour. It took longer to write this article than to build the server.

## FAQs

### Q: Do I need to be a developer to do this?
A: Basic Python skills are enough. The entire server is about 60 lines of Python. If you can copy-paste and change a few variable names, you can do this.

### Q: Where should I host the MCP server?
A: Any server with Python 3.10+. Free options: Render free tier, Fly.io, or a $5 Linode VPS. Or run it locally and expose it with a Cloudflare Tunnel.

### Q: Will this actually generate sales?
A: Not tomorrow. But it positions you for the wave that's coming. The first MCP servers for domains will be the ones agents learn to query first.

### Q: Should I remove my domains from Afternic if I build an MCP server?
A: No. Keep Afternic listings for human buyers. The MCP server is an additional channel for agent buyers. Use both.

### Q: How do I promote my MCP server to agents?
A: You don't need to. Agents discover MCP servers through configuration files, directories, and tool registries. List your server in the MCP directory at github.com/modelcontextprotocol/servers.

---

*Related: [AI Agents Are Buying Domains](/articles/ai-agents-buying-domains/) -- the strategic overview. [Domain Investing Workflow](/articles/domain-investing-workflow/) -- my full approach to building a portfolio worth an MCP server. [Selling Domains Lessons](/articles/selling-domains-lessons/) -- lessons from 12 months in the market.*
