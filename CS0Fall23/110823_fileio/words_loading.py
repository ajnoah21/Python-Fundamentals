'''
Name: Corin Chepko
Date: 11/08/23
Program Description: Loading words from file practice.
'''
import random
import re

def test():
    pass

def game(difficulty, name):
    filename = "dict-words.txt"
    stats = ()
    won = 0
    lost = 0

    with open(filename) as word_file:
        words = word_file.readlines()
        #words = re.sub('\w+','',words)

    while(True):    
        random_word=rand_word(difficulty,words)
        print(f"There are {len(words)} loaded.")
        print(f"Random word: {random_word}")
        won += 1
        lost = 3
        again = input("Want to play again?")
        if(again == 'y' or again == 'Y'):
            continue
        else:
            stats = (name, won, lost)
            print("Thanks for playing!")
            break
    print(stats)
    with open(name + 'txt', 'w') as out_file:
        out_file.write(f"Player Name: {stats[0]}\nWon: {stats[1]}\nLost: {stats[2]}")


    


        

def rand_word(difficulty, words):
    if(difficulty == 1):
        while(True):
            random_word = random.choice(words).strip()
            if( len(random_word) > 3 and len(random_word) < 5):
                break
    if(difficulty == 2):
        while(True):
            random_word = random.choice(words).strip()
            if( len(random_word) > 5 and len(random_word) < 8):
                break
    if(difficulty == 3):
        while(True):
            random_word = random.choice(words).strip()
            if( len(random_word) > 8 ):
                break
    random_word = random_word.lower()
    return random_word

def main():
    difficulty = 2
    name = input("Enter your player name. (no spaces)")
    game(difficulty, name)

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()
