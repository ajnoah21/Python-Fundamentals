'''
Name: Corin Chepko
Date: 10/6/23
Program Description: https://open.kattis.com/problems/fizzbuzz
Algorithm:
    input 3 integers, x, y, N
    for each number up to N,
        print the number or
        if the number is divisible by x, print 'Fizz'
        if the number is divisible by y, print 'Buzz'
        if the number is divisble by both, print 'FizzBuzz'
'''

import sys

def test():
    assert check(2, 2, 3) == "Fizz"
    assert check(3, 2, 3) == "Buzz"
    assert check(6, 2, 3) == 'FizzBuzz'
    print("All tests passed!", file=sys.stderr)

def check(i1, x, y):
    if(i1%x == 0 and i1%y == 0): # if i divisible by x
        return "FizzBuzz"
    elif(i1%y == 0): # if i divisible by y
        return "Buzz"
    elif(i1%x == 0): # if i divible by x and y
        return "Fizz"
    else:
        return str(i1) #print from 1 to N

def main():
    test()
    '''x, y, N = input().split()
    x=int(x)
    y=int(y)
    N = int(N)'''

    x, y, N = map(int, input().split())
    #print(x,y,N,x+y+N)
    for i in range(N):
        i1 = i+1
        print(check(i1, x, y))


# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()