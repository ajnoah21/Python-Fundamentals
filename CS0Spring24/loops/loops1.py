def main():
    again = 'y'

    for i in range(10):
        print(f"You are on game #{i}")
        print("Would you like to play again or skip the rest?")
        again = input()
        if(again == 'y'):
            continue
        else:
            print("Exiting...")
            break
    else:
        print("You've played all 10 games!")

main()