'''
Name: Corin Chepko
Date: 10/27/23
Program Description: https://open.kattis.com/problems/pieceofcake2
Algorithm: input length of sides, vertical and horizantal distances of cuts
            find biggest horizantal and vertical dimesions for largest piece
            print the volume of that piece
''' 

import sys

def solution(l,v,h):
    if( l-v > v ):
        v_side = l-v
    else:
        v_side = v
    
    if( l-h > h ):
        h_side = l-h
    else:
        h_side = h
    
    return h_side*v_side*4

def test():
    assert (solution(4,2,2) == 16)
    print("All tests passed!", file=sys.stderr)

def main():
    test()

    l, v, h = map(int,input().split())
    
    volume = solution(l,v,h)

    print(volume)

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()