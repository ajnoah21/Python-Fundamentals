'''
User definned functions
9/18/23
'''

def print_message():
    '''Fruitless function, takes no parameters, returns no information.
    Prints a message'''

    message = '''Some long profound message.'''
    print(message)

def print_custom_message(message='default value'):
    '''Fruitless function, takes one parameter, returns no information.
    Prints a message'''

    print(message)

def return_custom_message(message):
    '''Fruitfull function, takes one parameter, returns a value, in
    this case, a string'''
    out_message = "Hello, " + message
    
    condition = True

    if(condition == True):
        return out_message # return statements exit a function, 
                           # no more code below is executed
    #else:
    #    return out_message + "some more stuff."
    return out_message + "some more stuff."

def print_global_message():
    '''Fruitless function, takes one parameter, returns no information.
    Prints a message'''
    
    print(message)

print("Hello,\n")
print_message()
message = "An even more profound message!"
print_custom_message(message)

message2 = return_custom_message(message) # not tabbed in, this is a global variable
print(message2)

print_custom_message()

message = "something else"
print_global_message()
print(message)