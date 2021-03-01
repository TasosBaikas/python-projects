import re
from string import digits,punctuation
import sys

try:
    print("\n" * 5)
    print("please enter the file name")
    print("if the file is 'two_cities.txt' then enter 1")
    print()
    fileName = input("enter the file name :")
    if fileName:
        fileName = "two_cities.txt"
    file = open(fileName , "r" )
except:
    print("the file does not exist! Restart the programm")
    sys.exit(0)
    

stringText = file.read().replace('\n', ' ')
stringText = " ".join(stringText.split())

stringText = re.sub(r'[^\w\s]',' ',stringText) 
remove_digits = str.maketrans('', '', digits) 
stringText = stringText.translate(remove_digits)

wordList = [ [] for i in range(20)]

print("\n------Showing letters with sum 20------\n")

tempList = stringText.split(" ")
for word in tempList:
    if len(word) > 20 or len(word) < 1:
        continue
    else:
        wordList[len(word) - 1].append(word)

while True:
    if len(wordList[19]) > 1:
        print("words: " + str(wordList[19].pop()) + " and " + str(wordList[19].pop()) + " their sum is 20")
    else:
        break

while True:
    if len(wordList[9]) > 1:
        print("words: " + str(wordList[9].pop()) + " and " + str(wordList[9].pop()) + " their sum is 20")
    else:
        break

for i in range(9):
    while True:
        if len(wordList[i]) > 0 and len(wordList[18 - i]) > 0:
            print("words: " + str(wordList[i].pop()) + " and " + str(wordList[18 - i].pop()) + " their sum is 20")
        else:
            break

file.close()