'''
Name:
Date:
Program Description: 
'''

import pathlib
import os
print(pathlib.Path(__file__).parent.resolve())

def test():
    pass

def game():
    pass

def main():
    name = input("Whats your player name?")
   # if( os.path.isfile(fpath) and os.path.getsize(fpath) > 0):
   #     print("File Exists")
    player_file = open(name)
    player_file.seek(os.SEEK_END)
    if( player_file.tell() == 0):
        print("Empty file")
    player_file.close()
    game()

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()
