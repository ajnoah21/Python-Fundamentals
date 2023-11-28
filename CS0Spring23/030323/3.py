number_items = int(input("Enter the number of inputs."))

names = []

for i in range(number_items):
    names.append(input("Enter a name:"))

print(names)

a=2
b=4
list1 = [a,b]
list2 = [a,b]

list1.append(3)

print(list2)

print(list1 is list2)