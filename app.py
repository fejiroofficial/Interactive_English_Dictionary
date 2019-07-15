import json
import difflib
from difflib import get_close_matches

data = json.load(open('data/data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        options = input( f'Did you mean {get_close_matches(word, data.keys())[0]} instead?'
                        ' Enter Y if yes, or N if no: ')
        choice_chosen =  options.upper()
        if choice_chosen == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif choice_chosen == 'N':
            return 'This word doesn\'t exist'
        else:
            return 'We didn\'t understand your query'
    else:
        return 'The word doesn\'t exist. Please double check it.'

word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

