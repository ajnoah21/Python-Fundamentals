# iterating over tuples, or lists

def funct1(l):
    l[0] = 2

def funct2(t):
    t[0] = 5

star = ("Hi", "Everyone")
star2 = (1,3)
stars = star,star2

for i in range(len(star)):
    print(star[i], star2[i])

print("Now with tuple iteration:")

for star,star2 in stars:
    print(star,star2)

l = [2,4]
t = (2,4)
funct1(l)
print(l[0])
#funct2(t) #tuples cannot be modified by a function