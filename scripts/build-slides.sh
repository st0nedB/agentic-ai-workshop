#!/usr/bin/env bash
# Compile every Markdown deck to PDF through the official Marp Docker image.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if ! command -v docker >/dev/null 2>&1; then
  echo "Fehler: Docker CLI fehlt. Alternativ den GitHub-Actions-Workflow verwenden." >&2
  exit 1
fi

mkdir -p slides/dist
shopt -s nullglob
decks=(slides/decks/*.md)
if (( ${#decks[@]} == 0 )); then
  echo "Keine Markdown-Präsentationen in slides/decks/ gefunden." >&2
  exit 1
fi

for source in "${decks[@]}"; do
  name="$(basename "${source%.md}")"
  target="slides/dist/${name}.pdf"
  echo "Erstelle ${target} ..."
  docker run --rm --init \
    -v "${PWD}:/home/marp/app" \
    -e LANG=C.UTF-8 \
    -e MARP_USER="$(id -u):$(id -g)" \
    marpteam/marp-cli:latest \
    --theme-set slides/themes/tu-ilmenau.css \
    --pdf \
    --output "${target}" \
    "${source}"
done

echo "Fertig: slides/dist/*.pdf"
