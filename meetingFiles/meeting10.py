import re
import nltk
import requests
from nltk.tokenize import sent_tokenize, word_tokenize
import urllib.request
from bs4 import BeautifulSoup
import requests


sent = word_tokenize("Now is the time that all good men to come to the aid of their country.")
print(sent)
delimiter = '||'
out = delimiter.join(sent)
#print(out)
def header(text, header_length=78):
    text = text.upper()
    text_length = len(text)
    bar = '=' * (int(header_length / 2) - text_length)
    print(bar,text,bar,'\n')

header('new york times')

url = "https://www.dallasnews.com"
respObj = requests.get(url)
rawHTML = respObj.text.encode("utf8")
soupObj = BeautifulSoup(rawHTML, "html.parser")
#print(soupObj.text)
for sent in sent_tokenize(soupObj.text):
    print(sent)
