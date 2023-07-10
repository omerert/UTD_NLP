

#!python
################################################################################
#
#         FILE:
#           examples_07.py
#       AUTHOR:
#           Chris Irwin Davis, Ph.D.
#    COPYRIGHT:
#           (c)2023 The University of Texas at Dallas
#      LICENSE:
#           Academic Public License
#  DESCRIPTION:
#           Code examples associated with slide deck
#           "UTD Summer NLP Workshop - 07 - POS Tagging"
#
#           This program is an example of how to POS tag a sentence.
#           .
#   REFERENCES:
#           https://www.w3schools.com/python/python_regex.asp
# DEPENDENCIES:
#           Created with Python 3.10.11
#           Requires nltk package
#
################################################################################
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
porter = nltk.PorterStemmer()

def stem_and_tag(sent_str):
    sent_list = []
    tagged = nltk.pos_tag(word_tokenize(sent_str.lower()))
    for w in tagged:
        sent_list.append((w[0],w[1],porter.stem(w[0])))
    return sent_list

# print(stem_and_tag("The technologies weren't good."))
# print(stem_and_tag("The technologies were not good."))
# quit()

loop_counter = 0
max_sentences = 100

inFile = open("/Users/omer2/OneDrive/Documents/NLP/UTD_NLP/meetingFiles/text_web.txt","r", encoding="utf8")
inFileText = inFile.read()
inFileSentences = sent_tokenize(inFileText)



# word_token_list = word_tokenize(text)
# sent_tagged = nltk.pos_tag(word_token_list)

for sentence in inFileSentences:
    loop_counter += 1
    if loop_counter > max_sentences:
        break
    print('-' * 80)
    print(stem_and_tag(sentence))
    # for w in word_tokenize(sentence):
        # print(porter.stem(w)),
    print()



inFile.close()