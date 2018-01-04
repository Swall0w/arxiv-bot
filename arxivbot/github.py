import os
import json
import requests


def create_github_issue(init, title, body="", labels=[]):
    """Create an issue on github.com using the given parameters."""

    # URL to create issues via POST
    url = 'https://api.github.com/repos/{}/{}/issues'.format(
        init['repo_owner'], init['repo_name'])
    session = requests.Session()
    session.auth = (init['username'], init['password'])

    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}

    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        return True, r.content
    else:
        return False, r.content
