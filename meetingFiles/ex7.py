################################################################################
#
#         FILE:
#           ex07b.py
#
#       AUTHOR:
#           Chris Irwin Davis, Ph.D.
#
#    COPYRIGHT:
#           (c)2023 The University of Texas at Dallas
#
#      LICENSE:
#           Academic Public License
#
#  DESCRIPTION:
#           This program demonstrates data mining from the website given a URL
#               using the 'requests' library.
#           Using Beautiful Soup ('bs4' library) to extract plain text from HTML
#           Tokenizing the plain text into word lists.
#
# EDIT HISTORY:
#           2023-07-05  Created during lecture
#
#   REFERENCES:
#           https://pypi.org/project/beautifulsoup4/
#
# DEPENDENCIES:
#           Created with Python 3.10.11
#           Package requirements:
#               NLTK
#                   Install with command line: pip install nltk
#               Regular Expression package
#                   Install with command line: pip install re
#               Requests package
#                   Install with command line: pip install requests
#               BeautifulSoup package bs4
#                   Install with command line: pip install beautifulsoup4
#
################################################################################
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
# We can see that the data type is <class 'nltk.stem.porter.PorterStemmer'>
print(type(porter)) # Uncomment to view


# Add a space after close tags in text to prevent
# undesired concatenation when tags are removed.
def add_space_between_tags(txt):
    return re.sub('>', '> ', str(txt))
# Reduce multiple whitespace with a single space
def kill_whitespace(txt):
    return re.sub(' +',' ',txt)

# Home made function to strip HTML tags out of a string.
# Replaces a regex pattern with an empty string ''.
# This is a naive implementation--it is susceptible to false positives/negatives.
def strip_tags(thing):
    # Ensure that 'thing' is a string data type via casting str(thing)
    return re.sub('<[^<]+?>', '', str(thing))

# Define a function that will display a pretty header line divider to the stdout
def divider(text,header_length=78):
    text = text.upper()
    text_length = len(text)
    bar = "=" * int((header_length - text_length)/ 2)
    div = ' '.join(['>',bar, "<" + text + ">",bar,'<'])
    print("div_length =",len(div))
    print(div)


###############################################################################
###############################################################################
###############################################################################


# For the benefit of hoomanz, display a header with "DALLAS NEWS" to the screen output
divider("dallas news")

# Set a URL string of the page you want to mine data from.
# url = "https://www.dallasnews.com/" # Dallas News Homepage

# A specific editorial article from 2023-07-05 about recycling peanut butter jars.
url = "https://www.dallasnews.com/opinion/editorials/2023/07/05/stop-putting-peanut-butter-in-your-recycling-bin-or-else/"


# Get a <request.Response> object from the URL string
respObj = requests.get(url)

# Get the html source code from the <request.Response> object as a UTF-8 encoded text string
# raw_html = respObj.text.encode("utf8") # encode("utf8") returns a byte sequence, not a string
raw_html = respObj.text # returns raw HTML from website as a string
#FIXME
raw_html = add_space_between_tags(raw_html)

print((raw_html))





# Convert the HTML source code from raw html into a <BeautifulSoup> object
# that represents the website's source code.
soupObj = BeautifulSoup(raw_html, "html.parser")

# Display the markup and enclosed text of the <title></title> tag 
divider('<title>')
print(soupObj.title)
# Same thing with HTML tags stripped out
print(strip_tags(soupObj.title))

# Display the markup and enclosed text of the <header></header> tag 
divider('header')
print(soupObj.header)
print("=" * 80)
print(strip_tags(soupObj.header))
print(kill_whitespace(strip_tags(soupObj.header)))

word_tokenize(kill_whitespace(strip_tags(soupObj.header)))

#x = pos_tag(word_tokenize(kill_whitespace(strip_tags(soupObj.header))))
#print(x)

# Ditto...
# divider('<body>')
# print(soupObj.body)

# Ditto...
# divider('all the body text')
divider('body body body')

divider('tokenized sentences')
sent_tokenized_body_text = sent_tokenize(soupObj.text)

for sentence in sent_tokenized_body_text:
    print('-' * 64)
    # remove extra spaces inserted by add_space_between_tags
    sentence = kill_whitespace(sentence)
    print(sentence)
    print(word_tokenize(sentence))
    tagged = nltk.pos_tag(word_tokenize(sentence.lower()))
    print(tagged)
    sent_list = []
    for w in tagged:
        sent_list.append((w[0],w[1],porter.stem(w[0])))
    print(sent_list)


quit() ###########################################################


header("sentence tokenized")
for sent in sent_tokenize(soupObj.text):
    print(sent)
quit()
header('new york times')

url = "http://www.nytimes.com"
respObj = requests.get(url)
# print(type(respObj))
raw_html = respObj.text.encode("utf8")
soupObj = BeautifulSoup(raw_html, "html.parser")
# for attribute in dir(soupObj):
    # print(attribute)

print(soupObj.title)
# remover = re.compile('<.*?>')
# print(re.sub(remover, '', soupObj.title))
# print(re.sub('<[^<]+?>', '', soupObj.title))
# x = BeautifulSoup(soupObj.title, 'html.parser')
# print(x.title)
# raw_html_text = respObj.text
#!python
# -*- coding: utf-8 -*-

import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
porter = nltk.PorterStemmer()
import urllib.request
from bs4 import BeautifulSoup
import requests




sent = "Now is the time for all good men to come to the aid of their country."
sent = word_tokenize(sent)
print(sent)
delimiter = ' '
out = delimiter.join(sent)
print(out)








# import sklearn
# print()

