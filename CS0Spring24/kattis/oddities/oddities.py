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

num_numbers=int(input()) # find out how many numbers to evaluate
                        # also had to convert this for math and stuff
for _ in range(num_numbers):
    xander = input()
    xander = int(xander) #convert from string to 
                        #integer so I can do math and loops and stuff
    if(xander%2 == 0):
        ans = f"{xander} is even"
    else:
        ans = f"{xander} is odd"
    
    print(ans)