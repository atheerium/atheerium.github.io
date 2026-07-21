---
title: "Domain-ion -- Unified Domain Toolkit"
description: "A CLI and MCP server for domain appraisal, comparable sales, trademark checks, lead generation, and portfolio management."
pubDate: 2026-07-15
tags: ["domains", "tools", "cli", "mcp"]
status: "active"
url: "https://github.com/atheerium/domain-ion"
---

Domain-ion is my unified domain toolkit. It replaces a collection of separate scripts with a single CLI that covers the full domain workflow.

## Features

- **Appraise** — five-factor domain valuation
- **Comps** — comparable sales from 19K+ records
- **Trademark check** — USPTO/EUIPO/WIPO via Signa API
- **Leads** — contact discovery and lead generation
- **Portfolio** — track owned domains, prices, and status

All accessible via CLI or MCP server.

## Architecture

Python CLI built with Typer, backed by SQLite + external APIs. The MCP server wraps the same functionality for use with AI agents.

## Status

Actively maintained. Daily use for domain evaluation and outreach workflow.
