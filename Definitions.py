import requests

def Definitions(word: str):
    text = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
    definition = text.text[text.text.find("\"definition\":") + 14:text.text.find("\"", text.text.find("\"definition\":") + 14)]
    if definition == "Definitions Found":
        return '$Error$'
    return definition
