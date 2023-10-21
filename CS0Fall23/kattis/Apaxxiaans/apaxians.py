'''
Name: Corin Chepko
Date: 10/20/23
Program Description: https://open.kattis.com/problems/apaxiaaans
Algorithm:
    input string
    remove any repeating characters
    print improved string
'''
def test():
    pass

def solution(name):
    answer = ""
    last_char = ''
    for character in name:
        if character != last_char:
            answer += character
        last_char = character
    return answer
        

def main():
    name = input()
    answer = solution(name)
    print(answer)

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()