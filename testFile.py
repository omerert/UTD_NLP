from nltk import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet as wn

print(wn.synsets('airstrike'))
quit()
sentence = "Noah is an actor and he is enrolling for a leadership position"
ts = word_tokenize(sentence)
for i in pos_tag(ts[1:]):
    print(i)

quit()
import nltk
from nltk.corpus import wordnet as wn

text = "actor And now for something completely different"
t = nltk.word_tokenize(text)
tagged = nltk.pos_tag(t)
print(tagged) 


quit() ################################################################################################################
inFile = open("/Users/omer2/OneDrive/Documents/NLP/UTD_NLP/meetingFiles/text_web.txt", "r", encoding="utf8")
outFile = open("output.txt", "w")

plainText = inFile.read()

sentences = nltk.sent_tokenize(plainText)
count = 0
for line in sentences:
    if count > 10:
        break
    print(line)
    outFile.write(line)
    count += 1