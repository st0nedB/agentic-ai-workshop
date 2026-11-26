# Agentic AI Workshop

A hands-on workshop on using, directing, and safely running AI agents. The exercises run in a browser-based GitHub Codespace; no local installation is needed.

## Workshop overview

| Block | Learning objective | Exercises | Slides |
|---|---|---|---|
| 1 — From LLMs to AI Agents | Understand the agent loop, tool use, and autonomous decisions. | 1 — Organize the Chaos | [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/01-from-llms-to-agents.pdf) |
| 2 — Directing AI Agents | Provide context, define success, review plans, and use skills and MCP. | 2 — Analyze measurement data; 3 — Draw the actual workflow | [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/02-directing-ai-agents.pdf) |
| 3 — Sandboxing AI Agents | Understand and compare enforced access boundaries. | 4 — One task, two security boundaries | [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/03-sandboxing-ai-agents.pdf) |

The numbered directories correspond to the three workshop blocks. Exercises 2 and 3 share `02_data_analysis/` because the second exercise builds on the analysis from the first.

## Get started

You need a GitHub account and an API key or another form of model access supported by your chosen agent. The setup guides use [OpenRouter](https://openrouter.ai/), which may require purchased credits.

**[Launch or resume the workshop Codespace](https://codespaces.new/st0nedB/agentic-ai-workshop?quickstart=1)**

1. **Sign in to GitHub**.
2. Resume your existing Codespace or select **Create codespace** (preferably **2 cores**) if you do not have one.
3. Wait for **VS Code** to open.
4. Open the terminal and configure your chosen AI agent using the instructions below.

**Costs:** GitHub Codespaces and model inference are billed separately. Codespaces usage is free within your included allowance. A 4-core Codespace consumes that compute allowance twice as fast as a 2-core Codespace, giving you half as many free runtime hours. Model costs depend on your provider and selected model. Never put API keys in prompts or tracked files.

**Idle timeout:** Codespaces automatically stop after 30 minutes of inactivity by default, which can interrupt agent work. I recommend increasing the idle timeout to 60 minutes in your [GitHub Codespaces settings](https://github.com/settings/codespaces).

**Git:** You do not need to push anything to GitHub during this workshop. Working in your Codespace does not grant write access to the upstream workshop repository. If you want to publish your work, use your own repository or fork.

**Forwarded ports:** Keep ports private unless you specifically need to share a service with others.

## AI agents

The workshop uses two preinstalled CLI agents in the VS Code terminal: OpenCode (`opencode`) and Codex (`codex`).

**[Agent setup instructions (PDF)](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/Agent-Setup.pdf)** · [Markdown](slides/handouts/Agent-Setup.md) — OpenCode (page 1), Codex (page 2).

OpenCode includes **Plan** and **Build** agents. Select Plan to investigate and propose an approach, then Build to carry it out. **If you start with Codex, you will also need to configure OpenCode before Exercise 4.**

### Recommended models

If you are unsure which model to use, I recommend starting with [DeepSeek Flash Latest](https://openrouter.ai/~deepseek/deepseek-flash-latest). It is inexpensive and a reasonable choice for the types of tasks we will work on. You are free to use a different model, provided it supports tool calling and works with your agent. See the [model recommendations](MODEL-RECOMMENDATIONS.md) for alternatives.

## Block 1 — From LLMs to AI Agents

### [Exercise 1 — Organize the Chaos](01_file_organization/README.md)

Organize a fictional research folder and observe which files the agent reads, which tools it uses, and which decisions it makes independently. The sample files are automatically prepared in your Codespace. See the [source attribution and CC BY 4.0 license](01_file_organization/SOURCES_AND_LICENSE.md).

## Block 2 — Directing AI Agents

### [Exercise 2 — Analyze measurement data](02_data_analysis/README.md)

Analyze an organizer-provided HDF5 measurement file. Define an Agent Contract, review a proposed plan, inspect and apply an existing visualization skill, and verify the resulting plots and code. A synthetic fallback is available if the organizer-provided file is missing. Optional dataset acquisition instructions are included for the organizer.

### [Exercise 3 — Draw the actual workflow](02_data_analysis/EXERCISE-3.md)

Using the analysis files and code from Exercise 2, find and connect an Excalidraw MCP server of your choice and have the agent draw an editable workflow diagram showing the actual processing steps. Verify the diagram against the code. See the Exercise 3 instructions in the [Block 2 slides (PDF)](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/02-directing-ai-agents.pdf) or [slide source](slides/decks/02-directing-ai-agents.md).

## Block 3 — Sandboxing AI Agents

### [Exercise 4 — One task, two security boundaries](03_sandboxing/README.md)

Compare OpenCode running directly in Codespaces with the same agent inside a restricted Docker container. The exercise uses only synthetic measurements and an invalid dummy SSH key. New Codespaces include Docker-in-Docker. Existing Codespaces created before this feature was added need a rebuild.

## Workshop materials

### Presentations

- Block 1 — From LLMs to AI Agents: [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/01-from-llms-to-agents.pdf) · [Markdown](slides/decks/01-from-llms-to-agents.md)
- Block 2 — Directing AI Agents: [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/02-directing-ai-agents.pdf) · [Markdown](slides/decks/02-directing-ai-agents.md)
- Block 3 — Sandboxing AI Agents: [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/03-sandboxing-ai-agents.pdf) · [Markdown](slides/decks/03-sandboxing-ai-agents.md)

### Handouts

- Agent setup instructions: [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/Agent-Setup.pdf) · [Markdown](slides/handouts/Agent-Setup.md)
- Prompting cheat sheet: [A4 PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/prompting-cheat-sheet.pdf) · [Markdown](slides/handouts/prompting-cheat-sheet.md)

The PDFs are published with [tagged releases](https://github.com/st0nedB/agentic-ai-workshop/releases/latest). For build instructions, see [slides/README.md](slides/README.md).

---

**At the end:** [Stop your Codespace](https://github.com/codespaces) to stop consuming compute time.
