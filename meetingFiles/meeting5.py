import re
import nltk
import datetime
from nltk.tokenize import sent_tokenize, word_tokenize

inFile = open("/Users/omer2/OneDrive/Documents/NLP/UTD_NLP/meetingFiles/text_web.txt", "r", encoding="utf8")
outFile = open("output.txt", "w")

#replacing = [("A.I.", "|AI|"), ("“", "|LQUOTE|"), ("”", "|RQUOTE|")]

text = inFile.read()
text = text.replace("A.I.", "|AI|")
text = text.replace("“", " |LQUOTE| ")
text = text.replace("”", " |RQUOTE| ")


#theCount = 0
count = 0
today = datetime.date.today()
for sentence in sent_tokenize(text):
    sentence = sentence.replace("<p>","")
    result = re.findall("\d\d\d\d-\d\d-\d\d", sentence)
    results = re.findall("\d\d-\d\d-\d\d\d\d", sentence)
    if result != [] or results != []:
        for dt in result:
            print(f"convert to date object {dt}")
            dateObj = (datetime.date(int(dt[0:4]), int(dt[5:7]), int(dt[9:11])))
            print(sentence)
            print(dateObj)
            print("=" * 80)
        for dt in results:
            dateObj = (datetime.date(int(dt[6:11]), int(dt[0:2]), int(dt[3:5])))
            print(sentence)
            print(dateObj)
            print("=" * 80)        
        #print(result)
   # if count>10000:
     #   break   
   #count += 1
    #for word in word_tokenize(sentence):
        #if word.lower()=='the':
            #theCount += 1
            #word = word.replace("|AI|","A.I.")
            #print(word)
    #sentence = sentence.replace("|AI|","A.I.")
    #print(sentence.replace("|AI|","A.I."))
    #outFile.write("> " + sentence+"\n")
#print(f"THE Count: {theCount}")
inFile.close()
outFile.close()