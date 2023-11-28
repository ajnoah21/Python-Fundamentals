def func(number):
    if(number > 0 ):
        print("Error!")
        return 1
    elif( number < 0):
        return -1
    else:
        return 0
    print("something else")

print(func(int(input('Enter a number: '))))