'''
Name: Corin Chepko
Date: 10/4/23
Program Description: Kattis Problem "Judging Moose":
https://open.kattis.com/problems/judgingmoose

Algorithm:
    Input line with two integers
    Take the larger integer and double it for the number of tines
    if numbers are the same:
        print even num_tines
    else:
        print odd num_tines
'''

import sys

def test():
    assert solution(2,2) == 'Even 4'
    assert solution(1,2) == "Odd 4"
    assert solution(0,0) == 'Not a moose'
    print("All tests passed!", file=sys.stderr)

def larger(n1, n2):
    if(n1 > n2):
        return n1
    else:
        return n2

def solution(n1, n2):
    # if they are equal, just double one of the numbers and print "even N"
    if(n1 == 0 and n2 == 0):
        answer = "Not a moose"
    elif(n1 == n2):
        answer = "Even " + str(2*n1)    
    else:
        answer = f"Odd {2*larger(n1,n2)}"
    
    return answer

def main():
    test()

    line = input()
    n1, n2 = line.split()
    n1 = int(n1)
    n2 = int(n2)

    answer = solution(n1, n2)
    print(answer)

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()