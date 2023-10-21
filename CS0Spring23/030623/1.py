a = [1,2,3]
b=a
b=[1,2,3]

print(a)
print(b)

print(a is b)

a[0] = 10

print(a)
print(b)

# How do you actually clone lists - do a deep copy?
c = a[:] # easy way shallow copy
d = a.copy() # shallow copy
print( c is a)
print( d is a)

import copy
e = copy.deepcopy(a)

print(e is a)
print(a,c,d,e)

a[0] = 25
print(a,c,d,e)