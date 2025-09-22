# AI Engineering for Placements — 10-Session Curriculum

![CI](https://github.com/<your-user>/ai-engineering-curriculum-10-sessions/actions/workflows/ci.yml/badge.svg)

Repository: `ai-engineering-curriculum-10-sessions`

This is a practical, placement-first curriculum that uses AI tools in every session. It is designed for typical student laptops and emphasizes demonstrable artifacts recruiters value.

## AI Engineering Ladder (4 Levels)
- Level 1 — Using AI: prompts, function-calling, APIs, tokens/parameters.
- Level 2 — Integrating AI: RAG, embeddings, similarity search, caching, agents/tool-use.
- Level 3 — Engineering AI Systems: guardrails, evaluations, multi-model patterns.
- Level 4 — Optimizing at Scale: cost/latency, routing, privacy, governance, observability.

## Sessions Overview (60 min each)
1) AI & Generative AI in Industry — Interactive only (no coding). Demo: AI Career Map. Artifact: 1-page use case + diagram.
2) DSA for Placements — LLM-assisted problem solving with tests. Artifact: tested snippet + complexity note.
3) Cloud & DevOps — LLM-drafted Dockerfile + CI. Artifact: green CI screenshot.
4) Cybersecurity & Ethical Hacking — LLM phishing analysis + password policy. Artifact: short analysis.
5) Full-Stack & Modern Frameworks — LLM-written API spec + micro front-end. Artifact: short screen recording + docs.
6) Blockchain, Crypto & Web3 — LLM-generated Solidity + testnet deploy. Artifact: contract address + README.
7) System Design & Scalability — LLM diagrams + bottleneck critique. Artifact: 1-page design doc.
8) AI in Cybersecurity & Fraud — LLM-guided anomaly detector demo. Artifact: mini report with metrics.
9) Agents & Automation — Orchestrate a multi-step flow (n8n or simple agent). Artifact: flow screenshot + README.
10) Career Roadmap & Readiness — LLM resume polishing + mock interview. Artifact: recruiter-ready README + bullets + demo.

## Tools we’ll use (local-only)
- LLM: Ollama (local models) + VS Code Continue extension
- Recommended models: `phi3:mini` (very light), `llama3.2:3b-instruct` (balanced), `mistral:7b-instruct` (if laptop allows)
- Coding assistance: VS Code Continue (configured to use Ollama)
- Orchestration: n8n (runs locally, optional)
- Diagrams/docs: Mermaid diagrams and README drafts generated via the local LLM

See:
- Local AI Setup: `LOCAL_AI_SETUP.md`
- Reusable Prompts Pack: `prompts/reusable_prompts.md`

## Quick start

```bash
# clone and set up (replace <your-user> with your GitHub username)
git clone https://github.com/<your-user>/ai-engineering-curriculum-10-sessions.git
cd ai-engineering-curriculum-10-sessions
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# try Session 2 challenges (local tests)
python -m unittest discover -s sessions/session02_dsa/content/challenges -p 'test_*.py' -v
```

### Local AI setup
1) Install Ollama (https://ollama.com)
2) Pull models (pick based on your laptop):
   ```
   ollama pull phi3:mini               # very light, fast
   ollama pull llama3.2                # balanced
   ollama pull mistral                 # larger, needs more RAM
   ollama pull codellama               # code-focused
   ```
3) Install VS Code Continue extension and set Provider to Ollama with your chosen model.
4) Use Continue chat to scaffold code, tests, docs, and diagrams using local models only.

Workshop reference
- Session 09 n8n local workshop: `sessions/session09_agents_automation/content/n8n_workshop.md`

## How to use this repo
- Instructor: start with `sessions/InstructorHandbook.md` and the quick cards under `sessions/sessionXX_*/content/quick_card.md`.
- Students: each session yields a small artifact (code snippet, diagram, mini report). Keep these in your personal repo fork with a recruiter-facing README.
