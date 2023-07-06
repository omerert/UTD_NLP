import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from datetime import date
from nltk.corpus import wordnet as wn
import re

#text = word_tokenize("And now for something completely different")
#tagged = nltk.pos_tag(text)

#print(tagged)



porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
raw = "Omer tis is some sample text and it is for testing purposes. This will be an alternative to the actual lines of raw text."
token = nltk.word_tokenize(raw)

def stemAndTag(sent_str):
    sent_list = []
    tagged = nltk.pos_tag(word_tokenize(sent_str.lower()))
    for w in tagged:
        sent_list.append((w[0],porter.stem(w[0]),w[1]))
    return sent_list
print(stemAndTag(token))
quit()
output = [(word.lower(), porter.stem(word)) for word in token]
for word in token:
    output += tuple()
print(output)
quit()
myword = "dancing"
sent = word_tokenize("John is going to dog that movie")
print( nltk.pos_tag(sent))
#stem = porter.stem(sent)

stems = [porter.stem(t) for t in token]
print(stems)
stems = [lancaster.stem(t) for t in token]
print(stems)

quit()
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