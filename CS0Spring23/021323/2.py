# How to modify global variable inside function
var1 = "Alice" # global

def myFunc(arg1, arg2):
    #global var1 # Tell myFunc that var1 is global
    var1 = "Bob" # global or local? How can we access global var1?
    var2 = "John"
    print('var1 = {}'.format(var1))
    print('var2 = ', var2)
    print('arg1 = ', arg1)
    print('arg2 = ', arg2)

myFunc(1, 'Apple')
print(var1