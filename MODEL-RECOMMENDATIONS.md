# Recommended workshop models

You may use any model that works with your chosen agent. The following OpenRouter models are affordable candidates for the workshop, selected for coding and tool use rather than just chatbot performance.

Prices checked **26 November 2026**. USD per million tokens, as displayed on the linked model pages. Actual rates depend on provider routing, caching, reasoning, and discounts; check the current prices before starting.

| Model | Input / 1M | Output / 1M | When to choose it |
|---|---:|---:|---|
| [GLM 5.3 Flash](https://openrouter.ai/z-ai/glm-5.3-flash) | $0.0356 | $0.0815 | Very low-cost candidate for iterative coding and tool use. |
| [DeepSeek V4.1 Flash 1017](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017) | $0.036 | $0.50 | Low-cost alternative for multi-step analysis and debugging. |
| [GPT-6 Luna](https://openrouter.ai/openai/gpt-6-luna) | $0.10 | $0.50 | Recommended starting point: affordable, general-purpose agent work. |
| [GPT-5.6 Luna](https://openrouter.ai/openai/gpt-5.6-luna) | $0.20 | $1.20 | Alternative used in the workshop's Codex configuration example. |
| [Gemini 3.8 Flash](https://openrouter.ai/google/gemini-3.8-flash) | $0.75 | $3.75 | More expensive optional alternative for multimodal analysis; price includes a temporary discount. |
| [OpenRouter Free](https://openrouter.ai/openrouter/free) | $0 | $0 | For experimenting without paying for inference; routes between free models. |

The first four paid models appear in [OpenRouter's Codex usage statistics](https://openrouter.ai/apps/codex), providing evidence of real-world harness use, not a guarantee of reliability. All paid entries are candidates for OpenCode. Test the chosen model before starting; the workshop does not certify individual model/provider combinations.

## Select a model

- **OpenCode:** connect OpenRouter, then choose the model using `/models`. Use a model with tool-calling support.
- **Codex:** use the full OpenRouter ID from the linked model page in the `model` field of `~/.codex/config.toml`, or select it in `/model` if available. The model must work with the Responses API and tools.
- **Exercise 4:** the isolated agent uses the OpenRouter gateway. Set `WORKSHOP_MODEL` to a full model ID, e.g. `openai/gpt-6-luna`. You may choose different models for the two runs; record which models you used.

See the [agent setup guide](slides/handouts/Agent-Setup.md). Verify real tool execution with a harmless command such as `pwd`, and check the model and cost in [OpenRouter Activity](https://openrouter.ai/activity).

## Cost guidance

A workload of 1 million billable, uncached input tokens and 100,000 output tokens would cost about $0.15 with GPT-6 Luna or $0.32 with GPT-5.6 Luna at the displayed rates, excluding fees and taxes. This is an illustrative workload, not an estimate of actual workshop consumption. Agents can make many requests and resend growing context. Reasoning tokens may contribute to output charges.

Set a personal API-key spending limit and check usage during exercises. Free variants generally have [lower request quotas](https://openrouter.ai/pricing) (typically 50 requests per day without a qualifying credit purchase), and can be unavailable or throttled. They are useful for trying the workshop but should not be the only planned option for a full day. The free router can also change the underlying model between calls.

See [current tool-capable models](https://openrouter.ai/collections/tool-calling-models/) and the [OpenRouter model catalogue](https://openrouter.ai/models) for alternatives.
