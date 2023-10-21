# This program multiplies two numbers and prints the output

def multiply(num1, num2):
    return num1*num2

numbers = input("Please enter 2 numbers separted by a space: ")
numbers1, numbers2 = numbers.split()

numbers1 = float(numbers1)
numbers2 = float(numbers2)
print(numbers1)
print(numbers2)
print(multiply(numbers1, numbers2))

name =  input("enter a name: ")

print(f'Hi, my name is: {name}')

assert multiply(2.0,-2.0) == -4.0
