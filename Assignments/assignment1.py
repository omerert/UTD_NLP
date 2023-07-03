import nltk
import datetime
import re
from nltk.tokenize import sent_tokenize, word_tokenize

inFile = open("text_web.txt", "r", encoding="utf8")


count = 0
#Separate by <p>
text = inFile.read().split("<p>")  
for para in text: 
#Separate by sentence
    tokenizedFile =  sent_tokenize(para)
    for sentence in tokenizedFile:
        #Checks first kind of datetype
        dt1 = re.findall("\d\d\d\d-\d\d-\d\d", sentence)
        if dt1 != []:
            dateList = []
            for dt in dt1:
                #count += 1
                dateList.append(datetime.date(int(dt[0:4]), int(dt[5:7]), int(dt[9:11])))
            print(sentence + "\n" + str(dateList) + "\n" + "=" * 80)
        #Check second kind of datetype
        dt2 = re.findall("\d\d/\d\d/\d\d\d\d", sentence)
        if dt2 != []:
            
            dateList = []
            for dt in dt2:
                #count += 1
                dateList.append(datetime.date(int(dt[6:11]), int(dt[0:2]), int(dt[3:5])))
            print(sentence + "\n" + str(dateList) + "\n" + "=" * 80)
        #Check third kind of datetype
        dt3 = re.findall("s\d\d-\d\d-\d\d\s", sentence)
        if dt3 != []:
            #count += 1
            dateList = []
            for dt in dt3:
                dateList.append(datetime.date(int(dt[6:8]), int(dt[0:2]), int(dt[3:5])))
            print(sentence + "\n" + str(dateList) + "\n" + "=" * 80)
print(count)
