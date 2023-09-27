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

def main():
    name = input()
    a = int(input())
    b = int(input())
    ab = int(input())

    if(a-b < 0):
        if( ab == abs(a-b)):
            ans = 'SITH'
        else:
            ans = 'JEDI'
    else:
        ans = 'VEIT EKKI'
    
    print(ans)



if __name__ == '__main__':
    main()