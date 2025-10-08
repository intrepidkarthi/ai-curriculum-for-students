---
marp: true
paginate: true
class: lead
---

# Cybersecurity & Ethical Hacking (AI‑assisted)

Practical security basics with local LLM help (Ollama + Continue)

---

## Today’s Plan (60m)

- Threat landscape (5m)
- Security basics: MFA, hashing vs encryption, least privilege (10m)
- Programming challenges (pick 2): Password Policy, Phishing URL, HTML Sanitizer, Password Hash (25m)
- Live with Continue + Ollama: analyze → generate → minimal diff (15m)
- Wrap + homework (5m)

---

## Threat Overview (student edition)

- Phishing/social engineering: look‑alike domains, urgency, attachments
- Weak passwords/reuse: credential stuffing
- Insecure code: string SQL, unsanitized HTML, unsafe eval/subprocess
- Missing MFA / poor secrets handling

---

## Incident Examples (quick, relatable)

- Ransomware (WannaCry/LockBit): encrypts files → backups + patching + least privilege matter
- Supply chain (SolarWinds / npm typosquatting): trusted deps compromised → pin versions, verify publishers
- Cloud misconfig (open S3/public buckets): accidental data exposure → least privilege + IaC checks
- Credential stuffing: reused passwords → MFA and rate limiting
- Secrets in repos/CI logs: API tokens committed → secret scans + env vars
- LLM prompt injection: user content manipulates tools → sanitization, allowlists, sandboxing

---

## Campus/Student scenarios

- Student portal phishing: look‑alike domains; QR code phishing on posters
- Public Wi‑Fi risks: captive portals, MITM → prefer HTTPS/VPN
- Group project repos: accidental public with .env keys → rotate secrets, .gitignore
- USB drops/social engineering: unknown devices → policy and training
- MFA fatigue: spam approvals → number matching, FIDO/passkeys

---

## AI‑based Cyber Threats (near future)

- Hyper‑targeted spear‑phishing at scale (LLM‑written, context‑aware)
- Real‑time deepfake voice/video for vishing and executive spoofing
- Autonomous fraud/recon agents chaining tools (email/drive/calendar)
- Adaptive malware that rewrites itself to evade pattern‑based detections
- Prompt‑injection supply chain (malicious web/RAG sources tainting tools)
- Data poisoning of public content used in retrieval/training
- Synthetic identity farms (AI‑generated KYC docs, profiles)
- Adversarial media (QR codes, images) that exploit scanners/models

---

## AI on Campus: likely scenarios soon

- Deepfake dean/HR calls to release data or approve payments
- AI chatbots answering helpdesk forms leak secrets via prompt injection
- Scholarship/loan fraud with synthetic students and forged transcripts
- Mass plagiarism/contract cheating with AI writing that evades basic checks
- Model/API key leaks through student repos and classroom demos
- RAG apps pulling poisoned pages from campus wikis or forums

---

## Defenses vs AI threats (what helps)

- Strong auth: FIDO/passkeys; number matching; block SMS fallback
- Out-of-band verify: callback policy for voice requests; shared passphrase for finance
- Content provenance: require source allowlists for RAG; pin domains; log citations
- Prompt hygiene: strict tool allowlist; sanitize inputs; strip HTML/JS; escape outputs
- Secrets discipline: secret scanning in CI; env vars; rotate keys; least-privileged tokens
- Rate limits and anomaly detection: throttle auth attempts; alert on behavior spikes
- Media defenses: train on deepfake cues; require video callbacks for high-risk actions
- Student repos: enforce .gitignore; disallow committing .env; teach revocation/rotation

---

## Case Study — Deepfake vishing playbook

- Vector: voice call claims to be CFO/Dean; urgent payment/data request
- Impact: unauthorized transfers, data exfiltration, reputational damage
- Mitigations:
  - Callback policy: hang up and call back on a known official number
  - Shared passphrase/code word for finance/HR approvals
  - Dual approval for high‑risk actions; no OTP over voice
  - Log/report attempts to IT; keep short audio clip as evidence
- Tell‑tales: slight latency, odd phrasing/timbre, refuses callback

---

## Checklist — If you suspect phishing

