#!/usr/bin/env python3
"""
Local AI check script for Ollama.
- Lists available models
- Optionally generates a short response with a selected model

Usage:
  python scripts/local_ai_check.py --model llama3.2:3b-instruct --prompt "Say 'Hello TCE'"
"""

import argparse
import json
import sys
import time
from urllib import request, error

OLLAMA_URL = "http://127.0.0.1:11434"


def get(url: str):
    req = request.Request(url, method="GET")
    with request.urlopen(req, timeout=10) as resp:
        return resp.read().decode("utf-8")


def post_json(url: str, payload: dict):
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    with request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="llama3.2:3b-instruct", help="Ollama model name to use")
    parser.add_argument("--prompt", default="Say 'Hello from Ollama'", help="Prompt to generate")
    args = parser.parse_args()

    print("Checking Ollama server at", OLLAMA_URL)
    try:
        tags_raw = get(f"{OLLAMA_URL}/api/tags")
        tags = json.loads(tags_raw)
    except error.URLError as e:
        print("ERROR: Could not reach Ollama. Is it running? Try: ollama serve")
        print("Details:", e)
        sys.exit(1)
    except Exception as e:
        print("ERROR: Unexpected error talking to Ollama /api/tags:", e)
        sys.exit(1)

    models = [m.get("name") for m in tags.get("models", [])]
    print("Detected models:")
    for m in models:
        print(" -", m)
    if args.model not in models:
        print(f"NOTE: Model '{args.model}' not found in listed models. You may need to pull it: ollama pull {args.model}")

    print("\nAttempting a short generation ...")
    payload = {
        "model": args.model,
        "prompt": args.prompt,
        "stream": False,
    }
    t0 = time.time()
    try:
        gen_raw = post_json(f"{OLLAMA_URL}/api/generate", payload)
        gen = json.loads(gen_raw)
    except Exception as e:
        print("ERROR: Failed to generate from Ollama:", e)
        sys.exit(2)

    dt = time.time() - t0
    print("Response (truncated):")
    text = gen.get("response", "")
    print(text[:300])
    print(f"\nLatency: {dt:.2f}s")


if __name__ == "__main__":
    main()
