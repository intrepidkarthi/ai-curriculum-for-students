# Session 04 — Security Programming Challenges (stdlib-only)

How to run tests
- VS Code: Terminal → Run Task → "Session 4: Run Challenges (unittest)"
- CLI: `python -m unittest discover -s sessions/session04_cybersecurity/content/challenges -p 'test_*.py' -v`

Copy-ready prompts (paste into Continue)
- Phishing analysis (text): "Analyze this email and URLs for phishing indicators; return bullets + a short report to IT."
- Password policy (draft): "Draft a 1‑page campus password policy with examples of strong/weak passwords."
- Password policy evaluator (code): "Implement evaluate_password(p: str) -> dict with length>=12, upper/lower/digit/symbol, common‑password check; return dict of booleans + score and a tip."
- Phishing URL heuristics (code): "Implement is_suspicious_url(url: str) -> bool using heuristics: IP literal, many dots, '@', punycode 'xn--', odd TLD."
- HTML sanitizer (code): "Implement sanitize_html(s: str) -> str using html.escape(quote=True)."
- Password hash (code): "Implement pbkdf2_hmac('sha256') helpers: hash_password and verify_password with random 16‑byte salt."
