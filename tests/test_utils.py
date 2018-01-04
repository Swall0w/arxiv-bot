import unittest
from arxivbot.utils import find_pattern_url_on_text, arxiv_abs_pattern, usual_url_pattern
from arxivbot.utils import extract_arxiv_data


class ArxivURLTest(unittest.TestCase):
    def setUp(self):
        self.text1 = '<p>Hello World</p><a href="http://example.com">More Examples</a><a href="http://example2.com">Even More Examples</a>'
        self.text2 = '4桁以上の数字 https://arxiv.org/abs/1710.10755 '
        self.text3 = '面白そう arxiv.org/abs/1710.10755'
        self.url1 = 'https://arxiv.org/abs/1710.10755'

    def test_find_pattern_url(self):
        self.assertEqual(len(find_pattern_url_on_text(self.text1, usual_url_pattern())), 2)
        self.assertEqual(len(find_pattern_url_on_text(self.text2, arxiv_abs_pattern())), 1)
        self.assertEqual(len(find_pattern_url_on_text(self.text3, arxiv_abs_pattern())), 1)

    def test_extract_arxiv_data(self):
        self.assertTrue(isinstance(extract_arxiv_data([self.url1]), list))
