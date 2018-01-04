from arxivbot.twitter import get_oauth, AbstractedlyListener
from tweepy.streaming import Stream
import configparser


def main():
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


if __name__ == '__main__':
    main()
