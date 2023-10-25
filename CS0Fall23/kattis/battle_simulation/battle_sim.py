'''
Name: Corin Chepko
Date: 10/25/23
Program Description: https://open.kattis.com/problems/battlesimulation
Algorithm:
    input a string
    for each char in string, output counter char, 'R'>'S','B'>'K','L'>'H'
    if see LBR,LRB,BRL,BLR,RBL,RLB ect..., output 'C' to counter
'''
def test():
    pass

def main():
    moves = input()
    combos = ('LBR','LRB','BRL','BLR','RBL','RLB')
    for combo in combos:
        moves=moves.replace(combo,'C') #Replace all combos with 'C' counter
    print(moves)
    counters = ""
    for ch in moves:
        if ch == 'R':
            counters = counters + 'S'
        elif ch == 'B':
            counters = counters + 'K'
        elif ch == 'L':
            counters += 'H'
        else: # Contain 'C'
            counters += ch
    
    print(counters)


# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()