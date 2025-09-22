---
marp: true
paginate: true
class: lead
---

# AI & Generative AI in Industry (2025)

Trends, Use‑Cases, Careers — Interactive Session (No coding)

---

## Today’s Plan (60 min)

- Icebreaker: your goals and interests (5m)
- AI landscape: what changed, why now (10m)
- College projects you can build (15m)
- Interactive: AI Career Map (15m)
- Group activity: design a use case + diagram (10m)
- Share‑outs & what’s next (5m)

---

## What changed (Why now)?

- Foundation models: pretraining + instruction tuning → strong zero/few‑shot skills
- Tool‑use: function calling + structured outputs → reliable actions
- Long context: from short prompts to hundreds of pages
- Local models: 3B–7B run on student laptops (quantized)
- Ecosystem: prompt patterns, eval toolkits, open models, GPUs everywhere

---

## College Projects — Campus Life

Build ideas
- Attendance OCR → CSV + summary + export to Sheets
- Notes summarizer + quiz maker (topics + flashcards)
- Timetable optimizer & clash detector
- Hostel/issues bot → polite email drafts + tracking
- Event poster + description generator (image + copy)
- Lecture recorder summarizer → key timestamps + action items
- Campus marketplace (books/electronics; price alerts; safety tips)
- Hackathon teammate finder (skills + availability matching)
- Lost & Found with OCR (image→text item registry)

---

## College Projects — Placement & Coding

Build ideas
- Resume bullet generator (metrics‑first, 2‑line max)
- Mock interview Q&A with feedback and follow‑ups
- DSA kata coach (writes tests, gives hints, tracks progress)
- PR reviewer (diff review + test suggestions)
- System design diagrammer + bottleneck critique

---

## College Projects — Creators & Communities

Build ideas
- YouTube chaptering + SEO tags
- Stream highlights auto‑clip detector
- Meme/caption generator with templates
- Discord/WhatsApp TA bot (FAQ + forms)
- Personal site page generator (try v0.dev / Bolt.new)

---

## What to Measure (for demos)

