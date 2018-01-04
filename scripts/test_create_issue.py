import configparser
from arxivbot.github import create_github_issue


def main():
    inifile = configparser.ConfigParser()
    inifile.read('./user.conf')

    github_user = {'repo_owner': inifile.get('github', 'repo_owner'),
                   'repo_name': 'arxiv-bot',
                   'username': inifile.get('github', 'username'), 
                   'password': inifile.get('github', 'password'), 
                   }
    title = 'Test create a issue'
    body = 'test'
    labels = ['wontfix']
    create_github_issue(github_user, title, body, labels)


if __name__ == '__main__':
    main()
