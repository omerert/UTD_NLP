import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from datetime import date
import re

#text = word_tokenize("And now for something completely different")
#tagged = nltk.pos_tag(text)

#print(tagged)



sentToken = sent_tokenize(open("/Users/omer2/OneDrive/Documents/NLP/UTD_NLP/meetingFiles/text_web.txt", "r").read())

count = 0
maxSentences = 100
for sent in sentToken:
    sent = sent.lower()

    porter = nltk.PorterStemmer
    
    
    count += 1
    if count > maxSentences:
        break
    word_list = word_tokenize(sent)
    print(word_list)
    for w in word_list:
        stem = porter.stem(w)
        print(stem)
    break
    tagged = nltk.pos_tag(word_list)
    print("-" * 80)
    
    sent.replace("<.+>", "")
    print(tagged)