import unittest
from arxivbot.utils import find_pattern_url_on_text, arxiv_abs_pattern, usual_url_pattern


class ArxivURLTest(unittest.TestCase):
    def setUp(self):
        self.text1 = '<p>Hello World</p><a href="http://example.com">More Examples</a><a href="http://example2.com">Even More Examples</a>'
        self.text2 = '4桁以上の数字 https://arxiv.org/abs/1710.10755 '

    def test_find_pattern_url(self):
        self.assertTrue(len(find_pattern_url_on_text(self.text1, usual_url_pattern())), 2)
        self.assertTrue(len(find_pattern_url_on_text(self.text2, arxiv_abs_pattern())), 1)
