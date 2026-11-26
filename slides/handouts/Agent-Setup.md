# Agent setup

Connect to OpenRouter from your workshop Codespace.

Generated from agent-setup.py; edit that source, not this file.

## OpenCode

### 1. Get an API key

Sign in at [openrouter.ai](https://openrouter.ai). Add credits for paid models. Create a key at [API Keys](https://openrouter.ai/settings/keys) and set a spending limit if available. Never share the key in prompts, Git or screenshots. OpenRouter bills separately from GitHub.

### 2. Open the terminal

In the Codespace, select **Terminal > New Terminal**. The agent is preinstalled. Check the repository root with `git rev-parse --show-toplevel`. Start the agent in the relevant exercise folder to focus its context; this is not a security boundary.

### 3. Start and connect

Run `opencode` in the terminal. Inside OpenCode, enter `/connect`, select OpenRouter, paste the key and confirm. Slash commands are entered in the agent, not Bash. The saved login normally survives a restart; reconnect after a rebuild or deletion if needed.

### 4. Select a model

Enter `/models` and choose DeepSeek Flash Latest or another OpenRouter model with tool-calling support. Check prices at [OpenRouter Models](https://openrouter.ai/models) and verify the selected model.

### 5. Plan and build

Use Shift+Tab to switch between Plan and Build in OpenCode 2.x; check the on-screen shortcut if it differs. Review the plan before allowing edits.

### 6. Verify the connection

Prompt: *Run pwd and report its output. Do not modify files.* Check the actual tool call and verify the expected model appears in [OpenRouter Activity](https://openrouter.ai/activity).

### 7. Troubleshoot

Unauthorized: reconnect and check the key. Insufficient credits: check your balance. Model unavailable: choose another via `/models`. Exit with `/exit`; reopen with `opencode`.

## Codex

### 1. Get an API key

Sign in at [openrouter.ai](https://openrouter.ai). Add credits for paid models. Create a key at [API Keys](https://openrouter.ai/settings/keys) and set a spending limit if available. Never share the key in prompts, Git or screenshots. OpenRouter bills separately from GitHub.

### 2. Open the terminal

In the Codespace, select **Terminal > New Terminal**. The agent is preinstalled. Check the repository root with `git rev-parse --show-toplevel`. Start the agent in the relevant exercise folder to focus its context; this is not a security boundary.

### 3. Load the key

In Bash, run the following and paste the key when prompted. Input is hidden; repeat in each new terminal or after a Codespace restart.

```
read -rsp "OpenRouter API key: " OPENROUTER_API_KEY
export OPENROUTER_API_KEY
echo
```

### 4. Open configuration

```
mkdir -p ~/.codex
nano ~/.codex/config.toml
```

Preserve existing settings. Home-directory config may be lost on rebuild; deletion removes the Codespace.

### 5. Configure provider

```
model = "~deepseek/deepseek-flash-latest"
model_provider = "openrouter"

[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
wire_api = "responses"

[model_providers.openrouter.auth]
command = "sh"
args = ["-c", "echo $OPENROUTER_API_KEY"]
```

Save with Ctrl+O, Enter; exit with Ctrl+X.

### 6. Start Codex

Start with DeepSeek Flash Latest, or choose another compatible full ID from [OpenRouter Models](https://openrouter.ai/models) with Responses API and tool support. Run `codex` in the same terminal. Use `/model` or `/status` inside Codex.

### 7. Verify the connection

Prompt: *Run pwd and report its output. Do not modify files.* Check the actual tool call and verify the expected model appears in [OpenRouter Activity](https://openrouter.ai/activity).

### 8. Troubleshoot

Check the key, credits, TOML syntax and model compatibility. Exit with `/quit`.
