# Agentic AI Workshop

A browser-based environment for the workshop. No local installation is needed.

### Get started

**[Launch or resume the workshop Codespace](https://codespaces.new/st0nedB/agentic-ai-workshop?quickstart=1)**

1. **Sign in to GitHub**.
2. Resume your existing Codespace or select **Create codespace** (preferably **2 cores**) if you do not have one.
3. Wait for **VS Code** to open.

### AI agents

The workshop uses two CLI agents in the VS Code terminal: `codex` and `opencode`. Connect your chosen agent to a model provider before using it.

**Agent setup instructions (PDF):**

- [OpenCode](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/04a-opencode-setup.pdf)
- [Codex](https://github.com/st0nedB/agentic-ai-workshop/releases/latest/download/04c-codex-setup.pdf)

OpenCode includes **Plan** and **Build** agents. Select Plan to investigate and propose an approach, then Build to carry it out.

### First hands-on exercise

**[01 – Organize the Chaos](01_dateichaos/README.md)**: A fictional folder is automatically prepared in your Codespace. See the [source attribution and CC BY 4.0 license](01_dateichaos/QUELLEN_UND_LIZENZ.md).

### Task 02 — Data analysis

**[02 – UAV measurement data](02_data_analysis/README.md)**: Analyze an organizer-provided HDF5 measurement file. Optional dataset acquisition instructions are included for the organizer.

### Block 3 — Container isolation

[Exercise 4: One task, two security boundaries](03_sandboxing/README.md) compares OpenCode running directly in Codespaces with the same agent inside a restricted Docker container. The exercise uses only synthetic measurements and an invalid dummy SSH key. New Codespaces include Docker-in-Docker. Existing Codespaces need a rebuild.

### Workshop slides

The [Markdown slide template](slides/decks/00-template.md) uses TU Ilmenau's documented colors. PDFs are built through [GitHub Actions](.github/workflows/build-slides.yml). See the [slide build instructions](slides/README.md).

### Your files

You can drag and drop files into the VS Code Explorer.

- **`workspace/eingang/`** – your input documents
- **`workspace/ergebnisse/`** – your outputs

These folders are created when the Codespace starts.

---

**At the end:** [Stop your Codespace](https://github.com/codespaces) to stop consuming compute time.

*Note: Usage counts against your own GitHub account. It is free within your remaining included allowance.*
