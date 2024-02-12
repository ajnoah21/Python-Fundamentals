# Global and local scope demo
name = "Alice" # global variable

def someFunc(a, b):
    print('name = ', name) # Access global variable, name
    name1 = "John" # Declare local variable
    print(f'{a} and {b}') # a and b are local variables
    print(f'Hello {name1}') # Access local variable, name1

someFunc(1, 'Apple')
print(name) # Access global variable name
print(name1) # Can you access name1 which is local to someFunc function?