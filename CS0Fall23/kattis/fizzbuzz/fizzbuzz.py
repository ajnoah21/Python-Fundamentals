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
def test():
    pass

def main():
    x, y, N = map(int, input().split())
    print(x,y,N)

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()