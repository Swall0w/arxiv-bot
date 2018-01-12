import unittest
import mock
from arxivbot.github import create_github_issue


class GithuhIssue(unittest.TestCase):
    def setUp(self):
        self.github_user = {
            'repo_owner': 'repo',
            'repo_name': 'arxiv-bot',
            'username': 'hoge',
            'password': 'fuga',
        }

    @mock.patch('requests.Session.post')
    def test_create_github_issue(self, session_mock):
        session_mock.return_value.status_code = 201
        session_mock.return_value.content = 'ok'

        title = 'title'
        body = 'content'

        self.assertEqual(
            create_github_issue(self.github_user, title)[0],
            True
        )

        self.assertEqual(
            create_github_issue(self.github_user, title, body)[0],
            True
        )

        session_mock.return_value.status_code = 404
        self.assertEqual(
            create_github_issue(self.github_user, title)[0],
            False
        )

        self.assertEqual(
            create_github_issue(self.github_user, title, body)[0],
            False
        )
