'''
Loops Examples
'''

# Basic range loop
for i in range(10): #prints "i and "Hello" if i is even, "World" otherwise
    if(i%2 == 0):
        print(i, "Hello!")
    else:
        print(i)
        continue

# Basic range loop
for i in range(10): #prints "i and "Hello" if i is even, "World" otherwise
    if(i%2 == 0):
        print(i, "Hello!")
    else:
        print(i)
        continue

    if(i == 6): #stop the loop at 6
        break

    print("World")

    for i in range(5): #for..else, executes else code if loop finishes wothout a break
        if i == 2:
            continue
        print(i)
    else:
        print('end!')

    # infinite loop - will break when user inputs y or Y
while True: 
    print('hello')
    ch = input('Would you like to print "Hello" again? y or Y for yes, any other key for no.')
    if(ch == 'y' or ch == 'Y'):
        continue
    else:
        break

# not sure when the user will get this correct...
# at least 1 try; could be more!!
while True:
    number = input('Enter a whole number: ')
    if not number.isdigit():
        print('Not a valid number!')
        continue
    number = int(number)
    break
print(f'You entered {number}')

# while loop - countdown
import time
import os

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

i = 10
while i >= 1:
    print(i)
    time.sleep(1) # sleep for 1 second
    clearScreen()
    i -= 1
    
#time.sleep(1)
print('Hapy new year!')