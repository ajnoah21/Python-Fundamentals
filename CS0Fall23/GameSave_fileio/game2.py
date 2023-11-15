import game_open_save as gos
import pathlib
import string
my_path = pathlib.Path(__file__).parent.resolve() #gets the path to file folder


def game(name, stats):
    while(True):
        guess = input("Guess a letter: ")
        stats["total_guesses"] += 1
        if( guess not in string.ascii_letters):
            print("Try entering a single chacter, a letter preferably: ")
        else:
            break
    if( guess.lower() == 'c'):
        stats["Wins"] += 1
    else:
        stats["Loses"] += 1
        
    stats["times_played"] += 1

def main():
    name = input("What your name?")
    filename = f"{my_path}/{name}.txt"

    stats, is_empty = gos.check_name_for_save(filename)

    for stat in stats:
        print(f"{stat} {stats[stat]}") 
        #stat is a dictionary item, so stat is the key, stats[stat] is value

    game(name, stats)

    for stat in stats:
        print(f"{stat} {stats[stat]}")

    input("Press anykey and enter to exit.")

    gos.write_file(filename, stats) # saves game

if __name__ == "__main__":
    main()