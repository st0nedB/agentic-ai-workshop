#!/usr/bin/env python3
"""Tiny single-purpose OpenRouter relay. Credentials stay OUTSIDE the sandbox.

DEMONSTRATION ONLY: No authentication between sandbox and relay. This endpoint
must only bind to the internal Docker bridge address, never a public interface.
The agent can use this relay to spend inference credits, even without seeing
the API key. For a production setup add request authorization, rate limiting,
network policy, and appropriate upstream access controls.
"""
import argparse
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class Handler(BaseHTTPRequestHandler):
    server_version = "WorkshopLLMRelay/0.1"

    def do_GET(self):
        if self.path == "/health":
            return self.send_json(200, {"status": "ok"})
        if self.path == "/v1/models":
            name = self.server.model
            return self.send_json(200, {
                "object": "list",
                "data": [{"id": name, "object": "model"}],
            })
        return self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/v1/chat/completions":
            return self.send_json(404, {"error": "endpoint not permitted"})
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self.send_json(400, {"error": "invalid size"})
        if not 0 < size <= 2_000_000:
            return self.send_json(413, {"error": "request too large"})
        body = self.rfile.read(size)
        try:
            payload = json.loads(body)
            if not isinstance(payload, dict):
                raise ValueError("expected a JSON object")
        except (ValueError, UnicodeDecodeError):
            return self.send_json(400, {"error": "invalid JSON"})
        # Prevent selecting a different model through the relay.
        payload["model"] = self.server.model
        request = Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": "Bearer " + self.server.token,
                "Content-Type": "application/json",
                "Accept-Encoding": "identity",
            },
            method="POST",
        )
        try:
            with urlopen(request, timeout=180) as upstream:
                self.send_response(upstream.status)
                self.send_header("Content-Type", upstream.headers.get("Content-Type", "application/json"))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                while True:
                    chunk = upstream.read(16384)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
        except HTTPError as error:
            # Limit error details, avoid forwarding upstream headers.
            self.send_json(error.code, {"error": "upstream inference error", "status": error.code})
        except (URLError, TimeoutError, OSError):
            try:
                self.send_json(502, {"error": "upstream unavailable"})
            except (BrokenPipeError, ConnectionResetError):
                pass

    def send_json(self, code, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, _format, *_args):
        # No request bodies or provider credentials in terminal logs.
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bind", required=True, help="Docker bridge IP only")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--model", default="openrouter/auto")
    args = parser.parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        parser.error("OPENROUTER_API_KEY must be set in the Codespace")
    server = ThreadingHTTPServer((args.bind, args.port), Handler)
    server.token = api_key
    server.model = args.model
    print(f"Inference relay listening at {args.bind}:{args.port} (internal Docker bridge)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
