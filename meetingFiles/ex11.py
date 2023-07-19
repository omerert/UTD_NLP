import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
porter = nltk.PorterStemmer()
import urllib.request
import requests
from bs4 import BeautifulSoup

# url = "https://en.wikipedia.org/wiki/American_Revolution"
# reqObj = requests.get(url)
# rawHTML = reqObj.text

# with open('civil_war.html', 'w', encoding='utf-8') as file:
#     file.write(rawHTML)
def divider():
    print("=" * 80)

with open('/Users/omer2/OneDrive/Documents/NLP/UTD_NLP/civil_war.html', 'r', encoding="utf8") as file:
    soupObj = BeautifulSoup(file.read(), "html.parser")
    text = soupObj.text
    # print(soupObj.find('title'))
    # print(soupObj.find('head').find_all('meta'))
    with open('ar_sentences.txt', 'w', encoding="utf-8") as sent_file:
        pList = soupObj.find_all('p')
        for p in pList:
            #divider()
            sentP = sent_tokenize(p.text.strip())
            for sent in sentP:
                #print(sent)
                sent_file.write(sent + "\n")
        