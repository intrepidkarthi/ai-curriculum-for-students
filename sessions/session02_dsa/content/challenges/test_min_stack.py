import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from min_stack import MinStack

class TestMinStack(unittest.TestCase):
    def test_push_pop_top_min(self):
        s = MinStack()
        s.push(3)
        s.push(5)
        self.assertEqual(s.get_min(), 3)
        s.push(2)
        s.push(2)
        self.assertEqual(s.get_min(), 2)
        self.assertEqual(s.top(), 2)
        s.pop()
        self.assertEqual(s.get_min(), 2)
        s.pop()
        self.assertEqual(s.get_min(), 3)
        self.assertEqual(s.top(), 5)
        s.pop()
        self.assertEqual(s.top(), 3)

    def test_errors_on_empty(self):
        s = MinStack()
        with self.assertRaises(IndexError):
            s.top()
        with self.assertRaises(IndexError):
            s.get_min()
        with self.assertRaises(IndexError):
            s.pop()

    def test_negatives_and_duplicates(self):
        s = MinStack()
        s.push(0)
        s.push(-1)
        s.push(-1)
        s.push(1)
        self.assertEqual(s.get_min(), -1)
        s.pop()
        self.assertEqual(s.get_min(), -1)
        s.pop()
        self.assertEqual(s.get_min(), -1)
        s.pop()
        self.assertEqual(s.get_min(), 0)

if __name__ == '__main__':
    unittest.main()
