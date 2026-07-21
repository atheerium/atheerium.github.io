---
title: "Laguna S 2.1 Free Is Now on OpenCode Zen — Why This Open-Weight Model Is a Big Deal"
description: "Poolside's 118B MoE model landed today with open weights, 1M context, and a free endpoint. It punches way above its 8B active parameters on coding benchmarks."
pubDate: 2026-07-21
tags: ["ai", "models", "opencode", "coding", "open-source", "agents", "review"]
---

## The Release

Poolside released **Laguna S 2.1** today -- and OpenCode added it to their Zen free endpoint within hours. OpenCode announced it with: "Laguna S 2.1 is now free on OpenCode, 1M Context, fully open source. Poolside's most capable model to date."

This is the kind of release that doesn't make front-page news but actually matters for developers who build with AI agents.

## The Specs

| | Laguna S 2.1 |
|---|---|
| **Architecture** | MoE (Mixture of Experts) |
| **Total params** | 118B |
| **Active params** | **8B** per token |
| **Context window** | **1M tokens** (1,048,576) |
| **License** | OpenMDW-1.1 (open-weight) |
| **Released** | July 21, 2026 |
| **Available on** | OpenCode Zen (free), OpenRouter (free), Hugging Face, Ollama |
| **Local hardware** | Runs on single DGX Spark (NVFP4 quantized) |

The headline stat: **8B active parameters.** That's tiny. For comparison, DeepSeek V4 Pro Max has 49B active. Claude Fable 5 has undisclosed but estimated 100B+. Nemotron 3 Ultra has 55B active.

Laguna S 2.1 does what it does with 8B active params. That's the story.

## Benchmarks

Here's how it stacks up against models many times its size:

### Terminal-Bench 2.1 (real-world terminal tasks)

| Model | Active Params | Score |
|-------|:------------:|:-----:|
| Kimi K3 | 50B | 88.3 |
| Claude Fable 5 | ~100B+ | 88.0 |
| **Laguna S 2.1** | **8B** | **70.2** |
| Tencent Hy3 | 21B | 71.7 |
| Inkling | 41B | 63.8 |
| DeepSeek V4 Pro Max | 49B | 64.0 |
| Nemotron 3 Ultra | 55B | 56.4 |

### Other Benchmarks

| Benchmark | Laguna S 2.1 | DeepSeek V4 Pro Max | Comparison |
|-----------|:------------:|:-------------------:|:----------:|
| SWE-Bench Multilingual | **78.5** | 76.2 | +2.3 points |
| SWE-Bench Pro (Public) | **59.4** | 55.4 | +4 points |
| **DeepSWE** | **40.4** | **9.0** | **+31.4 points** |
| SWE Atlas (Codebase QnA) | **46.2** | 27.2 | +19 points |
| Toolathlon Verified | 49.7 | **55.9** | -6.2 points |

The DeepSWE score is the standout. Laguna S 2.1 crushes DeepSeek V4 Pro Max (40.4% vs 9.0%) despite having 6x fewer active parameters. DeepSWE tests real-world, long-horizon software engineering tasks -- the kind of work coding agents actually do.

On SWE-Bench Multilingual, it even edges out Qwen 3.7 Max (78.3) and DeepSeek V4 Pro Max (76.2).

## Why the Active Parameter Count Matters

MoE models only activate a fraction of their total parameters per token. Laguna S 2.1's 8B active means:

1. **Fast inference** -- fewer params to compute per token
2. **Run locally** -- fits on consumer hardware with quantization
3. **Lower cost at scale** -- 8B active = 1/6th the compute of a 49B active model
4. **Free endpoint is sustainable** -- Poolside can offer free access because it's cheap to serve

Poolside specifically mentions it runs on a single NVIDIA DGX Spark with the official NVFP4 quantized version. That's a $3,000 desktop machine, not a data center.

## Open Weights + Free API = Unusual

Most model releases give you either open weights or a free API, rarely both.

- Open weights on Hugging Face under OpenMDW-1.1 license
- Free on OpenCode Zen with full 1M context
- Free on OpenRouter with 262K context
- Available on Ollama for local runs

You can:
1. **Use it for free** today through OpenCode or OpenRouter -- no credit card needed
2. **Run it locally** on a DGX Spark or similar through Ollama
3. **Fine-tune it** since the weights are open
4. **Build products on it** under the OpenMDW-1.1 license

This combination is rare for a model that scores 40%+ on DeepSWE.

## How It Compares to Other Free Models

On OpenCode Zen, the free tier now includes:

| Model | Context | Best For |
|-------|:-------:|----------|
| Big Pickle | N/A | General reasoning |
| Nemotron 3 Ultra | 1M | Heavy coding |
| DeepSeek V4 Flash | 1M | Speed |
| MiMo V2.5 | 1M | Multimodal |
| North Mini Code | 256K | Light tasks |
| **Laguna S 2.1** | **1M** | **Agentic coding** |
| Hy3 preview | 256K | Coding |

Laguna S 2.1 fills the "agentic coding" slot that was previously missing from the free tier. The 1M context on a free endpoint is also unusually generous.

## The Timing

This launched on the same day as Gemini 3.6 Flash. Two coding model releases on the same day, but very different approaches:

- **Gemini 3.6 Flash**: Proprietary, API-only, $7.50/1M output, 49% DeepSWE
- **Laguna S 2.1**: Open-weight, free API, 8B active, 40.4% DeepSWE

For local/offline agent setups, Laguna S 2.1 is the more interesting option because you can actually run it yourself.

## The Bottom Line

I switched my coding agent's secondary model to Laguna S 2.1 on OpenCode Zen free to test it. For a model with 8B active parameters, the coding quality is surprising. The DeepSWE score against larger models suggests Poolside optimized specifically for the kind of work coding agents do -- long tool call chains, debugging, multi-file edits.

If you run coding agents and haven't tried it, it's worth a test drive. Free endpoint, 1M context, no credit card. Hard to beat that price.

## FAQs

### Q: Is Laguna S 2.1 really free?
A: Yes. OpenCode Zen offers it free (no credit card needed). OpenRouter also has a free endpoint with 262K context. Both are legitimate free tiers, not trials.

### Q: Can I run Laguna S 2.1 locally?
A: Yes. It's on Ollama and Hugging Face. With 8B active params, it can run on a single high-memory machine. The official NVFP4 quantized version runs on a DGX Spark.

### Q: How does it compare to DeepSeek V4 Flash?
A: Different strengths. DeepSeek V4 Flash is faster. Laguna S 2.1 is better at complex multi-step coding tasks and has a much higher DeepSWE score.

### Q: What's the license?
A: OpenMDW-1.1 from Poolside. Open-weight, allows commercial use. Check the license terms on Hugging Face for specifics.

### Q: Is it better than Gemini 3.6 Flash?
A: On raw coding benchmarks, Gemini 3.6 Flash scores higher (49% vs 40.4% on DeepSWE). But Gemini is proprietary and costs $7.50/1M output. Laguna S 2.1 is open-weight and free. Different tools for different constraints.

### Q: 8B active parameters seems small. Does it actually work well for complex tasks?
A: Yes -- that's the surprising part. The benchmarks show it beating models with 5-6x more active parameters. The MoE architecture lets it be small at inference time while retaining high capability.

---

*Related: [Gemini 3.6 Flash Released](/articles/gemini-3-6-flash-released/) -- also launched today. [AI Agents for Developers](/articles/ai-agents-for-devs/) -- my current agent stack and how I choose models. [OpenCode vs Claude Code](/articles/opencode-vs-claude-code/) -- comparing the two coding agent platforms.*
