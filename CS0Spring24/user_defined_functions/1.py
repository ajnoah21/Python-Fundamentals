# function definitions will be above the first running lines of code

def greet():
    print("Hello world!")

def fancier_greet(name):
    '''
    This is a slightly more complicated function that take a name as an argument
    Also, a triple quoted string like this at beginning of function is read
    by VSCode and displayed as function help.
    '''
    print("Hello", name)

def greet_with_return():
    '''
    This is a fruitful function example that collects a name, 
    and returns it to the rest of the program.
    '''
    name = input("Enter your name: ")
    print("Hello", name)

    return name  # a fruitful function must return some data

def main(): #usually this is defined as the very beginning, with main()
    # being called as the very first unindented line
    greet()
    fancier_greet("Corin")

    my_name = greet_with_return()
    print(my_name)

# first unindented line that is not a function definition or import 
# is beginning of program
main()