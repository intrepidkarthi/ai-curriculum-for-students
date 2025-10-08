import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from phishing_url import is_suspicious_url

class TestPhishingURL(unittest.TestCase):
    def test_legit(self):
        self.assertFalse(is_suspicious_url("https://www.tce.edu/login"))

    def test_ip_literal(self):
        self.assertTrue(is_suspicious_url("http://192.168.0.1/login"))

    def test_at_symbol(self):
        self.assertTrue(is_suspicious_url("http://examp1e.com@phish.com/"))

    def test_punycode(self):
        self.assertTrue(is_suspicious_url("http://xn--google-qmc.com"))

    def test_many_dots(self):
        self.assertTrue(is_suspicious_url("http://a.b.c.d.e.com"))

if __name__ == '__main__':
    unittest.main()
