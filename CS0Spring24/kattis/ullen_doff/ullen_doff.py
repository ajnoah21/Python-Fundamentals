'''
Corin Chepko
2/23/24
Kattis Problem: Ullen etc...:   https://open.kattis.com/problems/ullendullendoff
Algorithm Steps:
    input number of friends and convert to int
    input names separted by a space using .split() method
    if( there are more than 14 friends, pick the 13th friend (or number 12 if starting from 0))
    else:
        Take 13 % N_friends name as friend, or (13 % N-friends) - 1 if zero based 
'''

import sys



def main():
    print("Enter # of friends: ", file=sys.stderr)  # Kattis safe message to user
    n_friends = int(input())

    print("Enter names separated by a space: ", file=sys.stderr)  # Kattis safe message to user
    names = input().split()

    #print(n_friends)
    #print(names)
    
    if(n_friends >= 13):
        print(names[12])
    else:               # There are less than 13 names
        position = 13%n_friends - 1
        print(names[position])  # print the name of the reaminder of 13/n_friends position



main()