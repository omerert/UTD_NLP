#
#
#          FILE:
#           oeassginment1.py
#       AUTHOR:
#           Omer Erturk
#  DESCRIPTION:
#           It detects different kinds of dates in a string and returns those strings
# DEPENDENCIES:
#           Created with Python 3.11.4 
#           NLTK and REGEX#
import nltk
import nltk.data
import datetime
import re
from nltk.tokenize import sent_tokenize, word_tokenize

inFile = open("text_web.txt", "r", encoding="utf8")

monthList = ["Jan","January","Jan.",

        "Feb","February","Feb.",

        "Mar","March","Mar.",

        "Apr","April","Apr.",

        "May",

        "Jun","June","Jun.",

        "Jul","July","Jul.",

        "Aug","August","Aug.",

        "Sep","September","Sep.","Sept.","Sept",

        "Oct","October","Oct.",

        "Nov","November","Nov.",

        "Dec","December","Dec."]

charDates = {("Jan", "January", "Jan."): 1,
    ("Feb", "February", "Feb."): 2,
    ("Mar", "March", "Mar."): 3,
    ("Apr", "April", "Apr."): 4,
    "May": 5,
    ("Jun", "June", "Jun."): 6,
    ("Jul", "July", "Jul."): 7,
    ("Aug", "August", "Aug."): 8,
    ("Sep", "September", "Sep.", "Sept.", "Sept"): 9,
    ("Oct", "October", "Oct."): 10,
    ("Nov", "November", "Nov."): 11,
    ("Dec", "December", "Dec."): 12}

count = 0
#Separate by <p>
text = inFile.read().split("<p>")  
for para in text: 
#Separate by sentence
    tokenizedFile =  sent_tokenize(para)
    for sentence in tokenizedFile:
        dateList = []

        #First kind of datetype

        for dt1 in re.findall(r"\d\d\d\d-\d\d-\d\d", sentence):
            dateList.append(datetime.date(int(dt1[0:4]), int(dt1[5:7]), int(dt1[8:12])))
            count += 1
        if dateList != []:
            print(sentence + "\n" + str(dateList) + "\n" + "=" * 80)

        #12/24/2023 Datetype

        dateList = []
        for dt2 in re.findall(r"\d\d/\d\d/\d\d\d\d", sentence):
            dateList.append(datetime.date(int(dt2[6:11]), int(dt2[0:2]), int(dt2[3:5])))
            count += 1
        if dateList != []:
            print(sentence + "\n" + str(dateList) + "\n" + "=" * 80)

        #12/24/23 Datetype

        dateList = []
        for dt3 in re.findall(r"\b\d{2}/\d{2}/\d{2}\b(?!\d{2,})", sentence):
            dateList.append(datetime.date(int(dt3[6:11]) + 2000, int(dt3[0:2]), int(dt3[3:5])))
            count += 1
        if dateList != []:
            print(sentence + "\n" + str(dateList) + "\n" + "=" * 80)
        
        #July and Jul datetypes
        dateList = []
        today = datetime.datetime.now().year
        for month in monthList:
            for dt4 in re.findall(fr'{month} \d\d, \d\d\d\d', sentence):
                dateList.append(datetime.date(int(dt4[6: 10]), int(charDates[month]), int(dt4[1:3])))
            #for dt4 in re.findall(r"\b" + month + "{2}, ", sentence):
             #    dateList.append(datetime.date(int(today), int(dt4[2:3]), int(dt4[1:3])))
            
        #print(dateList)
        
#print(count)