from arxivbot.twitter import get_oauth
from tweepy.streaming import StreamListener, Stream
from datetime import timedelta
import configparser
from arxivbot.utils import (find_pattern_url_on_text,
                            usual_url_pattern,
                            extract_arxiv_data)
from arxivbot.github import create_github_issue


class AbstractedlyListener(StreamListener):
    def __init__(self, github_user):
        super(AbstractedlyListener, self).__init__()
        self.github_user = github_user

    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        print("{text}".format(text=status.text))
        print("{name}({screen}) {created} via {src}\n".format(
            name=status.author.name, screen=status.author.screen_name,
            created=status.created_at, src=status.source))
        urls = find_pattern_url_on_text(status.text, usual_url_pattern())
        if (status.author.screen_name == 'Swall0wTech') and urls:
            issues = extract_arxiv_data(urls)
            print(issues)
            for issue in issues:
                title = issue['title']
                body = "{}\n\n{}\n\n{}".format(
                    ', '.join(issue['authors']), issue['abstract'], issue['url'])
                labels = []
                is_created, content = create_github_issue(
                    self.github_user, title, body, labels)
                if is_created:
                    print('OK')
                    print(content)
                else:
                    print('Bad')
                    print(content)


def main():
    inifile = configparser.ConfigParser()
    inifile.read('./user.conf')
    init = {'consumer_key': inifile.get('twitter', 'consumer_key'),
            'consumer_secret': inifile.get('twitter', 'consumer_secret'), 
            'access_key': inifile.get('twitter', 'access_key'), 
            'access_secret': inifile.get('twitter', 'access_secret'), 
            }

    github_user = {'repo_owner': inifile.get('github', 'repo_owner'),
                   'repo_name': inifile.get('github', 'repo_name'), 
                   'username': inifile.get('github', 'username'), 
                   'password': inifile.get('github', 'password'), 
                   }

    auth = get_oauth(init)
    stream = Stream(auth, AbstractedlyListener(github_user=github_user), secure=True)
    stream.userstream()


if __name__ == '__main__':
    main()
