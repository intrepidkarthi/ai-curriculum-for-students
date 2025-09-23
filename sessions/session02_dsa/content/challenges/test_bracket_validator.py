import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from bracket_validator import is_valid_brackets

class TestBrackets(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(is_valid_brackets("()"))
        self.assertTrue(is_valid_brackets("([]){}"))
        self.assertFalse(is_valid_brackets("([)]"))
        self.assertFalse(is_valid_brackets(")("))
        self.assertTrue(is_valid_brackets(""))

if __name__ == '__main__':
    unittest.main()
