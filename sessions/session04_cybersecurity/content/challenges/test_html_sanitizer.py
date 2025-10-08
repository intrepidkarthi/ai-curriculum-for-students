import os, sys; sys.path.append(os.path.dirname(__file__))
import unittest
from html_sanitizer import sanitize_html

class TestHTMLSanitizer(unittest.TestCase):
    def test_script_tag(self):
        s = '<script>alert("x")</script>'
        out = sanitize_html(s)
        self.assertNotIn('<', out)
        self.assertIn('&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;', out)

    def test_amp_and_quotes(self):
        s = 'Tom & Jerry "show"'
        out = sanitize_html(s)
        self.assertIn('Tom &amp; Jerry &quot;show&quot;', out)

if __name__ == '__main__':
    unittest.main()
