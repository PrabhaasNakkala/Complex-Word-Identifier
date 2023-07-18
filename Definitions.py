import requests

def Definitions(word: str):

    # Request to get the definition of the intended word
    text = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)

    # Editing the string to obtain only the definition
    definition = text.text[text.text.find("\"definition\":") + 14:text.text.find("\"", text.text.find("\"definition\":") + 14)]

    # Checks if the definition for the word is found or not
    if definition == "Definitions Found":
        return '$Error$'
    
    return definition
