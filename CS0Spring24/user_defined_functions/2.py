'''
Corin Chepko
2/19/24
My Calulator Program
'''


def add_two(number1, number2):
    sum = number1+number2
    return sum

def main():
    number1 = float(input("Enter first number"))
    number2 = float(input("Enter second number"))

    sum = add_two(number1, number2)
    print(f"Sum of {number1} + {number2} = {sum}")

main()

