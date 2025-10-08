"""Password policy evaluator.
Checks length >= 12, upper/lower/digit/symbol, and common-password list.
Returns a dict of booleans, a score (0-5), and a brief tip.
"""
from __future__ import annotations
import string

COMMON_PASSWORDS = {
    "password",
    "123456",
    "123456789",
    "qwerty",
    "letmein",
    "admin",
    "iloveyou",
    "welcome",
    "monkey",
    "dragon",
}


def evaluate_password(p: str) -> dict:
    length_ok = len(p) >= 12
    has_upper = any(c.isupper() for c in p)
    has_lower = any(c.islower() for c in p)
    has_digit = any(c.isdigit() for c in p)
    has_symbol = any(c in string.punctuation for c in p)
    not_common = p.lower() not in COMMON_PASSWORDS

    score = sum([length_ok, has_upper, has_lower, has_digit, has_symbol])
    # Clamp score to 0..5 just in case
    score = max(0, min(5, score))

    missing = []
    if not length_ok:
        missing.append("length>=12")
    if not has_upper:
        missing.append("uppercase")
    if not has_lower:
        missing.append("lowercase")
    if not has_digit:
        missing.append("digit")
    if not has_symbol:
        missing.append("symbol")
    if not not_common:
        missing.append("not-common")

    tip = "Strong password." if not missing else (
        "Improve: " + ", ".join(missing)
    )

    return {
        "length_ok": length_ok,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "not_common": not_common,
        "score": score,
        "tip": tip,
    }
