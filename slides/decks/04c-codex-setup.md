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

# OpenAI Codex

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

# 4 · Open the Codex configuration

Run:

```bash
mkdir -p ~/.codex
nano ~/.codex/config.toml
```

The file is in your home directory, outside the workshop repository.

On a fresh Codespace, it may be empty.

If it already contains settings, preserve unrelated settings and avoid duplicate TOML keys or sections.

The next slide shows the configuration to enter.

---

# 5 · Enter the OpenRouter configuration

```toml
model = "openai/gpt-5.6-sol"
model_provider = "openrouter"

[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
wire_api = "responses"

[model_providers.openrouter.auth]
command = "sh"
args = ["-c", "echo $OPENROUTER_API_KEY"]
```

Save: **Ctrl+O**, Enter. Exit: **Ctrl+X**.

The configuration references the key without storing its value.

---

# 6 · Choose a model and start Codex

The previous slide uses an example model ID. Replace it with a compatible full ID from [OpenRouter Models](https://openrouter.ai/models) if needed.

The model must support the **Responses API** and agent tool calls.

Start Codex in the same terminal:

```bash
codex
```

Inside Codex, use `/model` to select another available model and `/status` to inspect the session.

---

# Test the connection

At the agent's prompt, enter:

> Reply with CONNECTED. Do not read or modify files or run commands.

1. Check that the agent replies.
2. Open [OpenRouter Activity](https://openrouter.ai/activity).
3. Check that a new request appears with the expected model.

A reply alone does not prove the request went through OpenRouter.

---

# If the connection fails

- **Unauthorized:** reload your API key in the same terminal.
- **Configuration error:** check TOML syntax and the file location.
- **Model error:** check the full model ID and Responses API support.
- **Insufficient credits:** check the OpenRouter balance.

Exit with `/quit`. On a new terminal, reload the key.

Documentation: [OpenRouter Codex CLI setup](https://openrouter.ai/blog/tutorials/codex-cli-openrouter/)
