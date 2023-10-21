'''
More user definned functions
9/18/23
'''
def print_greeting(name, message):
    print("Hello!", name)
    print("more")

def main():
    '''
    This is where our program will actually begin.
    '''
    message = "Hi y'all"
    name = input("Please  enter your name: ")
    print_greeting(name, message)

main()
    