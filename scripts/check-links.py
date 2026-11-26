#!/usr/bin/env python3
"""Check Markdown inline links and images targeting tracked repository paths."""
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "/st0nedB/agentic-ai-workshop/"
LINK = re.compile(r"\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))")
tracked = subprocess.check_output(["git", "-C", str(ROOT), "ls-files", "-z"]).decode().split("\0")
errors = []
for name in tracked:
    if not name.lower().endswith(".md"):
        continue
    path = ROOT / name
    fenced = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if re.match(r"^\s*(?:\x60{3,}|~{3,})", line):
            fenced = not fenced
            continue
        if fenced:
            continue
        for match in LINK.finditer(line):
            url = urlsplit(match.group(1) or match.group(2))
            if url.netloc or url.scheme:
                if url.netloc.lower() != "github.com" or not url.path.startswith(PREFIX):
                    continue
                relative = url.path[len(PREFIX):]
                if not relative.startswith(("blob/main/", "tree/main/")):
                    continue
                target = ROOT / unquote(relative.split("/", 2)[2])
            elif url.path:
                target = (ROOT if url.path.startswith("/") else path.parent) / unquote(url.path.lstrip("/"))
            else:
                continue
            if not target.exists() or not target.resolve().is_relative_to(ROOT):
                errors.append(f"{name}:{number}: missing or invalid target {match.group(0)}")
if errors:
    raise SystemExit("\n".join(errors))
print("Internal Markdown link and image paths passed.")
