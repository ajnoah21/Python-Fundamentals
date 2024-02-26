def main():
    again = 'y'
    i=0
    while(True):
        print(f"You are on game #{i}")
        print("Would you like to play again or skip the rest?")
        again = input()
        i%=2
        if(again != 'y'):
            print("Exiting...")
            break
    
    i=1
    while(i != 10):
        i+=1
        print(i)

main()