#!/usr/bin/env python3
"""Create OpenRouter participant keys and save their one-time secrets to CSV."""
import argparse
import csv
from datetime import datetime, timedelta, timezone
import getpass
import json
import math
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from uuid import UUID


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--workspace-id", type=UUID, metavar="UUID",
                        help="Create all keys in this OpenRouter workspace")
    parser.add_argument("--limit", type=float, default=10.0, help="USD per key (default: 10)")
    parser.add_argument("--reset", choices=("daily", "weekly", "monthly"),
                        help="Default: a single lifetime budget per key")
    parser.add_argument("--expires-at", help="Default: 30 days from now. Override with a UTC timestamp, e.g. 2027-01-15T18:00:00Z")
    parser.add_argument("--prefix", default="workshop")
    parser.add_argument("--output", default="workshop-keys.csv", help="New CSV file")
    args = parser.parse_args()
    if args.count < 1 or not math.isfinite(args.limit) or args.limit <= 0:
        parser.error("count and limit must be positive and finite")

    token = os.environ.get("OPENROUTER_MANAGEMENT_KEY") or getpass.getpass("OpenRouter management key: ")
    if not token.strip():
        parser.error("a management key is required")
    expiry = datetime.now(timezone.utc) + timedelta(days=30)
    settings = {"limit": args.limit, "limit_reset": args.reset,
                "expires_at": args.expires_at or expiry.strftime("%Y-%m-%dT%H:%M:%SZ")}

    if args.workspace_id is not None:
        settings["workspace_id"] = str(args.workspace_id)

    fd = os.open(args.output, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["name", "api_key"])
        output.flush()
        for index in range(1, args.count + 1):
            name = f"{args.prefix}-{index:02d}"
            request = Request("https://openrouter.ai/api/v1/keys", method="POST",
                              data=json.dumps(dict(settings, name=name)).encode(),
                              headers={"Authorization": f"Bearer {token.strip()}",
                                       "Content-Type": "application/json"})
            try:
                with urlopen(request, timeout=30) as response:
                    secret = json.load(response)["key"]
                if not isinstance(secret, str) or not secret:
                    raise ValueError("empty API key in response")
                writer.writerow([name, secret])
                output.flush()
                os.fsync(output.fileno())
            except HTTPError as exc:
                sys.exit(f"Stopped at {name}: HTTP {exc.code} ({exc.reason}). Earlier rows are in {args.output}.")
            except (OSError, URLError, ValueError, KeyError) as exc:
                sys.exit(f"Stopped at {name} ({type(exc).__name__}). Check this key in OpenRouter before retrying. Earlier rows are in {args.output}.")
    print(f"Saved {args.count} keys to {args.output}")


if __name__ == "__main__":
    try:
        main()
    except OSError as exc:
        sys.exit(str(exc))
