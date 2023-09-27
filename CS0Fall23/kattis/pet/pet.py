'''
Kattis Problem Pet: https://open.kattis.com/problems/pet
Written by: Corin Chepko
Date: 9/22/23
Algorithm:
    input line of 4 numbers
        split line into integers
        add the integers and assign value into win_score
        make a line varible to track which line
    
    input next line and add stuff, increment line varible
        compare score with win_score, if score > win_score, win_score = score
        win_line = line
    
    Repeat 3 more times
    
'''

def in_line_and_sum():
    '''
    input a line of numbers, split the numbers into integers,
    and add them. Then return that value.
    '''
    #summation = sum(map(int, input().split())) #makes a list of our numbers
    
    n1,n2,n3,n4 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    summation = n1+n2+n3+n4

    return summation


def main():
    summation = 0
    line = win_line = 0
    win_score = summation

    for i in range(5):
        summation = in_line_and_sum()
        line += 1
        if(summation > win_score):
            win_score = summation
            win_line = line

    '''summation = in_line_and_sum()
    line += 1
    if(summation > win_score):
        win_score = summation
        win_line = line
    
    summation = in_line_and_sum()
    line += 1
    if(summation > win_score):
        win_score = summation
        win_line = line

    summation = in_line_and_sum()
    line += 1
    if(summation > win_score):
        win_score = summation
        win_line = line
    
    summation = in_line_and_sum()
    line += 1
    if(summation > win_score):
        win_score = summation
        win_line = line'''
    
    print(win_line, win_score)

main()
    
    
