import re
import urllib.request
import bs4


def find_pattern_url_on_text(text, pattern):
    urls = re.findall(pattern, text)
    return urls


def arxiv_abs_pattern():
    """ https://arxiv.org/abs/1710.10755 """
    return r'(http[s]?://|)arxiv.org/abs/([a-zA-Z]|[0-9]|\.]).+'


def usual_url_pattern():
    return r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def extract_arxiv_data(urls):
    pattern = re.compile(arxiv_abs_pattern(), re.X)
    arxiv_list = []
    for url in urls:
        response = urllib.request.urlopen(url)
        long_url = response.geturl()
        if pattern.match(long_url):
            ret = {}
            soup = bs4.BeautifulSoup(response.read(), "lxml")
            ret['title'] = soup.find('meta', attrs={'name': "citation_title"}).get("content")
            ret['url'] = long_url
            ret['authors'] = [item.get("content") for item in soup.find_all('meta', attrs={'name': "citation_author"})]
            ret['abstract'] = soup.find('blockquote').text.replace("\nAbstract: ", "")
            arxiv_list.append(ret)
        else:
            pass

    return arxiv_list
