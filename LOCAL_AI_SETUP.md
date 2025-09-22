# Local AI Setup — Ollama + VS Code Continue

This guide helps students run all sessions with local AI tools only. No paid APIs required.

## Prerequisites
- VS Code (latest) + Continue extension
- Ollama (macOS/Linux/Windows): https://ollama.com
- Optional: Python 3.11+ for running helper scripts

## Install and run Ollama
1) Install Ollama from the website above and launch it (or run `ollama serve`).
2) Pull at least one local model:
   ```bash
   ollama pull phi3:mini                 # very light, fast
   ollama pull llama3.2:3b-instruct      # balanced
   # optional if your laptop is strong:
   ollama pull mistral:7b-instruct
   ```
3) Smoke test the server:
   ```bash
   ollama list
   curl -s http://127.0.0.1:11434/api/tags | head -c 200
   ```

## Configure VS Code Continue (Provider: Ollama)
- Install the "Continue" extension from the VS Code marketplace.
- In Continue settings, set the provider to Ollama and choose your model.
- Example config (JSON preview):
  ```json
  {
    "models": {
      "default": {
        "provider": "ollama",
        "model": "llama3.2:3b-instruct"
      }
    }
  }
  ```
- You can switch models during class (e.g., to `phi3:mini`) for faster responses.

## Local smoke test script (optional)
Run the helper to check Ollama availability and one short generation:
```bash
python scripts/local_ai_check.py --model llama3.2:3b-instruct --prompt "Say 'Hello TCE'."
```
Expected: it prints detected models and a short response.

## Troubleshooting
- "Connection refused": ensure `ollama serve` is running and not blocked by a firewall.
- "Model not found": run `ollama pull <model>` and try again.
- Responses are slow: switch to a smaller model like `phi3:mini` or reduce prompt size.
- Token/cutoff issues: keep prompts short; avoid pasting giant texts.

## Tips for class
- In pairs: one laptop can run Ollama and share via LAN (replace 127.0.0.1 with host IP) if needed.
- Keep a fallback model pre-pulled (phi3:mini) for live demos.
- Encourage students to version their prompts and save best ones in their repo.
