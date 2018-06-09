from arxivbot.twitter import get_oauth
from tweepy.streaming import StreamListener, Stream
from datetime import timedelta
import configparser
from arxivbot.utils import (find_pattern_url_on_text,
                            usual_url_pattern,
                            extract_arxiv_data)
from arxivbot.github import create_github_issue
import traceback


class AbstractedlyListener(StreamListener):
    def __init__(self, github_user):
        super(AbstractedlyListener, self).__init__()
        self.github_user = github_user

    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        urls = find_pattern_url_on_text(status.text, usual_url_pattern())
        if (status.author.screen_name == 'Swall0wTech') and urls:
            try:
                issues = extract_arxiv_data(urls)
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
            except:
                error = traceback.format_exc()
                print(error)


    def _run(self):
        # Authenticate
        url = "https://%s%s" % (self.host, self.url)
        # Connect and process the stream
        error_counter = 0
        resp = None
        exception = None
        while self.running:
            if self.retry_count is not None:
                if error_counter > self.retry_count:
                    # quit if error count greater than retry count
                    break
            try:
                auth = self.auth.apply_auth()
                resp = self.session.request('POST',
                                            url,
                                            data=self.body,
                                            timeout=self.timeout,
                                            stream=True,
                                            auth=auth,
                                            verify=self.verify)
                if resp.status_code != 200:
                    if self.listener.on_error(resp.status_code) is False:
                        break
                    error_counter += 1
                    if resp.status_code == 420:
                        self.retry_time = max(self.retry_420_start,
                                              self.retry_time)
                    sleep(self.retry_time)
                    self.retry_time = min(self.retry_time * 2,
                                          self.retry_time_cap)
                else:
                    error_counter = 0
                    self.retry_time = self.retry_time_start
                    self.snooze_time = self.snooze_time_step
                    self.listener.on_connect()
                    self._read_loop(resp)

            except (Timeout, ssl.SSLError) as exc:
                # This is still necessary, as a SSLError can actually be
                # thrown when using Requests
                # If it's not time out treat it like any other exception
                if isinstance(exc, ssl.SSLError):
                    if not (exc.args and 'timed out' in str(exc.args[0])):
                        exception = exc
                        break
                if self.listener.on_timeout() is False:
                    break
                if self.running is False:
                    break
                sleep(self.snooze_time)
                self.snooze_time = min(self.snooze_time + self.snooze_time_step,
                                       self.snooze_time_cap)
            except Exception as exc:
                exception = exc
                # any other exception is fatal, so kill loop
                break

        # cleanup
        self.running = False
        if resp:
            resp.close()

        self.new_session()

        if exception:
            # call a handler first so that the exception can be logged.
            self.listener.on_exception(exception)
            raise


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
