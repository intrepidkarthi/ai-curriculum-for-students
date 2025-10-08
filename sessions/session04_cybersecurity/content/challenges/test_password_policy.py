import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from password_policy import evaluate_password

class TestPasswordPolicy(unittest.TestCase):
    def test_strong_password(self):
        res = evaluate_password("Abcd1234!@#$xyz")
        self.assertTrue(res["length_ok"]) 
        self.assertTrue(res["has_upper"]) 
        self.assertTrue(res["has_lower"]) 
        self.assertTrue(res["has_digit"]) 
        self.assertTrue(res["has_symbol"]) 
        self.assertTrue(res["not_common"]) 
        self.assertGreaterEqual(res["score"], 4)

    def test_common_short_weak(self):
        res = evaluate_password("password")
        self.assertFalse(res["length_ok"]) 
        self.assertFalse(res["has_digit"]) 
        self.assertFalse(res["has_symbol"]) 
        self.assertFalse(res["not_common"]) 
        self.assertLessEqual(res["score"], 3)

    def test_long_but_simple(self):
        res = evaluate_password("aaaaaaaaaaaa")
        self.assertTrue(res["length_ok"]) 
        self.assertFalse(res["has_upper"]) 
        self.assertFalse(res["has_digit"]) 
        self.assertFalse(res["has_symbol"]) 

if __name__ == '__main__':
    unittest.main()
