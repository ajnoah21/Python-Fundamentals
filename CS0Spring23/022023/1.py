#while loop demo

user_input = 'y'

while user_input == 'y':
    print("Again")
    user_input = input('Enter something') # Always executes at least once
    if user_input == 'b':
        break   # only executes if 'b' is entered
    elif user_input == 'c':
        continue    # only executes if c is enetered
    print("Agamin again!")  # only executes is y is entered
else:
    print("No break.")  # only executes when c is entered

print("All done!") # Always executes

print("A while loop")
i = 0
while i < 10:
    print(f"{i}")
    i+=1

print("now a for loop")
for i in range(11, 1, -1):
    if(i == 10):
        continue
    print(f'{i}')
    if(i == 3):
        break
else:
    print("No break") # will never execute

if( i == 3):
    print("Break")
    




