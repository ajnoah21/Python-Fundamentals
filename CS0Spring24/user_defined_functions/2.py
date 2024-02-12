def add_two():
    global number1
    sum = number1+number2
    number1 = 10

    return sum


number1 = 4
number2 = 5

sum = add_two()
print(f"Sum of {number1} + {number2} = {sum}")
print("Sum is", sum)

