"""Phishing URL heuristics (simple stdlib-only checks)."""
from __future__ import annotations
import re
import ipaddress
from urllib.parse import urlsplit

SUSPICIOUS_TLDS = {
    "zip", "mov", "country", "work", "gq", "tk", "ml", "cf"
}

def _is_ip(host: str) -> bool:
    try:
        # strip IPv6 brackets
        host2 = host.strip("[]")
        ipaddress.ip_address(host2)
        return True
    except ValueError:
        return False


def is_suspicious_url(url: str) -> bool:
    try:
        parts = urlsplit(url)
    except Exception:
        return True
    host = parts.hostname or ""
    if not host:
        return True

    # Heuristic 1: IP literal host
    if _is_ip(host):
        return True

    # Heuristic 2: '@' anywhere in netloc/path
    if '@' in parts.netloc or '@' in parts.path:
        return True

    # Heuristic 3: punycode
    if 'xn--' in host:
        return True

    # Heuristic 4: too many subdomains
    if host.count('.') >= 4:
        return True

    # Heuristic 5: odd TLD
    m = re.search(r"\.([a-zA-Z0-9-]{2,})$", host)
    if m and m.group(1).lower() in SUSPICIOUS_TLDS:
        return True

    return False