- Stop: do not click, approve, or enter passwords/OTP
- Verify out‑of‑band (phone a known number, new email thread)
- Capture evidence: headers, full URL, screenshot, caller ID
- Report: forward to security/IT; mark as phishing in mail client
- Remediate: change password, confirm MFA, review recent logins
- Devices: run AV scan; update OS/browser; clear saved sessions
- Voice: hang up; call back official line; never disclose MFA/OTP

---

## Security Basics (quick)

- MFA: something you know/are/have; phishing‑resistant (FIDO/Passkeys)
- Hashing ≠ encryption: one‑way (pbkdf2/bcrypt/argon2) vs reversible
- Transport: HTTPS/TLS; do not send secrets over HTTP
- Principle of least privilege; rotate and scope tokens

---

## Live with Continue + Ollama

- Use small local models for fast loops (phi3:mini) or balanced (llama3.2)
- Flow: paste problem → generate code/tests → run → minimal diff
- Keep prompts short; add concrete examples from edge‑case bank

---

## Copy‑ready prompts — Phishing analysis

```text
You are a security analyst. Analyze this email text and URL list for phishing indicators.
Highlight look‑alike domains, urgency language, mismatched links, attachments.
Return bullet points and a short “report to IT” paragraph.
```

---

## Copy‑ready prompts — Password policy

```text
Draft a campus password policy for students: length, complexity, rotation, MFA, and exceptions.
Keep it one page. Include 5 concrete examples of strong passwords and 5 weak ones (and why).
```

---

## Programming Challenges (choose 2)

- Password Policy Evaluator (pure Python)
- Phishing URL Heuristics (stdlib only)
- HTML Sanitizer (escape dangerous characters)
- Password Hash (pbkdf2_hmac)

---

## Challenge — Password Policy Evaluator

- Function: `evaluate_password(p: str) -> dict`
- Checks: length ≥ 12, upper/lower/digit/symbol, not common
- Output: dict with booleans + score (0–5) and a brief tip
- Tests: strong/weak, edge cases (only digits, long but simple)

Signature
```python
def evaluate_password(p: str) -> dict: ...
```

---

## Challenge — Phishing URL Heuristics

- Function: `is_suspicious_url(url: str) -> bool`
- Heuristics: IP literal, many dots, '@' in URL, punycode (xn--), odd TLD
- Tests: legit campus domain vs look‑alike, IP links, URL with '@'

Signature
```python
def is_suspicious_url(url: str) -> bool: ...
```

---

## Challenge — HTML Sanitizer

- Function: `sanitize_html(s: str) -> str`
- Approach: escape <, >, &, quotes (html.escape)
- Tests: `<script>`, onerror attributes, mixed text

Signature
```python
def sanitize_html(s: str) -> str: ...
```

---

## Challenge — Password Hash (pbkdf2)

- Functions: `hash_password(p: str, salt: bytes|None=None) -> tuple[salt_hex, hash_hex]`
  and `verify_password(p: str, salt_hex: str, hash_hex: str) -> bool`
- Use stdlib: `hashlib.pbkdf2_hmac('sha256', ...)`, random 16‑byte salt
- Tests: verify true/false, different salts for same password

---

## Edge‑Case Bank (security)

- Unicode: accents, homoglyphs ("rn" vs "m"), punycode `xn--`
- Zero‑width spaces, long repeats, all digits/letters only
- Mixed scripts (Latin + Cyrillic) in URLs/usernames

---

## Python Pitfalls (security)

- Avoid `eval`, `exec`; avoid `subprocess` with `shell=True`
- Never string‑concatenate SQL; prefer parameterized queries
- Don’t log secrets; use environment variables for config
- Always escape HTML; sanitize/validate inputs

---

## Resources & Links

- Run tests: VS Code Task → "Session 4: Run Challenges (unittest)"
- Code & tests: `sessions/session04_cybersecurity/content/challenges/`
- Local models: see `LOCAL_AI_SETUP.md`
- Reading: OWASP Top 10 (web), NCSC password guidance

---

## Wrap

- Practiced practical security with LLM support
- Next: add static analysis (ruff/semgrep) and secrets scanning to CI
