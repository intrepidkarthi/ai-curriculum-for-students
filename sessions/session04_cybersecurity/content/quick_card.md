# Quick Card — Session 04: Cybersecurity & Ethical Hacking (AI-assisted)

Duration: 60 min
Goal: Analyze phishing and craft password policy guidance; implement 1–2 security programming challenges.

Tools: Local LLM via Ollama + VS Code Continue for text analysis, policy drafting, and coding; unittest

Minute-by-minute
- 0–10: Threat overview
- 10–20: Security basics (MFA, hashing vs encryption, least privilege)
- 20–45: Programming challenges (choose 2): Password Policy, Phishing URL, HTML Sanitizer, Password Hash
- 45–55: Live with Continue + Ollama (analyze → generate → minimal diff)
- 55–60: Wrap + homework

Artifact
- Short analysis write-up (phishing features + password policy) + tested code snippets

Homework
- Find a phishing example; write mitigations with LLM help
- Optional: add a secrets scan or static analysis step to CI

Copy-ready prompts (paste into Continue)
- Phishing analysis: "Analyze this email/URLs for phishing indicators; return bullets + an IT report paragraph."
- Password policy: "Draft a 1‑page campus password policy with strong/weak examples."
- Password evaluator (code): "Implement evaluate_password(p: str) -> dict with length>=12, upper/lower/digit/symbol, common-password check; return booleans + score + tip."
- Phishing URL (code): "Implement is_suspicious_url(url: str) -> bool; heuristics: IP, '@', 'xn--', many dots, odd TLD."
- HTML sanitizer (code): "Implement sanitize_html(s: str) -> str using html.escape(quote=True)."
- Password hash (code): "Implement pbkdf2 helpers hash_password/verify_password with random 16-byte salt."
