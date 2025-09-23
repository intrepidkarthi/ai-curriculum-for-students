# Quick Card — Session 02: DSA for Placements (AI-assisted)

Duration: 60 min
Goal: Ship 2 green programming challenges with AI help; map to real systems.

Tools: Local LLM via Ollama + VS Code Continue, unittest/pytest (optional)

Minute-by-minute
- 0–5: Rules & scoreboard
- 5–10: Why DSA matters (real system mapping)
- 10–45: Pick any 2 programming challenges (LRU, Brackets, Two Sum, Min Stack, Grid BFS)
  - tests first (use LLM), implement, fix, summarize
- 45–55: Demo: Continue + Ollama flow (tests → code → fix → summarize)
- 55–60: Scoreboard + wrap

Artifact
- Two tested snippets + short complexity/usage notes.

Homework
- Solve one DP problem; include LLM-generated tests and explanation.
- Optional: micro-bench your LRU (hit/miss mix) and add a note.

Prompts to try (paste into Continue)
- "Generate 6 edge-case tests for [CHALLENGE]. Include capacity=1/overwrites or tricky inputs."
- "Target O(1) per op if possible; explain trade-offs briefly."
- "Given this failing test and code, propose a minimal diff."
- "Summarize time/space complexity and a real usage in 5 lines."
