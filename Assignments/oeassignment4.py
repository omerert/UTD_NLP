################################################################################ 
# 
#         FILE: 
#           oeassignment4.py 
#       AUTHOR: 
#           Omer Erturk 
#  DESCRIPTION: 
#           Assignment 4 
#           Find the top 10 most frequent bigrams(not including link or referebce brackets) and prints them out
# DEPENDENCIES: 
#           Created with Python 3.10.5 (Python version) 
#           NlTK, urllib, bs4, requests
# 
################################################################################
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
porter = nltk.PorterStemmer()
import urllib.request
import requests
from bs4 import BeautifulSoup

fd = nltk.FreqDist
bg = nltk.bigrams

count = 0
# The link I want
url = "https://en.wikipedia.org/wiki/AI_takeover"

#Gets source html

getRequest = requests.get(url)
htmlText = getRequest.text

# Writing HTML source to .txt file
with open("aiTakeover.txt", "w", encoding="utf-8") as file:
    file.write(htmlText)

# Reading source file
with open('aiTakeover.txt', 'r', encoding="utf8") as text:
    #Using BS to get the text I want
    soupText = BeautifulSoup(text, 'html.parser')
    
    # Writing tokenized sentences to .txt
    with open('sentTakeover.txt', 'w', encoding='utf-8') as wText:
        paragraphs = soupText.findAll("p")
        for para in paragraphs:
            sentP = sent_tokenize(para.text.strip())
            # Iterate over each sentence
            for sent in sentP:
                wText.write(sent + "\n")
 
# Reading sent_tokeized .txt
with open("sentTakeover.txt", "r") as sent_file:
    words = word_tokenize(sent_file.read())
    # Creating a dictionary of bigrams with words and count
    bigs = bg(words)
    wordFreq = (fd(bigs))
    # Sorts the dictionary based on most frequent bigram
    sorted_dict = dict(sorted(wordFreq.items(), key=lambda item: item[1], reverse = True))
    # Displays top 10 most frequent bigrams
    for words, freq in sorted_dict.items():
        if "[" in words or "]" in words:
            continue
        count += 1
        if count > 10:
            break
        print(words, freq)
        

        