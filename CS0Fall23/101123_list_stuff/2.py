names = ['a','b','c','z','d']
mlist = list
list = [8,9]
count = mlist(range(10))
print(count)

#for i in range(5):
#    names.append(input('Enter a name: '))
c_names = names # does not copy content into new list, just refers to sames list by different name
c_names = names.copy()
print(c_names is names)

del(names[1])
#names.remove('john')
names.sort()
print(names)
print(c_names)

def add(n1,n2):
    return n1+n2

n1=5
n2=3
assert add(n1,n2) == 8

    