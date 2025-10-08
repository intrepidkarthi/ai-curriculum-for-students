"""Simple HTML sanitizer using escaping (not a full sanitizer)."""
from __future__ import annotations
import html

def sanitize_html(s: str) -> str:
    return html.escape(s, quote=True)
