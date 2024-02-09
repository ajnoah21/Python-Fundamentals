import math

def main():
    print("Hello World!")
    A = calc_area(1)
    print(A)
    name=getName()
    greet(name)

    print()
    print(find_max(1,1,1))

def greet(name):
    print(f"Hello {name}!")
    print("hello", name, '!')

def getName():
    name = input("Hi there, enter your full name: ")
    return name
    print(f'Hi {name}, nice meeting you!') # dead code - will not be executed

def calc_area(radius):  # this is a fruitful function, it returns a value
    area = math.pi * radius**2
    return area

def find_max(a, b, c):
    if(a > b and a > c):
        return a  # if the above conditional is true, 
                #this statement executes and the function 
                # returns and ends, no futher lines will execute
    if(b > a and b > c):
        return b
    if(c > b and c > a):
        return c
    else:
        return a

main()