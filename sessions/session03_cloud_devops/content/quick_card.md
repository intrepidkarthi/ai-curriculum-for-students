# Quick Card — Session 03: Cloud & DevOps (AI-assisted CI/CD)

Duration: 60 min
Goal: Containerize a tiny API and set up CI that runs tests — using Ollama throughout.

Tools: Local LLM via Ollama + VS Code Continue (draft API/tests, Dockerfile/.dockerignore, CI YAML)

Minute-by-minute
- 0–5: Ollama quick check (VS Code Task: Local AI: Check Ollama)
- 5–10: Cloud + CI/CD basics
- 10–20: Generate API scaffold + tests (Continue → Ollama)
- 20–35: Generate Dockerfile + .dockerignore; build and run locally
- 35–50: Generate GitHub Actions CI; push; iterate minimal diffs to green
- 50–60: Wrap and homework

Artifact
- Screenshot of green CI + `curl /health` output

Homework
- Extend CI (add ruff/mypy and pip cache); write with LLM assistance

Copy-ready prompts (paste into Continue)
- API scaffold: "Create a FastAPI app with GET /health -> {\"status\":\"ok\"} and GET /sum?a&b -> {\"sum\": a+b}. Provide app/main.py only."
- Tests: "Write pytest tests for /health and /sum, including missing param failure. Return tests/test_app.py using TestClient."
- Dockerfile: "Draft a Dockerfile for python:3.11-slim; install from requirements.txt; copy app to /app/app; run uvicorn app.main:app on 0.0.0.0:8000."
- .dockerignore: "Generate a .dockerignore for Python: __pycache__/, *.pyc, .venv/, .git/, .mypy_cache/, .pytest_cache/, node_modules/."
- CI yaml: "Write a GitHub Actions workflow for pytest on push/PR to main/master using Python 3.11; cache pip; run pytest -q."
