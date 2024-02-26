# while loop - countdown
import time
import os

names = ["Corin", "Tony", "Steve", "Alice"]
names_backwards = names[::-1]  # This is called 'slicing', :: means all, -1 means backwards

for name in names_backwards:
    print(name)

for i in range(3,-1,-1):
    print(names[i])

quit()


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#i = 10
#while i >= 1:
print(list(range(10,1,-1)))
for i in range(10,0,-1):
    print(i)
    time.sleep(1) # sleep for 1 second
    clearScreen()
    i -= 1
    
#time.sleep(1)
print('Hapy new year!')