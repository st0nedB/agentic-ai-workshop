# Small, disposable agent runtime for the Block 3 isolation demonstration.
# Built inside the participant's Codespace using Docker-in-Docker.
FROM node:24-bookworm-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends python3 git ca-certificates \
 && rm -rf /var/lib/apt/lists/* \
 && npm install -g --no-audit --no-fund @opencode/cli

RUN mkdir -p /lab/working && chown node:node /lab/working
USER node
ENV HOME=/home/node
WORKDIR /lab/working
CMD ["opencode"]