- Time saved per task; adoption (# users/sessions)
- Accuracy/faithfulness or test pass‑rate
- Content throughput (posts/videos/summaries per hour)
- Latency; cost (local = zero tokens); satisfaction score

---
 
## By the Numbers (2024–2025)

- Business adoption: 78% of orgs used AI in 2024 ([AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report))
- GenAI investment: ~$33.9B private funding in 2024 (+18.7% YoY) ([AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report))
- Model leadership: U.S. leads frontier model production; China narrowing gap ([AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report))
- Local models: 3B–7B run on student laptops via quantization
- Productivity: multiple studies report significant time savings on text/coding tasks

---

## AI Engineering Ladder — Overview

- Level 1: Using AI — prompts, tokens/params, local LLMs or HTTP APIs
- Level 2: Integrating AI — RAG, embeddings, caching/batching, safe tool‑use
- Level 3: Engineering Systems — guardrails, evaluations, multi‑model patterns
- Level 4: Optimizing at Scale — serving, routing, observability, privacy/compliance

---
 

## Local vs Cloud Models — When to Use Which

Local (on‑device or on‑laptop)
- Privacy by design; low latency; no cost per token; works offline
- Great for ideation, coding help, summaries, small RAG
Cloud/Hosted
- Access to frontier capabilities; managed scaling; stronger multimodality
Tradeoffs
- Quantization (e.g., 4‑bit) enables 3B–7B locally
- Retrieval quality (chunking/reranking) often matters more than raw model size

---

## LLMs — What They Are (under the hood)

- Tokenization (e.g., BPE) turns text into tokens
- Embedding layer maps tokens → vectors
- Transformer blocks = multi‑head self‑attention + MLP; residual connections + LayerNorm
- Causal mask enforces left‑to‑right generation
- Positional/rotary encodings (RoPE) help long‑context
- Next‑token probabilities via softmax over vocabulary logits
- Context window limits how much fits; KV cache speeds long generations

---

## How LLMs Are Built (training pipeline)

- Data curation: filtering/dedup; code‑heavy corpora for coder models
- Pretraining: next‑token prediction on large text/code mixtures
- Instruction tuning (SFT): supervised pairs for following instructions
- Preference optimization: RLHF/PPO or DPO with pairwise human prefs
- Adapters: LoRA/QLoRA target attention/MLP modules (rank≈8–32)
- Quantization: int8/4‑bit (NF4/GPTQ/AWQ) trades accuracy for VRAM/speed
- Inference controls: temperature, top‑p/top‑k, stop tokens; avoid high T for coding
- Retrieval (RAG): extend context with external docs; rerank before synthesis
- Evaluation: pass@k (code), RAG faithfulness + hit@k, latency/throughput, safety

---

## Self‑Attention — The Core Step

- Q = XWq, K = XWk, V = XWv; Attention = softmax(QKᵀ/√d)V
- Multi‑head: parallel attentions concatenated, then projected
- Causal mask zeros future positions (autoregressive decoding)
- Intuition: attend to relevant past tokens; compose meaning across layers

---

## Transformer Block Layout (ASCII)

```text
[Input]
  |> LayerNorm -> Multi-Head Self-Attention -> Add (residual)
  |> LayerNorm -> MLP (GELU/SiLU) -> Add (residual)
[Output]
```

---

## Tokenization & Positional Encoding

- BPE/Unigram split text into subwords; vocab ≈ 30–100k tokens
- Code tokenizers handle symbols/whitespace better (indentation, braces)
- Positional: sinusoidal vs RoPE; RoPE helps longer ranges; ALiBi alternative
- Practical: chunk long fields (logs/docs), keep function/paragraph boundaries

---

## Inference Strategies & Controls

- Greedy (argmax) → deterministic; often brittle
- Sampling: top‑p (0.8–0.95), top‑k (20–100), temperature (0.1–0.9)
- Coding defaults: low T (0.1–0.3), moderate top‑p; set stop sequences
- Max tokens, repetition penalties to reduce loops

---

## Sampling Presets (cheat sheet)

- Coding (deterministic): T=0.1–0.2, top_p=0.7–0.9, stop on tests/asserts
- Refactor/explain: T=0.2–0.3, top_p=0.8–0.95, short max tokens
- Brainstorming: T=0.7–0.9, top_p=0.9–0.98, allow longer outputs
- Safety: always set explicit stop sequences and validate JSON/schema

---

## Quantization & Serving

- Quantization: int8/4‑bit (NF4/GPTQ/AWQ) → 2–4× less memory, small quality drop
- Hardware: 8–16GB RAM runs 3B @4‑bit; 16–24GB for 7B locally
- Serving: KV cache reuse; paged attention; vLLM/TGI for batching/throughput
- Tradeoffs: latency vs throughput; CPU works, Apple Silicon/GPUs are faster

### Memory/Latency Budget (rough guide)

- 3B @4‑bit, 4k tokens: ~4–6 GB RAM; single‑thread latency ~1–3s/100 tokens (CPU)
- 7B @4‑bit, 4k tokens: ~8–12 GB RAM; Apple M‑series is comfortable
- Longer context doubles KV cache cost; prefer RAG + rerank over naive long prompts
- Batch/stream where possible; avoid blocking I/O in handlers

---

## RAG Deep Dive (retrieval‑augmented generation)

- Pipeline: split → embed → index → retrieve → (rerank) → synthesize
- Chunking: 300–800 tokens with 10–20% overlap; preserve semantic units
- Index: FAISS/HNSW/ScaNN; filter with metadata
- Rerank: cross‑encoders boost precision@k; reduces hallucinations
- Metrics: hit@k/MRR/nDCG, faithfulness/attribution, latency, cost

---

## Guardrails & Structured Outputs

- JSON schemas / function calling for tool use and validation
- Allowlists for tools/URLs; redact secrets/PII; content filters
- Prompt‑injection defenses: isolate/quote untrusted inputs; strip instructions
- Fail closed: refusal + friendly fallback; log adversarial tests

---

## Current Leading Models — Text & Code (2025)

Proprietary (hosted)
- Frontier families lead on coding/reasoning (e.g., GPT‑4 class, Claude 3.5 class, Gemini 1.5+)

Open‑source (local/hosted)
- Llama 3.x family (sizes from small to large)
- Mistral/Mixtral (inc. MoE variants)
- Qwen 2/2.5 series (general/coder variants)
- Phi‑3 (efficient small models)


---

## Coding LLMs (2025)

Capabilities
- Code generation and refactor; tests and docs; fill‑in‑the‑middle; tool/function calling
Practical picks (local‑first)
- Llama 3.x Instruct, Qwen2.5‑Coder (various sizes), Mistral/Mixtral Instruct — run via Ollama
Hosted/frontier (context)
- GPT‑4‑class, Claude 3.5‑class, Gemini 1.5+ excel on complex coding/reasoning
Caveats
- Hallucinated APIs/methods; mitigate with retrieval/snippets, strict schemas, and unit tests
Light eval ideas
- Try 5 small coding tasks; count how many it gets right on the first try (or within 3 tries)
- Run unit tests to confirm behavior
- Run a linter and a type checker to catch issues early
- Skim the code diff for unsafe calls or obvious bugs
  
---

## AI Coding IDEs & Tools (2025)
  
For class (free, local)
- VS Code + Continue (Provider: Ollama)
- Models: `phi3:mini`, `llama3.2:3b-instruct`, `mistral:7b-instruct` (if laptop allows)
Hosted & IDEs (landscape)
- Claude (Projects), Windsurf, Cursor, Lovable, Bolt.new, v0.dev, Replit (Ghostwriter)
- Also: GitHub Copilot, Codeium, Amazon Q, JetBrains AI
Tips
- Paste failing tests; ask for small diffs; keep prompts short
  
---

## Current Leading Models — Multimodal (Vision/Audio/Gen)

Vision‑Language (VLMs)
- Qwen‑VL, LLaVA‑Next, Llama 3.x‑Vision: captioning, doc‑QA, UI reading

Speech/Audio
- Whisper Large‑v3 (ASR), Distil‑Whisper (faster), local TTS options (e.g., Piper)

Image/Video Generation
- Stable Diffusion SDXL/SD3, Flux (image). Video remains mostly cloud‑hosted today


## Prompt Patterns (Level 1 — Using AI)

- Zero‑shot → direct instruction
- Few‑shot → show 2–3 high‑quality examples
- Chain‑of‑Thought → ask for steps, then final answer
- Self‑critique → “check for missing assumptions/risks”

---

## Safety & Ethics (always‑on)

- Refusals: better to say “I don’t know” than hallucinate
- Privacy: avoid sensitive data in prompts; redact where possible
- Prompt injection: sanitize inputs; don’t run untrusted tools
- Attribution: cite sources for grounded answers

---

## Interactive: AI Career Map (15m)

Activity
- Students list interests and target roles
- Use local LLM to generate roles, skills, and a 4‑week plan
Output
- Screenshot or saved text for personal repo

---

## Group Activity: Design a Use Case (10m)

In pairs
- Pick a domain (fintech/healthcare/gaming/campus)
- Define: problem, user, constraints (privacy/latency), success metric
- Ask local LLM for a Mermaid diagram of the pipeline
Deliverable
- One slide (or note) with problem → approach → metric + diagram

---

## Sources & Links

- Stanford AI Index (latest)
- Corporate/state‑of‑AI surveys (e.g., McKinsey, developer surveys)
- Open model releases: Llama 3.x, Mistral, Phi‑3 (official blogs)
- Safety/regulation: EU AI Act overview
- Local tooling: Ollama, VS Code Continue
