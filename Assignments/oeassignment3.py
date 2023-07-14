#################################################################################
#         FILE:
#           oeassignment3.py
#       AUTHOR:
#           Omer Erturk
#  DESCRIPTION:
#           Assignment 3
#           My program breaks down the source code of a website, gets text from the article, tokenizes it by sentences and words, and prints out the tokenized sentence as well as a tuple( the word, pos_tag, and stemmed) of each word. 
# DEPENDENCIES:
#           Created with Python 3.10.5 (Python version)
#           re, nltk, urllib.request, requests, bs4, wordnet
#################################################################################
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import urllib.request
import requests
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn
# Create a shortcut to Porter Stemmer
porter = nltk.PorterStemmer()
pos_tag = nltk.pos_tag


def strip_tags(thing):
    # Ensure that 'thing' is a string data type via casting str(thing)
    return re.sub('<[^<]+?>', '', str(thing))

url = "https://www.dallasnews.com/opinion/editorials/2023/07/09/loan-forgiveness-doesnt-address-cause-of-crushing-student-debt/"

#Gets source html

getRequest = requests.get(url)
htmlText = getRequest.text

#Using BS and strip_tags to get the text I want

soupText = BeautifulSoup(htmlText, 'html.parser')
wantedText = strip_tags(soupText.findAll("p", class_="body-text-paragraph"))


splitSent = wantedText.replace(".,", ".")
splitSent = splitSent.replace("[", "")
splitSent = splitSent.replace("]", "")

#Tokenizing by sentences
sentences = sent_tokenize(splitSent)

for sent in sentences:
    print("=" * 80)
    print(sent)
    words = word_tokenize(sent)
    tuple = []
    for word, tag in pos_tag(words):
        tuple.append(f"{word.lower()}, {tag}, {porter.stem(word)}")
    print(tuple)