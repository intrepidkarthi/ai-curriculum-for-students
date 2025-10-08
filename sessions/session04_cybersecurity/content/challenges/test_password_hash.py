import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from password_hash import hash_password, verify_password

class TestPasswordHash(unittest.TestCase):
    def test_hash_and_verify(self):
        salt_hex, hash_hex = hash_password("secret123!")
        self.assertTrue(verify_password("secret123!", salt_hex, hash_hex))
        self.assertFalse(verify_password("wrong", salt_hex, hash_hex))

    def test_different_salts(self):
        s1, h1 = hash_password("abcDEF123!@#")
        s2, h2 = hash_password("abcDEF123!@#")
        self.assertNotEqual(s1, s2)
        self.assertNotEqual(h1, h2)

if __name__ == '__main__':
    unittest.main()
