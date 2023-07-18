from ExtractFromPDF import ExtractFromPDF
from Predictions import Predictions
from Definitions import Definitions

NumberOfWords = 10
PdfName = "1.pdf"

# Extracts words from pdf and makes preditions on them
WordList = ExtractFromPDF(PdfName)
RatingsWordList = Predictions(WordList)
ComplexWordList = []

# This variable keeps track of the count of words
count = 0

# Appends word and definition to list if the definition is valid
for word in RatingsWordList:
    definition = Definitions(word[1])
    if(definition != '$Error$'):
        ComplexWordList.append((word[1], definition))
    if(len(ComplexWordList) >= NumberOfWords):
        break

# Prints the list of most complex words in the pdf
print(ComplexWordList)

