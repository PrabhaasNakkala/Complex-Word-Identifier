import PyPDF2

def ExtractFromPDF(url: str):
    OldWordList = []
    OpenFile = open(url, 'rb')
    ReadFile = PyPDF2.PdfReader(OpenFile)
    
    for page in ReadFile.pages:
        content = page.extract_text()
        content = content.replace(r'\n', ' ').replace('-', '').replace('\n', '')
        OldWordList += content.split()

    SetWordList = set()
    for word in OldWordList:
        if word.isalpha() and len(word) > 8 and len(word) < 24:
            SetWordList.add(word)

    WordList = list(SetWordList)
    OpenFile.close()
    return WordList
