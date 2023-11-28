import math

'''
Lists Examples
'''
'''
num1, num2, num3 = input("Enter three numbers separated by a space:\n").split()
print(num1, num2, num3)

numbers = input("Enter numbers separated by a space:\n").split()
print(type(numbers))
print(numbers)
num1, num2, num3 = numbers # unpacking a list, must have same # of variables as list items
print(num1, num2, num3)'''

# There will be N numbers, then input those N numbers into a list
N = int(input("Enter how many numbers: "))
alist = list() # make an empty list
print(len(alist))
average = 0
for i in range(N):
    num=input()
    alist.append(num)
    average = average + int(num)
print("Average = ",average/N)

average = 0
blist = map(int,input(f"Enter {N} numbers separated by a space:\n").split())
for num in blist:
    average = average + num

print("Average of numbers is: ", average/N)