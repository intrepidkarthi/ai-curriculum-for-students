---
marp: true
paginate: true
class: lead
---

# DSA for Placements (AI‑assisted)

Real systems, real patterns — with local LLM help

---

## Today’s Plan (60m)

- Why DSA matters in real systems (5m)
- Rules & scoreboard (5m)
- Programming Challenges (choose 2): LRU, Brackets, Two Sum, Min Stack, Grid BFS (35m)
- Live demo with Continue + Ollama (10m)
- Wrap: complexity notes + repo artifacts (5m)

---

## Why DSA matters (fast mapping)

- Caches → LRU/LFU → feed scroll, API rate limits
- Editors/IDEs → stacks/tries → undo/redo, autocompletion
- Maps/chat → graphs/queues → routing, fan‑out
- Search/retrieval → hashing/sets → de‑dup, joins
- Campus apps → BFS/DP → path, scheduling

---

## Rules & Scoreboard

- Tests first: ask the LLM to draft edge‑case tests
- Timebox: 15–20m per challenge
- Pairing: navigator (prompts) + driver (code)
- Scoreboard: tests pass, time to green, clean code
  - Extensions: micro‑bench (optional), memory notes

---

## Local AI Setup — Ollama + Continue

- Install Ollama (macOS/Linux/Windows): https://ollama.com
- Pull models (pick 1–2 based on laptop):
```bash
ollama pull phi3:mini               # very light, fast
ollama pull llama3.2   # balanced
# optional if your laptop is strong:
ollama pull mistral
ollama pull codellama
ollama run deepseek-r1
```
- Start server: run the Ollama app or `ollama serve`
- Smoke test:
```bash
ollama list
curl -s http://127.0.0.1:11434/api/tags | head -c 200
```

---

## Configure VS Code Continue (Provider: Ollama)

- Install "Continue" extension in VS Code
- Set Provider: Ollama; pick your model (switchable in class)
- Example config (preview):
```json
{
  "models": {
    "default": { "provider": "ollama", "model": "llama3.2:3b-instruct" }
  }
}
```
- Tip: use `phi3:mini` if responses are slow

---

## Model Presets (speed vs quality)

- `phi3:mini` — fastest, very light; great for tests and small diffs
- `llama3.2:3b-instruct` — balanced; better reasoning while still light
- `mistral:7b-instruct` — optional; needs stronger laptop (16GB+)
- Tip: switch models mid-session in Continue if you need more speed/quality

---

## Troubleshooting (quick)

- Connection refused → ensure `ollama serve` is running
- Model not found → `ollama pull <model>`
- Slow responses → smaller model, shorter prompts

---

## Run Tests Quickly

- VS Code Task: Terminal → Run Task → "Session 2: Run Challenges (unittest)"
- CLI:
```bash
python -m unittest discover -s sessions/session02_dsa/content/challenges -p 'test_*.py' -v
```

---

## Big-O Snack (quick intuition)

- O(1), O(log n), O(n), O(n log n), O(n^2) — know when they appear
- Rules: nested same-range loops → O(n^2); divide & conquer → O(n log n)
- Space ↔ time tradeoffs: extra memory can buy O(1) per op (e.g., LRU)

---

## Data Structures at a Glance

- List/Array: O(1) index; O(n) mid insert/delete — buffers, random access
- Linked List: O(1) end insert/delete with pointers — queues, logs
- Stack/Queue/Deque: O(1) push/pop — undo/redo, BFS frontier
- Hash Map/Set: O(1) avg lookup/insert — caches, de-dup, joins
- Heap/Priority Queue: O(log n) push/pop — scheduling, top-k
- Tree/BST (balanced): O(log n) search/insert — ordered queries, ranges
- Graph: adj list vs matrix — traversal, routing, dependencies

---

## Patterns at a Glance

- Two Pointers: pairs, dedupe in sorted arrays — O(n)
- Sliding Window: longest/shortest substring/window — O(n)
- Hashing: frequency maps, seen sets, anagrams — O(n)
- Binary Search: sorted data or answer space — O(log n)
- BFS/DFS: traverse/shortest path (unweighted) — O(V+E)
- DP (memo/tab): overlapping subproblems — O(states)
- Greedy: local choice works globally (prove/explain)

---

## DP Primer (memo vs tab)

- When: overlapping subproblems + optimal substructure
- Memoization (top‑down): recursive + cache; easy to write
- Tabulation (bottom‑up): iterative; better control of order/space
- Transitions: define state, base cases, recurrence, order
- Tip: beware exponential recursion without memo

---

## Binary Search on Answer Space

- Works when “feasibility” is monotonic (true/false as x grows)
- Pick low/high bounds; mid = (low+high)//2; test predicate(mid)
- Examples: min capacity to ship in D days; min speed to eat bananas
- Complexity: O(log range × check_cost)

---

## Edge-Case Bank (use for any challenge)

- Empty/min sizes; capacity=1; all duplicates; negatives/zeros
- Sorted and reverse-sorted; long runs; alternating patterns
- Off-by-one boundaries (start/end blocked, first/last index)
- Invalid/exception paths (empty stack ops, missing sums)

---

## Python Pitfalls (quick)

