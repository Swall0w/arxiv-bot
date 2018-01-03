import os
import json
import requests
import configparser


def make_github_issue(init, title, body=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues'.format(
        init['repo_owner'], init['repo_name')
    session = requests.Session()
    session.auth = (init['username'], init['password'])
    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue {0:s}'.format(title))
    else:
        print ('Could not create Issue {0:s}'.format(title))
        print ('Response:', r.content)

def main():
    inifile = configparser.ConfigParser()
    inifile.read('./user.conf')
    init = {'repo_owner': inifile.get('github', 'repo_owner'),
            'repo_name': inifile.get('github', 'repo_name'), 
            'username': inifile.get('github', 'username'), 
            'password': inifile.get('github', 'password'), 
            }

    title = 'Spatial Transformer Networks'
    body = 'https://arxiv.org/abs/1506.02025' + '\n' + 'Convolutional Neural Networks define an exceptionally powerful class of models, but are still limited by the lack of ability to be spatially invariant to the input data in a computationally and parameter efficient manner. In this work we introduce a new learnable module, the Spatial Transformer, which explicitly allows the spatial manipulation of data within the network. This differentiable module can be inserted into existing convolutional architectures, giving neural networks the ability to actively spatially transform feature maps, conditional on the feature map itself, without any extra training supervision or modification to the optimisation process. We show that the use of spatial transformers results in models which learn invariance to translation, scale, rotation and more generic warping, resulting in state-of-the-art performance on several benchmarks, and for a number of classes of transformations.'
    labels = ['CNN']
    make_github_issue(init, title, body, labels)

if __name__ == '__main__':
    main()
