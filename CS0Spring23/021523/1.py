import math

def multply_pi_by_input(input_val):
    return math.pi*input_val

name = "corin"
number = 3.14159

out_string = f'This is a message for {name}, his number is {number}.'

print(out_string)
print("Hello, %s, nice to meet you. Here's a number, %1.2f" % (name, number))
print("Hello, {0}, nice to meet you. Here's your number {1}".format(name, number))
print("Hello, {1}, nice to meet you. Here's your number {0}".format(name, number))
print(f"Hello {name}, nice to meet you! Here's your number: {number}")

return_val = multply_pi_by_input(number)
print(return_val)