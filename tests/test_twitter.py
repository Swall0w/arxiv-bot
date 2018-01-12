import unittest
import mock
from arxivbot.twitter import get_oauth
import tweepy


class TwitterTest(unittest.TestCase):
    def setUp(self):
        self.tweet = {
            'consumer_key': 'hoge',
            'consumer_secret': 'fuga',
            'access_key': 'bar',
            'access_secret': 'bar-secret',
        }

    def test_get_oauth(self):

        self.assertEqual(
            type(get_oauth(self.tweet)),
            tweepy.auth.OAuthHandler
        )
