################################################################################
#
#         FILE: 
#           oeassignment2.py
#       AUTHOR: 
#             Omer Erturk
#  DESCRIPTION: 
#           Assignment 2#           
#           My program breaks down a text file into tokenized sentences (removing possible html tags and line breaks), displays pos_tags of each sentence, gets the first noun and displays its definition, and compares its synsets with the remaining nouns synset with their definition
# DEPENDENCIES:
#           Created with Python 3.10.5 (Python version)
#           NLTK, re, wordnet
################################################################################
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
import re

inFile = open("/Users/omer2/OneDrive/Documents/NLP/UTD_NLP/meetingFiles/text_web.txt", "r", encoding="utf8")
outFile = open("output.txt", "w")
text = inFile.read()

#Removes HTML tags
removed_text = re.sub(r'<.*?>', "", text)
count = 0
countt = 0
#Tokenizes by sentences
for sentence in sent_tokenize(removed_text):
    #Virtual Separator
    print("=" * 80)
    outFile.write("=" * 80 + "\n")
    print(sentence)
    outFile.write(sentence)
    sentList = word_tokenize(sentence)
    #Get pos_tag for each word in the sentence
    print(nltk.pos_tag(sentList))
    outFile.write(str(nltk.pos_tag(sentList)) + "\n")
    for word,tag in nltk.pos_tag(sentList):
        countt += 1 
        #Checks for the first noun
        if tag == "NN" :
            firstWord = word
            print(word)
            outFile.write(word + "\n")
            #Gets the list of synsets of the first noun
            for i in wn.synsets(word):
                #Definition of first noun
                print(i, i.definition()[:30])
                outFile.write(str(i) + " " + i.definition()[:30] + "\n")
                #Compares with other nouns in sentence
                for word2,tag in (nltk.pos_tag(sentList[countt:])):
                    if tag == "NN" and wn.synsets(word2) != []:
                        otherSynset = wn.synsets(word2)[0]
                        print(f"\tNearest Common Hypernym with {word2} is {i.lowest_common_hypernyms(otherSynset)}")
                        outFile.write(f"\tNearest Common Hypernym with {word2} is {i.lowest_common_hypernyms(otherSynset)}\n")
                        print(f"\t\t{word2}: {otherSynset.definition()[:30]}")
                        outFile.write(f"\t\t{word2}: {otherSynset.definition()[:30]}\n")
            break    
    countt = 0            
               
        
        
    
   
    
    
    