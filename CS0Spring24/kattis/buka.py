'''
Written by: Corin Chepko
Date: 2/5/24
Program: Kattis Buka problem: https://open.kattis.com/problems/buka
Algorithm steps:
    input a number, A
    input an operator
    input second number, B
    use eval() to evaluate the expression A operator B (ex: A+B)
'''

#a = input()
#a = int(a)
a = input()  #one line that is same as last two
#a can be a string, coverting to int is not something we need to do for this problem
operand = input()
b = input()

expression = a+operand+b
#print(expression) #check and verify step that my previous lines are doing what I want
print(eval(expression))

a='hello'
expression = a+operand+b
print(eval(expression))