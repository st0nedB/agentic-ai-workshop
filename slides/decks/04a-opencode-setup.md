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

# OpenCode

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

# 3 · Connect OpenRouter

Start the agent:

```bash
opencode
```

In the OpenCode interface:

1. Type `/connect` and press Enter.
2. Search for and select **OpenRouter**.
3. Paste your API key and confirm.

The slash command is entered inside OpenCode, not in Bash.

---

# 4 · Select a model

Inside OpenCode, type:

```text
/models
```

Select a model listed under **OpenRouter**.

- Prefer a model with tool-calling support.
- Check its pricing on [OpenRouter Models](https://openrouter.ai/models).
- Check the selected model before sending your first prompt.

Use **Tab** to switch between Plan and Build when those agents are available.

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

- **Unauthorized:** run `/connect` again and check your key.
- **Insufficient credits:** check your OpenRouter balance.
- **Model unavailable:** select another OpenRouter model with `/models`.
- **Unexpected file changes:** use Plan mode and inspect changes before accepting them.

Exit with `/exit`. Reopen with `opencode`.

Documentation: [OpenCode providers](https://opencode.ai/docs/providers/) · [Models](https://opencode.ai/docs/models/)
