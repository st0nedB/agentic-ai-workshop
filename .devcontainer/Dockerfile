# Python-based Codespaces image with four CLI agents.
# This image does not store API keys or preconfigure model providers.
FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Node.js 24 LTS is needed by the current npm packages, including Claude Code.
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends ca-certificates curl gnupg bzip2 unzip; \
    curl -fsSL https://deb.nodesource.com/setup_24.x -o /tmp/nodesource-setup.sh; \
    bash /tmp/nodesource-setup.sh; \
    apt-get install -y --no-install-recommends nodejs; \
    rm -f /tmp/nodesource-setup.sh; \
    rm -rf /var/lib/apt/lists/*

# Install in the normal non-root Codespaces user's home directory.
USER vscode
ENV NPM_CONFIG_PREFIX=/home/vscode/.npm-global
ENV PATH=/home/vscode/.npm-global/bin:/home/vscode/.local/bin:${PATH}

RUN set -eux; \
    mkdir -p "${NPM_CONFIG_PREFIX}" "/home/vscode/.local/bin"; \
    npm install --global --no-audit --no-fund \
      @openai/codex \
      @anthropic-ai/claude-code \
      @mariozechner/pi-coding-agent; \
    curl -fsSL \
      https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh \
      | CONFIGURE=false GOOSE_BIN_DIR="/home/vscode/.local/bin" bash; \
    codex --version; \
    claude --version; \
    goose --version; \
    pi --version
