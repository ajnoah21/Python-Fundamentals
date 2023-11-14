import pathlib
import game_open_save as gos

def main():
    name = input("What your name?")
    my_path = pathlib.Path(__file__).parent.resolve()
    filename = f"{my_path}/{name}.txt"
    print(filename)
    stats, is_empty = gos.check_name_for_save(filename)

    print(f"Hello {name}, here are your stats so far:\n")
    for stat in stats:
        print(f"{stat}, {stats[stat]}")
    
    stats['Wins'] = 5

    gos.write_file(filename, stats)


if(__name__ == '__main__'):
    main() 