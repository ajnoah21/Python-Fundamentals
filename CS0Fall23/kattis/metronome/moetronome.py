'''
Metronome kattis problem: https://open.kattis.com/problems/metronome
Written by: Corin Chepko
9/20/23
'''

def solution(number):
    ans = number/4
    return ans

def test():
    assert solution(4) == 1.0
    assert solution(99) == 24.75
    print("All test passed!")

def main():
    num = int(input()) # input a number and turn it into an integer
    answer = solution(num)
    print(answer)

    test()

main()
