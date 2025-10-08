# Instructor Handbook — AI Engineering for Placements

This handbook provides session-by-session guidance. Session 1 is fully interactive (no coding). Sessions 2–10 add hands-on demos with heavy AI-tool usage.

## Course principles
- Local-first where possible; minimize friction and focus on artifacts.
- AI tools everywhere: use LLMs for ideation, scaffolding, tests, docs, diagrams, and evaluation narratives.
- Placement-first: every session yields a tangible artifact.

## References
- Local AI Setup: `LOCAL_AI_SETUP.md`
- Reusable Prompts Pack: `prompts/reusable_prompts.md`

## AI Engineering Ladder
- Level 1 — Using AI: prompt patterns (zero/few-shot, CoT), function-calling/APIs, tokens/params.
- Level 2 — Integrating AI: RAG + embeddings; caching/batching; agents & tool-use.
- Level 3 — Engineering AI Systems: guardrails; evals (RAG faithfulness/hit-rate/win-rate); multi-model patterns.
- Level 4 — Optimizing at Scale: cost/latency, routing, observability, privacy/governance.

## Sessions summary
1) AI & GenAI in Industry (interactive only) — Demo: AI Career Map.
2) DSA for Placements — LLM-assisted problem + tests.
3) Cloud & DevOps — LLM-drafted Dockerfile + CI.
4) Cybersecurity — Phishing analysis + password policy.
5) Full-Stack — API + micro front-end.
6) Web3 — Minimal smart contract on testnet.
7) System Design — WhatsApp-lite design.
8) AI for Security/Fraud — Anomaly detector.
9) Agents & Automation — Multi-step orchestration.
10) Career Roadmap — README + bullets + mock interview.

---

## Session 01 — AI & Generative AI in Industry (Interactive only)
- Learning outcomes
  - Distinguish AI vs ML vs DL; identify GenAI impact across sectors.
  - Frame use-cases with value, risk, and ethics.
- Agenda (60 min)
  - 0–10: Icebreakers; collect student backgrounds.
  - 10–25: AI landscape; examples in fintech/healthcare/gaming.
  - 25–45: Live “AI Career Map” exploration (students feed interests → roles, skills, 4-week plan). No coding.
  - 45–55: Small-group activity: draft one use case with risks; use LLM to generate a simple Mermaid diagram.
  - 55–60: Share-out; set expectations for Session 2.
- AI tools
  - Ollama + VS Code Continue to ideate use-cases and produce diagrams/docs.
- Artifact
  - 1-page use case + career map + diagram (students keep in their personal repo).
- Homework
  - Refine use case and risks with an LLM critique.

## Session 02 — Data Structures & Algorithms for Placements
- Learning outcomes
  - Practice a classic problem and link it to real systems.
- Agenda (60 min)
  - 0–10: Why DSA still matters; real usages (indexes, caches, recsys).
  - 10–40: Live problem (e.g., LRU cache or Two Sum) with LLM-generated tests; then edit/refine.
  - 40–55: Pair activity on a second problem; LLM explains complexity.
  - 55–60: Assign homework DP problem.
- AI tools
  - VS Code Continue (Ollama) for scaffolding, edge-case tests, and complexity write-up.
- Artifact
  - Tested snippet + short complexity/usage note.

## Session 03 — Cloud Computing & DevOps
- Learning outcomes
  - Understand CI/CD basics; containerize a small API.
- Agenda (60 min)
  - 0–10: Cloud primitives; Docker/K8s in a nutshell.
  - 10–20: CI/CD concepts; environments; secrets.
  - 20–45: Draft minimal API + Dockerfile + CI YAML via LLM; fix errors iteratively.
  - 45–55: Show local run and green CI.
  - 55–60: Homework brief.
- AI tools
  - Local LLM via VS Code Continue drafts Dockerfile/workflow and README; Continue scaffolds the API.
- Artifact
  - Green CI screenshot + run command.

