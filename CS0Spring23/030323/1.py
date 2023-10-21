# lists with elements of different types
list1 = ["hello", 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]

print(list1[3][1][1]) #prints the 4th element of list, then the 2nd element of the list that refers to, then the 2nd element of the tuple ('hi,'world')

list1[0] = "John"

print(list1)

for l in list1:
    print(l)

# Exercise: create a list of even numbers between 1 and 20 inclusive
print(list(range(0,22,2)))

# Exercise: create a list of odd numbers between 1 and 20 inclusive
print(list(range(1,21,2)))

# Exercise: create a list of numbers from 20 and 1 inclusive
print(list(range(20,0,-1)))

horsemen = ["war", "famine", "pestilence", ["death"]]
print('war' in horsemen)

list2 = ['some', 'more', 'things']

list3 = list1 + list2
print(list3)
list4 = [1]*10 #creates a list of 10 '1's
print(list4)

import string
alphas = list(string.ascii_lowercase)
print(alphas)
print(alphas[::2]) #prints every 2nd element

achar = ','
numList = list(string.ascii_lowercase)
del numList[10]
returned = achar.join(numList)
print(numList)
print(returned)