# Written by: Corin Chepko
# Date: 2/8/23
# Kattis Buka: Inputs three lines consisting of a number, than a chacter,
# either '*' or '+', and the programs will output the expression
# number1 "character_operator" number2

number1 = input()
operator = input()
number2 = input()

expression = number1+operator+number2

answer = eval(expression)

print(answer)