# Which model should I use?

For this workshop, I recommend starting with **DeepSeek Flash Latest**. There is little reason to start with an expensive model for relatively simple tasks such as organizing files, analyzing data or writing small Python scripts. You can always switch models if you find that the current one is struggling.

DeepSeek Flash Latest automatically points to the latest model in the Flash family. If you would like to try a different model, the following are reasonable options:

| Model | Input / 1M tokens | Output / 1M tokens |
|---|---:|---:|
| [DeepSeek Flash Latest](https://openrouter.ai/~deepseek/deepseek-flash-latest) | $0.036 | $0.50 |
| [GLM 5.3 Flash](https://openrouter.ai/z-ai/glm-5.3-flash) | $0.036 | $0.082 |
| [GPT-6 Luna](https://openrouter.ai/openai/gpt-6-luna) | $0.10 | $0.50 |

*OpenRouter prices as of 26 November 2026, rounded where appropriate. Follow the model links for current prices.*

The GLM and DeepSeek models are particularly interesting if you want to experiment with inexpensive open-weight alternatives. The GPT models are another option for both OpenCode and Codex. Gemini is worth considering if you also want to work with images. These are candidates, not models that have all been tested in the workshop.

## How much will it cost?

As an example, one million input tokens and 100,000 output tokens cost about $0.086 with DeepSeek Flash Latest (10:1 is a typical ratio), compared with $0.15 with GPT-6 Luna. An agent may consume considerably more tokens than a conventional chatbot, since it repeatedly reads files, executes tools and sends their results back to the model. Actual costs depend on how you use it.

If you do not want to spend money, you can also try [OpenRouter Free](https://openrouter.ai/openrouter/free). However, free models have request limits that you may reach rather quickly during a workshop like this.

I recommend setting a spending limit on your API key and occasionally checking your [usage](https://openrouter.ai/activity).

## Using your chosen model

In OpenCode, select the model via `/models`. In Codex, use the model ID in your configuration as described in the [agent setup guide](slides/handouts/Agent-Setup.md). Codex requires a model that supports the Responses API and tool calling. Before starting the exercises, check that your agent can execute a simple command.
