import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

inFile = open("nyt.txt", "r", encoding="utf8")
inText = inFile.read()

inText = inText.replace("A.I.", "|AI|")

sentenceList = tokenizer.tokenize(inText)
count = 0
theCount = 0
startThe = 0
for sent in sentenceList:
    sent = sent.replace("|AI|", "A.I.")
    sentList = sent.split(" ")
    if sentList[0].lower() == 'the':
        startThe += 1
    for word in sentList:
        print(word)
        count += 1
        #if word=="the":
        #    theCount += 1
        if "the" in word.lower():
            theCount += 1
    print("=" * 70)
print("Stentence Count: " + str(len(sentenceList)))
print("Word Count: " + str(count))
print("The count:", theCount)
print("startThe count:", startThe)
print("the Frequency:", theCount / count)
avgSentLen = count / len(sentenceList)
print(avgSentLen)
