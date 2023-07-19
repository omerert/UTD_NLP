import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
porter = nltk.PorterStemmer()
import urllib.request
import requests
from bs4 import BeautifulSoup

def divider():
    print("=" * 80)

with open("ar_sentences.txt", "r") as sent_file:
    #sents = sent_tokenize(sent_file.read())
    words = word_tokenize(sent_file.read())
    bigs = nltk.bigrams(words)
    fd = dict(nltk.FreqDist(bigs))
    #fd.sort()
    for key, value in fd.items():
        print(key, value)
    quit()
    for b in bigs:
        print(b)
    # for sent in sents:
    #     print(sent)