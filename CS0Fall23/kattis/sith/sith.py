'''
Corin Chepko
9/27/23
Kattis Problem Sith: https://open.kattis.com/problems/sith

input line of name
input a
input b
input a-b
if(a-b is negative and a-b == abs(a-b):
    SITH
    a-b is negative and a-b = a-b):
    JEDI
else:
    DONT KNOW
'''

import math
import sys

def solution(a, b, ab):
    if(a-b < 0):  # if a-b is negative, then we can figure if the user is a jedi or sith
        if( ab == abs(a-b)):
            ans = 'SITH'
        else:
            ans = 'JEDI'
    else:
        ans = 'VEIT EKKI'
    
    return ans

def test():
    a = 69
    b = 80
    ab = -11
    assert solution(a,b,ab) == 'JEDI'
    assert solution(2, 4, 2) == 'SITH'
    assert solution(4, 3, 1) == 'VEIT EKKI'
    print("All test cases passed!", file=sys.stderr)


def main():

    test()

    name = input()
    a = int(input())
    b = int(input())
    ab = int(input())

    ans = solution(a, b, ab)
    
    print(ans)



if __name__ == '__main__':
    main()