import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
porter = nltk.PorterStemmer
import urllib.request
import requests
from bs4 import BeautifulStoneSoup
from nltk import FreqDist

bigrams = nltk.bigrams




with open("/Users/omer2/OneDrive/Documents/NLP/UTD_NLP/meetingFiles/text_web.txt", "r", encoding="utf8") as fileObj:
    web_text = fileObj.read()
    words = word_tokenize(web_text)
    fd = FreqDist(words)
    bigs = bigrams(words)
    count = 0
    ct = 0
    max = 1000

    frequency = FreqDist(bigs)
    for key, value in frequency.items():
        if (key[0] == 'President'):
            print(key[0],key[1], value)
        ct += 1
        if (ct > max):
            break
    for b in bigs:
        print(b)
        count += 1
        if count > max:
            break
    print('President', fd['President'])
    #print(fd['Microbiology'])
    # print(fd.values())

    # for tuple in fd.items():
    #     if(tuple[1] > 10):
    #         print(tuple)
quit()
x = nltk.FreqDist(['a', 'b', 'c', 'a', 'b'])

for item, num in x.items():
    print(item, num)