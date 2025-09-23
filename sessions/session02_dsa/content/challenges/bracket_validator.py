"""Bracket validator: return True if string has balanced (), {}, [] in order."""
from typing import List

def is_valid_brackets(s: str) -> bool:
    stack: List[str] = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            # ignore other chars (optional)
            continue
    return len(stack) == 0
