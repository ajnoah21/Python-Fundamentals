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
        total_trees += 1
        line = line.strip() # take off the newline character ('\n') at the end
        if line not in trees: # if tree name isn't in the dictionary, create it with 1 tree counted
            trees[line] = 1
        else:   # seen this tree before, add 1 to the count
            trees[line] += 1 
        
        if(line == ''): # needed so during testing user can gracfully exit program by pressing enter
            total_trees -= 1 #not a tree, so subract 1 from population total
            break
    
    trees = dict(sorted(trees.items())) # sorts dictionary by key names (tree names)
    for key,value in trees.items():
        print(f"{key} {(value/total_trees)*100:.6f}") # print the percentage out of the total population for this type of tree out to 6 decimals
        

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()
