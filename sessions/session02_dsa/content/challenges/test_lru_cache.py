import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_basic_put_get(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        self.assertEqual(c.get(1), 1)
        c.put(3, 3)  # evicts key 2
        self.assertEqual(c.get(2), -1)
        c.put(4, 4)  # evicts key 1
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(3), 3)
        self.assertEqual(c.get(4), 4)

    def test_capacity_one(self):
        c = LRUCache(1)
        c.put(10, 10)
        self.assertEqual(c.get(10), 10)
        c.put(11, 11)  # evict 10
        self.assertEqual(c.get(10), -1)
        self.assertEqual(c.get(11), 11)

    def test_update_existing(self):
        c = LRUCache(2)
        c.put(5, 5)
        c.put(5, 7)
        self.assertEqual(c.get(5), 7)
        c.put(6, 6)
        c.put(7, 7)  # evict LRU (which should be 6)
        self.assertEqual(c.get(6), -1)

if __name__ == '__main__':
    unittest.main()
