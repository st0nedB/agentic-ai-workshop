# Exercise 3 — Draw the actual workflow

**Block 2 · 35 minutes · Group work**

## Prerequisites

Use the analysis code and outputs from [Exercise 2](README.md). Find an MCP server that lets your agent draw in Excalidraw. Inspect its documentation and decide how to connect it to your chosen agent. No particular server or setup method is prescribed.

Inspect the server's source, installation instructions and requested permissions before running it. A local MCP server can execute code under your user account. Keep any forwarded Codespaces ports private unless sharing is necessary.

If Exercise 2 is incomplete, use your existing partial analysis code and any available outputs. Diagram only implemented processing steps and explicitly note incomplete or unexecuted stages; do not invent missing steps.

## Assignment

If you have exited your agent since Exercise 2, reopen it from the analysis directory:

```bash
cd "$(git rev-parse --show-toplevel)"
cd 02_data_analysis
opencode  # or: codex
```

Ask the agent to inspect the actual analysis code and create an editable Excalidraw diagram of its workflow. Show the input, file loading, data transformations, visualization and outputs. Do not invent processing steps.

1. **Connect and inspect (10 min):** Find and connect an Excalidraw MCP server. Identify the code, input and outputs to be visualized.
2. **Draw (15 min):** Ask the agent to create a diagram using the MCP drawing tools. Observe the actual tool calls. Use the visualization or export mechanism provided by your chosen server.
3. **Verify (10 min):** Compare each node and edge with the implementation. Correct missing or invented steps, incorrect labels and unexplained branches.

Save the editable diagram as `02_data_analysis/results/workflow.excalidraw` (export it from Excalidraw if necessary). Record the source script used and any limitations in `results/WORKFLOW.md`.

**Success:** The diagram is editable, includes named inputs and outputs, accurately represents the implemented code and distinguishes any unexecuted steps, and can be opened in Excalidraw.
