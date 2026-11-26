#!/usr/bin/env bash
# Compile every Markdown deck to PDF through the official Marp Docker image.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if ! command -v docker >/dev/null 2>&1; then
  echo "Error: Docker CLI not found. Use the GitHub Actions workflow instead." >&2
  exit 1
fi

mkdir -p slides/dist
shopt -s nullglob
decks=(slides/decks/*.md)
if (( ${#decks[@]} == 0 )); then
  echo "No Markdown decks found in slides/decks/." >&2
  exit 1
fi

for source in "${decks[@]}"; do
  name="$(basename "${source%.md}")"
  target="slides/dist/${name}.pdf"
  echo "Building ${target} ..."
  docker run --rm --init \
    -v "${PWD}:/home/marp/app" \
    -e LANG=C.UTF-8 \
    -e MARP_USER="$(id -u):$(id -g)" \
    marpteam/marp-cli@sha256:3cf660df7b9737f875e57f7169dff0b08d1d3ab604ea2d655ab761102942fa42 \
    --theme-set slides/themes/tu-ilmenau.css \
    --allow-local-files \
    --pdf \
    --output "${target}" \
    "${source}"
done

python3 slides/handouts/prompting-cheat-sheet.py --output-dir slides/dist
python3 slides/handouts/agent-setup.py --output-dir slides/dist

echo "Done: slides/dist/*.pdf"
