'''
Written by: Corin Chepko
Date: 2/16/24
Program Description: Kattis problem: Digit Swap
    https://open.kattis.com/problems/digitswap
Algorithm Steps:
    input a number, which will be 2 digits
    make a varible for digit 1, and 1 for digit 2
    print them in opposite order
'''

import sys

def solution(number):
    first = number[0] # the square bracket on a string lets us                     # specify whcih charater in the string
    second = number[1] # This will be the second character, or digit in this case
    return second+first

def test():
    assert(solution("12") == "21")
    assert(solution("32") == "23")

def main():
    
    test()    

    print("Enter a number: ", file=sys.stderr) # with file=sys.stderr kattis will ignore this message

    number = input()

    ans = solution(number)
    print(ans)


if __name__ == "__main__":  # if I'm the main file being run, then run my program, otherwise my fuctions are available for import
    main()