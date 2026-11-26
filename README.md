# Agentic AI Workshop

A hands-on workshop on using, directing, and safely running AI agents. The exercises run in a browser-based GitHub Codespace; no local installation is needed.

## Workshop overview

| Block | Learning objective | Exercises | Slides |
|---|---|---|---|
| 1 — From LLMs to AI Agents | Understand the agent loop, tool use, and autonomous decisions. | 1 — Organize the Chaos | [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/01-from-llms-to-agents.pdf) |
| 2 — Directing AI Agents | Provide context, define success, review plans, and use skills and MCP. | 2 — Analyze measurement data; 3 — Draw the actual workflow | [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/02-directing-ai-agents.pdf) |
| 3 — Sandboxing AI Agents | Understand and compare enforced access boundaries. | 4 — One task, two security boundaries | [PDF](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/03-sandboxing-ai-agents.pdf) |

## Get started

You need a GitHub account and access to a model provider. The setup guides use [OpenRouter](https://openrouter.ai/), which requires an API key and may require purchased credits.

**[Launch or resume the workshop Codespace](https://codespaces.new/st0nedB/agentic-ai-workshop?quickstart=1)**

1. **Sign in to GitHub**.
2. Resume your existing Codespace or select **Create codespace** (preferably **2 cores**) if you do not have one.
3. Wait for **VS Code** to open.
4. Open the terminal and configure your chosen AI agent using the instructions below.

GitHub Codespaces and model inference are billed separately. Codespaces usage counts against your GitHub account and is free within your remaining included allowance. OpenRouter usage depends on the selected model and its pricing. Use an API key with a spending limit where possible, and never put API keys in prompts or tracked files.

## AI agents

The workshop uses two preinstalled CLI agents in the VS Code terminal: OpenCode (`opencode`) and Codex (`codex`).

**[Agent setup instructions (PDF)](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/Agent-Setup.pdf)** — OpenCode (page 1), Codex (page 2).

OpenCode includes **Plan** and **Build** agents. Select Plan to investigate and propose an approach, then Build to carry it out. Exercise 4 uses OpenCode and requires an OpenRouter API key for the isolated run.

## Block 1 — From LLMs to AI Agents

**[Exercise 1 — Organize the Chaos](01_dateichaos/README.md)**

Organize a fictional research folder and observe which files the agent reads, which tools it uses, and which decisions it makes independently. The sample files are automatically prepared in your Codespace. See the [source attribution and CC BY 4.0 license](01_dateichaos/QUELLEN_UND_LIZENZ.md).

## Block 2 — Directing AI Agents

**[Exercise 2 — Analyze measurement data](02_data_analysis/README.md)**

Analyze an organizer-provided HDF5 measurement file. Define an Agent Contract, review a proposed plan, apply a visualization skill, and verify the resulting plots and code. Optional dataset acquisition instructions are included for the organizer.

**Exercise 3 — Draw the actual workflow**

Using the analysis files and code from Exercise 2, connect Excalidraw through MCP and have the agent draw an editable workflow diagram showing the actual processing steps. Verify the diagram against the code. See the Exercise 3 instructions in the [Block 2 slides (PDF)](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/02-directing-ai-agents.pdf) or [slide source](slides/decks/02-directing-ai-agents.md).

## Block 3 — Sandboxing AI Agents

**[Exercise 4 — One task, two security boundaries](03_sandboxing/README.md)**

Compare OpenCode running directly in Codespaces with the same agent inside a restricted Docker container. The exercise uses only synthetic measurements and an invalid dummy SSH key. New Codespaces include Docker-in-Docker. Existing Codespaces created before this feature was added need a rebuild.

## Workshop materials

- [All workshop PDFs — latest release](https://github.com/st0nedB/agentic-ai-workshop/releases/latest)
- [Agent setup instructions (PDF)](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/Agent-Setup.pdf)
- [Prompting cheat sheet (A4 PDF)](slides/handouts/prompting-cheat-sheet.pdf)

The slide PDFs are published with tagged releases. The current source files and instructions for building the slides are available in [slides/](slides/README.md).

## Your files

You can drag and drop files into the VS Code Explorer.

- **`workspace/eingang/`** – your input documents
- **`workspace/ergebnisse/`** – your outputs

These folders are created when the Codespace starts.

---

**At the end:** [Stop your Codespace](https://github.com/codespaces) to stop consuming compute time.
