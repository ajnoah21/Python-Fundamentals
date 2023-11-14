'''
Name: Corin Chepko
Date: 11/10/23
Program Description: Input and output game files, using a dictionary to save data 
'''

import pathlib
import os


def game(stats):
    for key in stats.keys():
        stats[key] += 1

def write_file(name_path, stats):
    '''Take two parameters, a file_name (with full path), and a stats{}
    dictionary which is loaded or created by check_name_for_save, writes
    the stats to the file.
    Takes a string pathname and a stats dictionary as parameters,
    returns nothing
    '''
    with open(name_path,'w') as my_file:
        for key,value in stats.items():
            my_file.write(f"{key} {value}\n")

def read_player_file(name_path):
    '''
    Open and read contents of file into "stats" dictionary
    Take a full pathname string for a parameter and returns 
    (stats) dictionary.
    '''
    stats = {}
    with open(name_path,'r') as my_file:
        for i in range(4):
            ins = my_file.readline().strip().split()
            stats[ins[0]] = int(ins[1])
        
    return stats

def check_name_for_save(name_path):
    '''
    Tries to open file at name_path, returns "stats" 
    dictionary and "is_empty" bool in case the file 
    is empty or does not exist. In the case of no file or empty,
    stats is initialized with zero values.
    Takes a string pathname as a parameter and returns (stats, is_empty)
    '''
    
    if( os.path.isfile(name_path) and os.path.getsize(name_path) > 0):
        print("File Exists and has stuff, better read it in...")
        stats = read_player_file(name_path)
        open_str = 'r+'
        is_empty = False
    else:
        print("No file or empty!")
        open_str = 'w'
        stats = {}
        stats["Wins"] = 0
        stats["Loses"] = 0
        stats["total_guesses"] = 0
        stats["times_played"] = 0
        is_empty = True
    
    return stats, is_empty

def main():
    my_path = pathlib.Path(__file__).parent.resolve()
    os.system('cls')

    name = input("Whats your player name?\n")
    name_path = f"{my_path}/{name}.txt"
    stats, is_empty = check_name_for_save(name_path)

    if(is_empty):
        print(f"\nWelcome to my game, {name}!\nI'll make a save_file to collect your playing data. Enjoy the Game!")
    else:
        print(f"\nWelcome to my game, {name}!\n")
        print("Here are your stats so far...\n")
        print(name)
        for key,value in stats.items():
            print(f"{key} {value}")

    game(stats)

    write_file(name_path, stats) 

    print("\nThanks for playing!")
# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()