## Session 04 — Cybersecurity & Ethical Hacking
- Learning outcomes
  - Identify phishing patterns; articulate password strength policies.
- Agenda (60 min)
  - 0–10: Threat landscape.
  - 10–25: Security basics: MFA, encryption, firewalls.
  - 25–45: LLM phishing analyzer + password strength lab.
  - 45–55: Careers & certs.
  - 55–60: Homework brief.
- AI tools
  - Local LLM via Ollama + VS Code Continue for classification/explanation and policy drafting.
- Artifact
  - Short analysis write-up.

## Session 05 — Full-Stack Development & Modern Frameworks
- Learning outcomes
  - API-first thinking; simple front-end integration.
- Agenda (60 min)
  - 0–10: MERN/MEAN overview; microservices basics.
  - 10–40: Build a notes API + micro front-end; LLM proposes validation rules and errors.
  - 40–55: Add pagination or input validation.
  - 55–60: Homework brief.
- AI tools
  - Local LLM via VS Code Continue drafts API spec/docs and generates fetch/handlers; local LLM checks edge cases.
- Artifact
  - Short screen recording + API README.

## Session 06 — Blockchain, Crypto & Web3
- Learning outcomes
  - Basics of blockchain, wallets, contracts.
- Agenda (60 min)
  - 0–15: Real use cases beyond tokens.
  - 15–45: LLM-drafted Solidity + tests; deploy via Remix to testnet.
  - 45–55: Risks and roles.
  - 55–60: Homework brief.
- AI tools
  - Local LLM via Ollama + VS Code Continue drafts contract/tests and explains functions and risks.
- Artifact
  - Contract address + README.

## Session 07 — System Design & Scalability
- Learning outcomes
  - Communicate trade-offs; design under constraints.
- Agenda (60 min)
  - 0–10: LB, caching, queues, databases, CDNs.
  - 10–35: WhatsApp-lite design; LLM bottleneck critique.
  - 35–55: Mock design interview (URL shortener/news feed).
  - 55–60: Homework brief.
- AI tools
  - Local LLM via Ollama + VS Code Continue produces Mermaid diagram, capacity estimates, and critiques.
- Artifact
  - One-page design doc with diagram.

## Session 08 — AI in Cybersecurity & Fraud Detection
- Learning outcomes
  - Basics of anomaly detection; tradeoffs and false positives.
- Agenda (60 min)
  - 0–10: Fraud/SOC landscape.
  - 10–40: Train/evaluate a toy anomaly detector; LLM narrates evaluation.
  - 40–55: Threshold tuning and escalation policy.
  - 55–60: Homework brief.
- AI tools
  - Local LLM via Ollama + VS Code Continue synthesizes a small dataset and drafts the notebook and evaluation narrative.
- Artifact
  - Mini report with metrics.

## Session 09 — Agents & Automation
- Learning outcomes
  - Orchestrate multi-step flows; design safe tool-use.
- Agenda (60 min)
  - 0–10: Agent patterns; function-calling; allow/deny lists.
  - 10–40: Build a simple n8n flow (webhook → transform → API → branch).
  - 40–55: Add a guardrail and a second branch (fallback).
  - 55–60: Homework brief.
- AI tools
  - Local LLM via Ollama + VS Code Continue drafts tool-call JSON, error messages, and user copy; n8n orchestrates.
- Artifact
  - Flow screenshot + short README.

## Session 10 — Tech Career Roadmap & Placement Readiness
- Learning outcomes
  - ATS-ready bullets; recruiter README; short demo pitch.
- Agenda (60 min)
  - 0–15: Roles & interview funnels.
  - 15–30: Resume clinic with LLM rewrites (metrics-first bullets).
  - 30–45: Mock interview Q&A with LLM coaching.
  - 45–55: 3–5 min candidate showcase.
  - 55–60: Next steps.
- AI tools
  - Local LLM via Ollama + VS Code Continue rewrites bullets, generates a recruiter README draft, and provides mock Q&A.
- Artifact
  - Recruiter-ready README + bullets + demo link.
