# Small, disposable agent runtime for the Block 3 isolation demonstration.
# Built inside the participant's Codespace using Docker-in-Docker.
FROM node:24-bookworm-slim

ARG OPENCODE_VERSION
LABEL workshop.opencode.version=$OPENCODE_VERSION

RUN apt-get update \
 && apt-get install -y --no-install-recommends python3 git ca-certificates \
 && rm -rf /var/lib/apt/lists/* \
 && test -n "$OPENCODE_VERSION" \
 && npm install -g --no-audit --no-fund "@opencode/cli@$OPENCODE_VERSION"

RUN mkdir -p /lab/working && chown node:node /lab/working
USER node
ENV HOME=/home/node
WORKDIR /lab/working
CMD ["opencode"]
