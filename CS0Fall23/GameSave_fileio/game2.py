import game_open_save as gos
import pathlib
my_path = pathlib.Path(__file__).parent.resolve() #gets the path to file folder

def main():
    name = input("What your name?")
    filename = f"{my_path}/{name}.txt"

    stats, is_empty = gos.check_name_for_save(filename)

    for stat in stats:
        print(f"{stat} {stats[stat]}") 
        #stat is a dictionary item, so stat is the key, stats[stat] is value

    stats["Loses"] = 2

    gos.write_file(filename, stats) # saves game

if __name__ == "__main__":
    main()