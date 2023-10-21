
def tri_calc(b, h):
    area = 1/2*b*h
    permimeter = b+h
    return area, permimeter

n1 = 4
n2 = 5.5
s3 = "{0} x {1} = {2} and {0} ^ {1} = {3:.2f}".format(n1, n2, n1*n2, n1**n2)
s4 = f"{n1} x {n2} = {n1*n2} and {n1} ^ {n2} = {n1**n2}"
print(s3)
print(s4)

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))

names = ("Corin", "Anna", "John")
ages = (30, 30, 55)
money = ("not enough", "need more", "sdvf")

index = 0
another_layout = "{0:<10}{1:^5}{2:>15}"

print(another_layout.format("Names", "Ages", "Money Stuff"))
for name in names:
    print( another_layout.format(name, ages[index], money[index]) )
    index += 1

tri_stuff = tri_calc(1,1)
print(tri_stuff)
area, perimeter = tri_stuff
print(f"Area = {area}, Perimeter = {perimeter}") 


corin = "Corin"
print(corin[0])
#corin[0] = 'D' string is immutable, cannot reassign value to index

#tri_stuff[0] = 2.0

x = 4
y = 2
xy = (x,y)

print(xy)
x = 10
y = -1
print(xy)