import nltk
from nltk.corpus import wordnet as wn

inFile = open("/Users/omer2/OneDrive/Documents/NLP/UTD_NLP/meetingFiles/text_web.txt", "r", encoding="utf8")

for line in inFile:
    print(line)


quit()
#d = wn.synset('bat.n.04')
allSyn = wn.synsets('bat')

for synset in allSyn:
    print('=' * 80)
    print(synset.definition())
    print(synset.lemmas())