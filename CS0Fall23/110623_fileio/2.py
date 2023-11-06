# File IO examples
import random

print("Hello World!")

words = []

with open("dict-words.txt", 'r') as fin:
    lines = fin.readlines()
    #while( True):
    #    line = fin.readline()
    #    words.append(line)
    #    if line == '':
    #        break
    
#print(lines)
choice = random.choice(lines).strip().lower()
print(choice)

games_won = 3
games_lost = 2
guesses = ['a','b','c']

with open("game_stats.txt", 'w') as fout:
    line_out = f"Games won: {games_won}\nGames Lost: {games_lost}\n"
    fout.write(line_out)
    for guess in guesses:
        out = f"{guess:>5}"
        fout.write(out)