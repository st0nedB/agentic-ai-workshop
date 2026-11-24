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

# Goose

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

# 3 · Configure the provider

In the terminal, start the configuration wizard:

```bash
goose configure
```

1. Choose **Configure Providers**.
2. Select **OpenRouter**.
3. Enter your OpenRouter API key when prompted.

If a keyring is unavailable, use the environment-variable method on the next slide instead.

---

# Alternative · Configure without a keyring

In a Bash terminal, run:

```bash
read -rsp "OpenRouter API key: " OPENROUTER_API_KEY
export OPENROUTER_API_KEY
echo
export GOOSE_PROVIDER=openrouter
read -rp "OpenRouter model ID: " GOOSE_MODEL
export GOOSE_MODEL
```

Enter a full model ID from [OpenRouter Models](https://openrouter.ai/models), such as `openai/gpt-5.6-sol`.

These values apply only to this terminal.

---

# 4 · Select a model and launch

If you used the wizard, select or enter the full OpenRouter model ID when asked. Choose a model with tool-calling support and check its price.

Start an interactive session:

```bash
goose session
```

Check the provider and model reported at startup.

If you used environment variables, launch from the same terminal.

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

- **Keyring error:** use the environment-variable setup.
- **Unauthorized:** check the API key.
- **Model error:** verify the full model ID and tool support.
- **Insufficient credits:** check the OpenRouter balance.

Use `Ctrl+C` to interrupt if necessary.

Documentation: [Goose providers](https://goose-docs.ai/docs/getting-started/providers/) · [Environment variables](https://goose-docs.ai/docs/guides/environment-variables/)
