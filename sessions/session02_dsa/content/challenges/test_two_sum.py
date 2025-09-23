import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from two_sum import two_sum_indices

class TestTwoSum(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(two_sum_indices([2,7,11,15], 9), (0,1))
        self.assertEqual(two_sum_indices([3,2,4], 6), (1,2))
        self.assertEqual(two_sum_indices([3,3], 6), (0,1))

    def test_none(self):
        self.assertIsNone(two_sum_indices([1,2,3], 7))

if __name__ == '__main__':
    unittest.main()
