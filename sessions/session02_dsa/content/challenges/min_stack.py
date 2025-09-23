"""Min Stack with O(1) get_min.
API: push(x), pop(), top() -> int, get_min() -> int
Raises IndexError on pop/top/get_min for empty stack.
"""
from __future__ import annotations
from typing import List


class MinStack:
    def __init__(self) -> None:
        self._vals: List[int] = []
        self._mins: List[int] = []

    def push(self, x: int) -> None:
        self._vals.append(x)
        if not self._mins or x <= self._mins[-1]:
            self._mins.append(x)

    def pop(self) -> None:
        if not self._vals:
            raise IndexError("pop from empty stack")
        v = self._vals.pop()
        if self._mins and v == self._mins[-1]:
            self._mins.pop()

    def top(self) -> int:
        if not self._vals:
            raise IndexError("top from empty stack")
        return self._vals[-1]

    def get_min(self) -> int:
        if not self._mins:
            raise IndexError("min from empty stack")
        return self._mins[-1]
