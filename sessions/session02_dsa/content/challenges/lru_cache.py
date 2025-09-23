"""LRU Cache skeleton.
Implement LRUCache with O(1) get/put using HashMap + doubly-linked list.
Fill in methods below. Keep API stable for tests.
"""
from __future__ import annotations
from typing import Optional


class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.cap = capacity
        self.map: dict[int, Node] = {}
        # Dummy head/tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front(self, node: Node) -> None:
        # insert right after head
        nxt = self.head.next
        assert nxt is not None
        node.prev = self.head
        node.next = nxt
        self.head.next = node
        nxt.prev = node

    def _remove(self, node: Node) -> None:
        p = node.prev
        n = node.next
        assert p is not None and n is not None
        p.next = n
        n.prev = p
        node.prev = node.next = None

    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._add_front(node)

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node:
            node.val = value
            self._move_to_front(node)
            return
        # new
        node = Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) > self.cap:
            # evict LRU = node before tail
            lru = self.tail.prev
            assert lru is not None and lru is not self.head
            self._remove(lru)
            del self.map[lru.key]
