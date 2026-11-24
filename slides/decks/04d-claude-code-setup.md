---
marp: true
theme: tu-ilmenau
size: 16:9
paginate: true
lang: en-US
header: Agentic AI Workshop
footer: Technische Universität Ilmenau · AI Agent Workshop
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Claude Code

## Connect to OpenRouter

Workshop · 2026

---

# 1 · Get your OpenRouter API key

1. Sign in at [openrouter.ai](https://openrouter.ai).
2. Add credits if you intend to use paid models.
3. Open [API Keys](https://openrouter.ai/settings/keys) and create a key.
4. Copy the key. Set a spending limit if available.

**Keep the key private:** never put it in a prompt, Git repository or screenshot.

OpenRouter bills model usage independently of your GitHub account.

---

# 2 · Open the workshop terminal

In the Codespace, select **Terminal → New Terminal** in VS Code.

The harness is already installed. No installation is necessary.

Check that you are in the workshop repository:

```bash
pwd
git rev-parse --show-toplevel
```

Commands on the following slides go into this terminal.

---

# 3 · Load the API key

In the Bash terminal, run these commands:

```bash
read -rsp "OpenRouter API key: " OPENROUTER_API_KEY
export OPENROUTER_API_KEY
echo
```

Paste the key when prompted, then press Enter.

The input is hidden. Nothing is written to shell history.

**New terminal?** Repeat this step before launching the agent.

---

# 4 · Configure the OpenRouter connection

Run the following in the same Bash terminal:

```bash
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""
```

This redirects Claude Code's model requests to OpenRouter.

The empty API key prevents conflicts with direct Anthropic authentication.

These settings are temporary; repeat them in a new terminal.

---

# 5 · Select a Claude model and launch

For this workshop, Claude Code requires an **Anthropic Claude model**. Do not select other model families.

```bash
export ANTHROPIC_DEFAULT_SONNET_MODEL="~anthropic/claude-sonnet-latest"
claude --model sonnet
```

Sonnet is a balanced starting point. The alias selects the current Sonnet model; check its price on [OpenRouter Models](https://openrouter.ai/models).

If you previously signed in directly to Claude, use `/logout` inside Claude Code and restart before proceeding.

---

# 6 · Verify the provider

Inside Claude Code, enter:

```text
/status
```

Confirm that the status identifies:

- Auth token: `ANTHROPIC_AUTH_TOKEN`
- Anthropic base URL: `https://openrouter.ai/api`

If a direct Claude account is shown instead, resolve the authentication conflict before sending a task.

---

# Test the connection

At the agent's prompt, enter:

> Reply with CONNECTED. Do not read or modify files or run commands.

1. Check that the agent replies.
2. Open [OpenRouter Activity](https://openrouter.ai/activity).
3. Check that a new request appears with the expected model.

A reply alone does not prove the request went through OpenRouter.

---

# Watch your token budget

**Claude Code can consume your token budget faster than other harnesses.**

- Agent context and repeated model calls can increase token usage.
- Auxiliary operations may make additional model requests.
- Long sessions and large file reads can increase costs.

Keep tasks scoped and inspect [OpenRouter Activity](https://openrouter.ai/activity) regularly.

Actual usage varies by model, task, caching and session length.

---

# If the connection fails

- **Unauthorized:** check the key and all three connection variables.
- **Wrong provider:** use `/logout` if previously signed in, then restart.
- **Model error:** select an available Claude model.
- **Insufficient credits:** check the OpenRouter balance.

Exit with `/exit`. Reload the variables in a new terminal.

Documentation: [OpenRouter Claude Code integration](https://openrouter.ai/docs/guides/coding-agents/claude-code-integration)
