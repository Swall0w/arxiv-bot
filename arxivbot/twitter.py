from tweepy.auth import OAuthHandler


def get_oauth(init):
    consumer_key = init['consumer_key']
    consumer_secret = init['consumer_secret']
    access_key = init['access_key']
    access_secret = init['access_secret']
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth
