'''
Corin Chepko
2/21/24
Kattis Problem: Sith  https://open.kattis.com/problems/sith
Algorithm Steps:
    input first line, we can ignore this line
    input second line input into varible 'a'
    input third line into variable 'b'
    input forth line into varible a_minus_b
    check if a-b == a_minus_b and a-b == |a_minus_b| (absolute value)
'''

import sys

def solution(a, b, a_minus_b):
    if( a-b > 0 ):  # if this is greater than zero, cannot tell if SITH or JEDI
        answer = "VEIT EKKI"
    elif(a-b == a_minus_b):  # if this is negative and equal to reported difference, user is JEDI
        answer = "JEDI"
    else:
        answer = "SITH" # otherwise the force user is a dirty liar

    return answer

def test():
    assert solution(38, 68, 30) == "SITH"
    assert solution(69, 80, -11) == "JEDI"
    assert solution(67, 17, 50) == "VEIT EKKI"
    print("All test passed!", file=sys.stderr)

def main():
    print("Enter name of force user: ", file=sys.stderr)
    input()  # Don't need the name, so we just toss this input
    print("Enter first number: ", file=sys.stderr)
    a = int(input())
    print("Enter second number: ", file=sys.stderr)
    b = int(input())
    print("Enter difference: ", file=sys.stderr)
    a_minus_b = int(input())

    answer = solution(a, b, a_minus_b)
    
    print(answer)


test()
main()