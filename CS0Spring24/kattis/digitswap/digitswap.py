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

def main():
    print("Enter a number: ", file=sys.stderr) # with file=sys.stderr kattis will ignore this message

    number = input()

    #print(number[::-1]) another way to do what the next three lines do

    first = number[0] # the square bracket on a string lets us                     # specify whcih charater in the string
    second = number[1] # This will be the second character, or digit in this case
    print(second+first)

    #print(number[1]+number[0])

if __name__ == "__main__":  # if I'm the main file being run, then run my program, otherwise my fuctions are available for import
    main()