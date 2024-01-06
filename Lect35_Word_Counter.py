import requests
from bs4 import BeautifulSoup
# import operator


def start(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    # for post_text in soup.find_all('span', {'itemprop': 'name'}):
    for post_text in soup.find_all('script', {'class': 'yoast-schema-graph'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(str(each_word))
            wordlist.append(each_word)


start('https://motoroctane.com/')
