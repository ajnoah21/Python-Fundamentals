import json
import random

with open("EDMTDictionary.json") as json_dict:
    words_dict = json.load(json_dict)
    #print(type(words_dict))
    #print('There are {0} words in the file.'.format(len(words_dict)))
    #print(words_dict[2584])
    #print(type(words_dict[2584]))
    #choice = random.choice(words_dict)
    #print('{}\n{}\n{}'.format(choice['word'], \
    #    choice['type'], choice['description']))
difficulty = 1

if(difficulty == 1):
    while(True):
        random_word = random.choice(words_dict)
        if( len(random_word['word']) > 3 and len(random_word['word']) < 5):
            break
if(difficulty == 2):
    while(True):
        random_word = random.choice(words_dict)
        if( len(random_word['word']) > 5 and len(random_word['word']) < 8):
            break
if(difficulty == 3):
    while(True):
        random_word = random.choice(words_dict)
        if( len(random_word['word']) > 8 ):
            break
#random_word = random_word.lower()
print(f"There are {len(words_dict)} loaded.")
print(f"Random word: {random_word['word'].lower()}")
print(f"Definition: {random_word['description']}")
    

