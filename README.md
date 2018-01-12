# arxiv-bot
This is a app creating a paper issue that we should read through my tweet.

[![Build Status](https://travis-ci.org/Swall0w/arxiv-bot.svg?branch=master)](https://travis-ci.org/Swall0w/arxiv-bot)
[![Maintainability](https://api.codeclimate.com/v1/badges/e0c7cedc44f1053568b2/maintainability)](https://codeclimate.com/github/Swall0w/arxiv-bot/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e0c7cedc44f1053568b2/test_coverage)](https://codeclimate.com/github/Swall0w/arxiv-bot/test_coverage)
[![codebeat badge](https://codebeat.co/badges/94385701-f326-4a65-9a50-c93233d2a5e2)](https://codebeat.co/projects/github-com-swall0w-arxiv-bot-master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1104e0c8081f44d4b281d7928f4e6e24)](https://www.codacy.com/app/technext.jpn/arxiv-bot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Swall0w/arxiv-bot&amp;utm_campaign=Badge_Grade)

# Demo
![demo-gif](./imgs/cap2.gif)

* Tweet or Retweet a message that contains URL of arxiv.
* This app creates an issue which includes the title, authors, abstract, URL to [this repository](https://github.com/Swall0w/papers) instead of you.

# Getting Started
These instuctions will get you how I deploy thie app for my repository.
If you want to deploy this for your repository and for your twitter account,
you need to set the configration file for them.

## Prerequisites
* Python 3.6.1 :: Anaconda custom (64-bit)
* tweepy
* beautifulsoup4
* lxml

## Installing
```
    git clone https://github.com/Swall0w/arxiv-bot
    make build
    make install
```

## Running the tests
```
    make test
```

## Deployment
Before you launch the script,
make sure that your configration file is correctly written like bellow,
Modify these parameter for your twitter account and github account.

```
    mv scripts/user.conf.bak scripts/user.conf
    cat scripts/user.conf

    [twitter]
    consumer_key = hoge
    consumer_secret = fuga
    access_key = bar
    access_secret = foo

    [github]
    repo_owner = repository_owner_name
    repo_name = repository_name
    username = your_github_name
    password = your_github_password

```

After setting the configration file, you launch the app.

```
    cd scripts
    python3 main.py
```

# Author
* Swall0w

# License
* MIT License
