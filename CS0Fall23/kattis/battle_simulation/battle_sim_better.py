'''
Name: Corin Chepko
Date: 10/25/23
Program Description: https://open.kattis.com/problems/battlesimulation
Algorithm:
    input a string
    for each char in string, output counter char, 'R'>'S','B'>'K','L'>'H'
    if see LBR,LRB,BRL,BLR,RBL,RLB ect..., output 'C' to counter
'''

# Python program to show time by perf_counter() 
from time import perf_counter

def test():
    pass

def main():
    moves = input()
    
    timestart = perf_counter()

    combos = ('LBR','LRB','BRL','BLR','RBL','RLB')
    
    counters = ""
    
    #for ch in moves:
    index = 0
    while(index < len(moves)):
        if( (index <= len(moves)-2) and (moves[index:index+3] in combos)):
            #counters.append('C')
            counters += 'C'
            index += 2
        elif moves[index] == 'R':
            #counters.append('S')
            counters += 'S'
        elif moves[index] == 'B':
            #counters.append('K')
            counters += 'K'
        else:# moves[index] == 'L':
            #counters.append('H')
            counters += 'H'
        
        index +=1
    
    print(counters)

    timestop = perf_counter()
    
    print(f"Time = {(timestop-timestart)*1000000} miliseconds." )


# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()