- Mutable default args: avoid []/{} as defaults
- Shallow vs deep copy: list(x) vs copy.deepcopy(x)
- Integer division: // vs / (beware truncation)
- Hashability: dict/set keys must be immutable

---

## Complexity Cheatsheet (common ops)

- Hash map/set: O(1) avg insert/lookup; worst-case O(n)
- Stack/queue: O(1) push/pop
- BFS on grid: O(mn) time, O(mn) space
- LRU (hash + dll): O(1) per get/put; O(n) space

---

## Prompt patterns for DSA (local LLM)

- Tests first: “Generate 6 edge‑case tests for [CHALLENGE]. Include capacity=1, updates, repeats.”
- Constrain: “O(n) time, O(1) extra space if possible; no sorting for hash path.”
- Fix failures: “Given this failing test, propose a minimal diff.”
- Explain: “Summarize complexity and a real‑world usage in 5 lines.”

## Programming Challenge — LRU Cache

- API: `get(key) -> int` (‑1 if missing), `put(key, value)`
- Goal: O(1) per op with HashMap + doubly‑linked list (or OrderedDict)
- Edge cases: capacity=1; overwrite existing; repeated gets; eviction order
- Output: tests green + short note: perf, typical use (caches, rate limits)

Signature
```python
class LRUCache:
    def __init__(self, capacity: int): ...
    def get(self, key: int) -> int: ...
    def put(self, key: int, value: int) -> None: ...
```

### Live Prompt — LRU Cache (copy/paste into Continue)
```text
You are a Python unit test generator.
Write 6 edge-case tests for LRUCache with API get(key)->int (-1 if missing) and put(key, value).
Cover: capacity=1, overwrite existing key, repeated gets (updates recency), eviction order.
Return unittest code with a TestCase named TestLRUCache only.
```

---

## Programming Challenge — Bracket Validator

- Input: string with (), {}, []
- Valid if brackets are balanced and properly nested
- Edge cases: empty, single char, ")(", nested mixed types
- Output: tests green + note on stack operations and O(n)

Signature
```python
def is_valid_brackets(s: str) -> bool: ...
```

### Live Prompt — Bracket Validator
```text
Write 6 unit tests for is_valid_brackets(s: str) -> bool.
Include: empty string, single char, ")(", mixed nested valid, cross-nesting invalid, long balanced.
Output Python unittest code defining TestBrackets only.
```

---

## Programming Challenge — Two Sum (and variants)

- Input: nums + target; return indices i,j (i<j) so nums[i]+nums[j]=target
- Hash map O(n) vs sorted two‑pointers O(n log n)
- Variant: stream mode (yield index pairs online)
- Output: tests green + note on collisions and stability

Signature
```python
def two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None: ...
```

### Live Prompt — Two Sum
```text
Write unit tests for two_sum_indices(nums: list[int], target: int) -> tuple[int,int] | None.
Include: multiple pairs (pick first valid indices order i<j), duplicates, negatives, no-solution -> None.
Output Python unittest code defining TestTwoSum only.
```

---

## Programming Challenge — Min Stack (O(1) min)

- API: `push(x)`, `pop()`, `top() -> int`, `get_min() -> int`
- Goal: O(1) for all ops using two stacks (values + mins) or pairs
- Edge cases: duplicates; negatives; long sequences; empty stack checks (raise)
- Output: tests green + note on space/time tradeoff

Signature
```python
class MinStack:
    def push(self, x: int) -> None: ...
    def pop(self) -> None: ...
    def top(self) -> int: ...
    def get_min(self) -> int: ...
```

### Live Prompt — Min Stack
```text
Write unit tests for MinStack with push, pop, top, get_min (all O(1)).
Include: duplicates, negatives, min updates after pops, and IndexError on pop/top/get_min when empty.
Output Python unittest code defining TestMinStack only.
```

---

## Programming Challenge — Grid Shortest Path (BFS)

- Grid: 0 = free, 1 = wall; moves: 4‑dir
- Return shortest path length from (0,0) to (m‑1,n‑1), or ‑1
- Edge cases: blocked start/end; narrow corridors; multiple paths
- Output: tests green + note on queue/visited sets; O(mn)

Signature
```python
def shortest_path_len(grid: list[list[int]]) -> int: ...
```

### Live Prompt — Grid BFS
```text
Write unit tests for shortest_path_len(grid: list[list[int]]) -> int.
Include: simple 3x3 path length, blocked start, blocked end, no path, rectangular grid, tie paths choose shortest.
Output Python unittest code defining TestGridBFS only.
```

---

## Demo: Continue + Ollama

- Provider: Ollama; Model: llama3.2:3b‑instruct (or phi3:mini)
- Flow: write tests → run → implement → fix → summarize
- Tip: paste failing test + function signature, ask for a minimal diff

---

## Resources & Links

- Run tests: VS Code Task → "Session 2: Run Challenges (unittest)"
- Code & tests: `sessions/session02_dsa/content/challenges/`
- Prompts: see Quick Card and challenges README
- Python stdlib: `collections.deque`, `heapq`, `bisect`, `Counter`

---

## Wrap

- Commit: tests + code + README note on complexity and usage
- Keep your best prompts in your repo
- Optional stretch: micro‑bench the LRU and discuss O(1) average vs worst‑case
