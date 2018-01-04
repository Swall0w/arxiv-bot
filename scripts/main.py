from arxivbot.twitter import get_oauth
from tweepy.streaming import StreamListener, Stream
from datetime import timedelta
import configparser


class AbstractedlyListener(StreamListener):
    """ Let's stare abstractedly at the User Streams ! """
    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        print("{text}".format(text=status.text))
        print("{name}({screen}) {created} via {src}\n".format(
            name=status.author.name, screen=status.author.screen_name,
            created=status.created_at, src=status.source))
        if status.author.screen_name == 'Swall0wTech':
            print('True: my tweet')


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
    stream = Stream(auth, AbstractedlyListener(), secure=True)
    stream.userstream()


    title = 'Spatial Transformer Networks'
    body = 'https://arxiv.org/abs/1506.02025' + '\n' + 'Convolutional Neural Networks define an exceptionally powerful class of models, but are still limited by the lack of ability to be spatially invariant to the input data in a computationally and parameter efficient manner. In this work we introduce a new learnable module, the Spatial Transformer, which explicitly allows the spatial manipulation of data within the network. This differentiable module can be inserted into existing convolutional architectures, giving neural networks the ability to actively spatially transform feature maps, conditional on the feature map itself, without any extra training supervision or modification to the optimisation process. We show that the use of spatial transformers results in models which learn invariance to translation, scale, rotation and more generic warping, resulting in state-of-the-art performance on several benchmarks, and for a number of classes of transformations.'
    labels = ['CNN']
    make_github_issue(github_user, title, body, labels)


if __name__ == '__main__':
    main()
