import json
from difflib import get_close_matches, SequenceMatcher

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Maybe you meant %s ? Enter y if yes or n if no: " % get_close_matches(word, data.keys())[0])
        if yn.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == 'n':
            return "Not existing word. Please double check it!"
        else:
            return "I didn't understand your query!"
    else:
        return "Not existing word. Please double check it!"

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
