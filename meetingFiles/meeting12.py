import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import urllib.request
import requests
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn
from nltk import FreqDist

def header(text,header_length=78):
    text = text.upper()
    text_length = len(text)
    bar = "=" * int((header_length - text_length)/ 2)
    div = ' '.join(['>',bar, "<" + text + ">",bar,'<'])
   
    print(div)

def add_space_bw_tags(htmlText):
    return re.sub(">", "> ", str(htmlText))

def kill_whitespace(txt):
    return re.sub(' +',' ',txt)
text = "This is going to be a long sencence and it will contain a lot of words."

url = "https://www.dallasnews.com"
htmlText = (requests.get(url)).text
soupObj = BeautifulSoup(htmlText, "html.parser")
htmlText = soupObj.text

htmlText = add_space_bw_tags(htmlText)

#print(htmlText)
soupObj = BeautifulSoup(htmlText, "html.parser")

sents = sent_tokenize(kill_whitespace(soupObj.text))

text = word_tokenize(htmlText)



header("ADD SPACE BETWEEN TAG")
print(len(text))

fdObj = FreqDist(text)
print(fdObj.keys)
header("FreqDist")

for key in fdObj.keys():
    print(key, fdObj[key])











quit()
htmlText = add_space_bw_tags(htmlText)

print(htmlText)
soupObj = BeautifulSoup(htmlText, "html.parser")

sents = sent_tokenize(kill_whitespace(soupObj.text))
for sent in sents:
    print(sent)
    #words = word_tokenize(sent)
    #print(words)