'''
Name: Corin Chepko
Date: 11/03/23
Program Description: https://open.kattis.com/problems/hardwoodspecies
'''

import sys

def test():
    pass

def main():
    trees = {}
    total_trees = 0
    for line in sys.stdin:
        trees += 1
        if line not in trees:
            trees[line] = 1
        else:
            trees[line] += 1
        if(line == ''):
            break
    
    trees = dict(sorted(trees.items()))
    for key,value in trees.items():
        print(f"{key} {value:.6f}")
        

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()
