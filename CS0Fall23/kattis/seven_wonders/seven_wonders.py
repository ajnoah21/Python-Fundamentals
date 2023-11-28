'''
Name: Corin Chepko
Date: 11/01/23
Program Description: https://open.kattis.com/problems/sevenwonders
Algorithm:
    input line
    for each character in line:
        if not in map:
            add to key, (card character), to map with a value of 1
        if in the map:
            add 1 to the value for that key
'''

import sys

def test():
    input = 'TTTCCCGG'
    score = 36
    assert solution(input) == score
    assert solution('T') == 1
    assert solution('CC') == 4
    print("All tests passed!", file=sys.stderr)

def solution(line):
    cards = {}
    for ch in line:
        if ch in cards:
            cards[ch] += 1
        else:
            cards[ch] = 1
    
    sets=0
    if( 'T' in cards and 'C' in cards and 'G' in cards):
        sets = min([cards['T'], cards['C'], cards['G']])
    
    score = 0
    for value in cards.values():
        score += value**2
    score += sets*7

    return score

def main():
    test()
    line = input()
    ans = solution(line)
    print(ans)

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()