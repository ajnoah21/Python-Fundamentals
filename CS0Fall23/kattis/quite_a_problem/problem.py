'''
Name: Corin Chepko
Date: 10/25/23
Program Description: https://open.kattis.com/problems/quiteaproblem
Algorithm:
    for each line of input:
        check if the text "problem" (any case) is in the line
        if it is:
            print "yes"
        else
            print "no"
'''
import sys

def test():
    pass

def solution(phrase):
    phrase = phrase.lower() # convert to all lower case
    if "problem" in phrase:
        ans = "yes"
    else:
        ans = "no"
    return ans

def main():
    for phrase in sys.stdin:
    
        
        ans = solution(phrase)
        
        print(ans)

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()