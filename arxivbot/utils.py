import re


def find_pattern_url_on_text(text, pattern):
    urls = re.findall(pattern, text)
    return urls


def arxiv_abs_pattern():
    """ https://arxiv.org/abs/1710.10755 """
    return r'http[s]?://arxiv.org/abs/([a-zA-Z]|[0-9]|\.]).+'


def usual_url_pattern():
    return r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
