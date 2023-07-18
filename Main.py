from ExtractFromPDF import ExtractFromPDF
from Predictions import Predictions
from Definitions import Definitions

NumberOfWords = 10
WordList = ExtractFromPDF("1.pdf")
RatingsWordList = Predictions(WordList)
ComplexWordList = []

count = 0
for word in RatingsWordList:
    definition = Definitions(word[1])
    if(definition != '$Error$'):
        ComplexWordList.append((word[1], definition))
    if(len(ComplexWordList) >= NumberOfWords):
        break

print(ComplexWordList)

