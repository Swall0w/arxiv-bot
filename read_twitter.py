from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
from datetime import timedelta
import configparser


def get_oauth(init):
    # 以下4つのキー等は適宜取得して置き換えてください。
    consumer_key = init['consumer_key']
    consumer_secret = init['consumer_secret']
    access_key = init['access_key']
    access_secret = init['access_secret']
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth

class AbstractedlyListener(StreamListener):
    """ Let's stare abstractedly at the User Streams ! """
    def on_status(self, status):
        # Ubuntuの時は気づかなかったんだけど、Windowsで動作確認してたら
        # created_atはUTC（世界標準時）で返ってくるので日本時間にするために9時間プラスする。
        status.created_at += timedelta(hours=9)
        print("{text}".format(text=status.text))
        print("{name}({screen}) {created} via {src}\n".format(
            name=status.author.name, screen=status.author.screen_name,
            created=status.created_at, src=status.source))
        if status.author.screen_name == 'Swall0wTech':
            print('True: my tweet')

if __name__ == '__main__':
    inifile = configparser.ConfigParser()
    inifile.read('./user.conf')
    init = {'consumer_key': inifile.get('twitter', 'consumer_key'),
            'consumer_secret': inifile.get('twitter', 'consumer_secret'), 
            'access_key': inifile.get('twitter', 'access_key'), 
            'access_secret': inifile.get('twitter', 'access_secret'), 
            }
    auth = get_oauth(init)
    stream = Stream(auth, AbstractedlyListener(), secure=True)
    stream.userstream()
