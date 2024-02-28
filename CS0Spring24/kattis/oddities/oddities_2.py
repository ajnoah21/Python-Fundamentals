'''
Corin Chepko
2/28/24
Kattis Problem: Oddities https://open.kattis.com/problems/oddities
Algorithm Steps:
    Read the number, 'num_numbers', of numbers to evaluate for even or oddness
    for num_numbers:
        read in the number
        check if the number is even or odd
        construct an answer "x is even" or "x is odd", 
            x being the number in question
'''
def even_odd(number: int) -> str:
    '''
    Args: a number to be evaluated

    Output: -> str
    '''
    if(number%2 == 0):
        ans = "even"
    else:
        ans = "odd"
    return ans

def answer(number):
    oddness = even_odd(number)
    if(number%2 == 0):
        ans = f"{number} is {oddness}"
    else:
        ans = f"{number} is {oddness}"
    return ans

def main():
    num_numbers=int(input()) # find out how many numbers to evaluate
                            # also had to convert this for math and stuff
    for _ in range(num_numbers):
        xander = input()
        xander = int(xander) #convert from string to 
                            #integer so I can do math and loops and stuff
        ans = answer(xander)
        
        print(ans)

if __name__ == "__main__":
    main()