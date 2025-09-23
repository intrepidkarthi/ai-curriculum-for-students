# Session 02 — Programming Challenges (with Local LLM)

How to run tests
- VS Code: Terminal → Run Task → "Session 2: Run Challenges (unittest)"
- Or CLI: `python -m unittest discover -s sessions/session02_dsa/content/challenges -p 'test_*.py' -v`

Prompts to use in Continue (Ollama)
- Tests first: "Generate 6 edge-case tests for [CHALLENGE] with capacity=1/overwrites or tricky inputs."
- Constrain: "Target O(1) per op if possible; explain trade-offs briefly."
- Fix: "Given this failing test + code, propose a minimal diff patch."
- Explain: "Summarize complexity and a real-world usage in 5 lines."

Challenges
- LRU Cache — O(1) get/put
- Bracket Validator — stacks and O(n)
- Two Sum — hash map vs two-pointers
- Grid Shortest Path — BFS on a grid
