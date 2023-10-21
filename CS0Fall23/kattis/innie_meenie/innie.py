'''
Written by: Corin Chepko
Date: 9//25/23
Program: Kattis problem: https://open.kattis.com/problems/ullendullendoff
Algorithm:
    input number of friends
    input list of names
    if number of names is greater than 13, answer is 13th name, index 12
    take 13%number-1 as index into name list
    print name
'''

def solution(number, names):
    '''
    computes who wins with a number of names and list of names
    '''   
    ans = ''
    if(number > 13):
        ans = names[12]
    else:
        index = 13%number-1
        ans = names[index]
    
    

    #print(number, names)
    #print(names[0]) # prints the first name
    #print(names[2]) # prints the third name
    #print(names[-1]) # index of -1 is last index
    #print(names[-2]) # index of -2 is second to last
    return ans

def test():
    number = 3
    names = ['corin', 'annie', 'tater']
    assert solution(number, names) == 'corin'

    number = 4
    names = ['corin', 'annie', 'tater', 'ceres']
    assert solution(number, names) == 'corin'

    number = 5
    names = ['corin', 'annie', 'tater', 'ceres', 'mark']
    assert solution(number, names) == 'tater'

    print("All test cases passed!")

def main():

    number = int(input())
    names = input().split()

    ans = solution(number, names)
    print(ans)

    test() #comment out for kattis submission

if __name__ == "__main__":
  #print(__name__)
  main() # call main function
