import nltk
#from nltk.corpus import brown
from nltk.corpus import wordnet as wn
count = 0


catSyns = wn.synset('vertebrate.n.01')
#print(dir(catSyns))
print(catSyns.hypernyms())

brown = nltk.corpus.brown
cats = brown.categories()

#FIXME: Locate proper syntax for root()
#root = nltk.corpus.gutenberg.root
#nltk.download()

#fileNames = nltk.corpus.gutenberg.fileids()
#for title in fileNames:
#    print(title)

#text = nltk.corpus.gutenberg.sents("shakespeare-caesar.txt")
#text = nltk.corpus.gutenberg.words("shakespeare-caesar.txt")
text = nltk.corpus.gutenberg.raw("shakespeare-caesar.txt")

#TODO: Complete the homework
#for line in text:
#    print(line)
#    count += 1
#    if count > 100:
#        break