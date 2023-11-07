'''
Name: Corin Chepko
Date: 11/03/23
Program Description: https://open.kattis.com/problems/hardwoodspecies
'''

import sys

def test():
    in_lines = 'oak aspen oak willow'
    lines = in_lines.split()
    assert solution(lines) == ['aspen 25.000000','oak 50.000000','willow 25.000000']

    print("Test case passed!",file=sys.stderr)

def solution(lines):
    trees = {}
    total_trees = 0
        
    for line in lines:
        total_trees += 1
        line = line.strip() # take off the newline character ('\n') at the end
        if line not in trees: # if tree name isn't in the dictionary, create it with 1 tree counted
            trees[line] = 1
        else:   # seen this tree before, add 1 to the count
            trees[line] += 1

    trees = dict(sorted(trees.items())) # sorts dictionary by key names (tree names)
    answer = []
    for key,value in trees.items():
        answer.append(f"{key} {(value/total_trees)*100:.6f}") # print the percentage out of the total population for this type of tree out to 6 decimals
    
    return answer

def main():
    test()

    lines = []
    for line in sys.stdin:
        if(line == '\n'): # needed so during testing user can gracfully exit input loop by pressing enter
            break
        lines.append(line) 
    
    answer = solution(lines) # send the input lines, get a list of ouput lines
    for ans in answer:
        print(ans)
    
        

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()
