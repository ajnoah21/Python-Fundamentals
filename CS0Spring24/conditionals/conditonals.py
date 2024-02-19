def main():
    x=5
    y=10

    print("x > y is",x>y)

    if y==10:
        print("y is equal to", y)

    yes_no = input("Would you like to add two numbers? ")

    if( yes_no != 'yes' and yes_no != "y" and yes_no != "Yes" and yes_no != 'Y'): # one way conditional
        sure = input("Are you sure?")
        if( sure == 'y'):
            print("Exiting program...")
            return  # This is an early exit to the program
    
    print("Sum of x and y is", x+y)

    day = "Friday"
    if(day == "Monday"):  # multi-way conditional
        print("It's Monday")
    elif(day == "Tuesday"):
        print("It's Tuesday")
    else:
        print("It's not Monday or Tuesday")

    something = -23
    if(something):  # if 'something' is a non-zero number, this evaluates to True
        print("That conditional was True")

    # and demo
    num = -14
    if num%2 == 0 and num < 0: # if remainder of division by 2 is equal to 0 and the number is positive
        print(f"{num} is even and negative")




main()