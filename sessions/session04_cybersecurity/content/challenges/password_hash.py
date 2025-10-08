"""Password hashing helpers using PBKDF2 (stdlib only)."""
from __future__ import annotations
import os
import binascii
import hashlib
import hmac

ITERATIONS = 100_000
SALT_BYTES = 16


def hash_password(p: str, salt: bytes | None = None) -> tuple[str, str]:
    if salt is None:
        salt = os.urandom(SALT_BYTES)
    dk = hashlib.pbkdf2_hmac('sha256', p.encode('utf-8'), salt, ITERATIONS)
    return binascii.hexlify(salt).decode(), binascii.hexlify(dk).decode()


def verify_password(p: str, salt_hex: str, hash_hex: str) -> bool:
    try:
        salt = binascii.unhexlify(salt_hex)
        expected = binascii.unhexlify(hash_hex)
    except binascii.Error:
        return False
    dk = hashlib.pbkdf2_hmac('sha256', p.encode('utf-8'), salt, ITERATIONS)
    return hmac.compare_digest(dk, expected)
