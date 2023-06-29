import re

text = "|LQUOTE| Mitigating the risk of extinction from A.I. should be a global priority alongside other societal-scale risks, such as pandemics and nuclear war, |RQUOTE|  the one-sentence statement said."

result = re.findall(".the.", text)
#print(result)

list = ["Jan","January","Jan.",

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

testString = "January 12, 2023"
for month in list:
        for dt4 in re.findall(f'{month} \d\d, \d\d\d\d', testString):
                print(dt4)
                #count += 1