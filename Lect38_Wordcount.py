import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    # for post_text in soup.find_all('span', {'itemprop': 'name'}):
    for post_text in soup.find_all('script', {'class': 'yoast-schema-graph'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            wordlist.append(each_word)
        clean_up_list(wordlist)


def clean_up_list(wordlist):
    clean_words_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_+{}:\"<>?,.//\\;'-[]-='"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            clean_words_list.append(word)
    create_dictionary(clean_words_list)

def create_dictionary(clean_words_list):
    word_count = {}
    for word in clean_words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key= operator.itemgetter(1)):
        print(key, value)


start('https://motoroctane.com/')