import random

names = ["Corin", "Scott", "Elizibeth", "Lydia", "Hi"]

import lib



name = lib.scott()
print(name) # This is the whole program, aside from definitions
                # Just a single function call

num3 = lib.tony(1,2) # Takes two arguments, returns one value
num1 = 1
number2 = 2
num3 = lib.tony(num1, number2)
print("Num1 = ",num1)
print(num3)

# an example of a function returning multiple values
a, b, c = input("Enter sides separated by a space: ").split()

print(lib.card)



