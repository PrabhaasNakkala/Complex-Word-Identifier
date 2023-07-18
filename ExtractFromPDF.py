import PyPDF2

def ExtractFromPDF(url: str):

    # Initializes list to store pdf content
    WordList = []

    # Opens and reads the pdf file
    OpenFile = open(url, 'rb')
    ReadFile = PyPDF2.PdfReader(OpenFile)
    
    # Filters out newlines and dashes from pdf text and appends to list
    for page in ReadFile.pages:
        content = page.extract_text()
        content = content.replace(r'\n', ' ').replace('-', '').replace('\n', '')
        WordList += content.split()

    # Initializes set to get rid of duplicate terms 
    SetWordList = set()

    # Adds to set if term is all letters and withing the given range
    for word in WordList:
        # Checks if term satisfies conditions to avoid making preditions on irrelevent terms
        if word.isalpha() and len(word) > 8 and len(word) < 24:
            SetWordList.add(word)

    # Converts set to list to return proper data type
    WordList = list(SetWordList)

    # Closes the pdf file
    OpenFile.close()

    return WordList
