def area_per(x,y):
    return x*y,2*x+2*y # creates and returns a tuple

record1 = ("Name", 3.5, [1,2,3])
record2 = "name2",3.3,[12,4]

print(record1, type(record1))
print(record2, type(record2))

area,perimeter = area_per(2,3)
print(f"Area = {area}, Perimeter = {perimeter}")

#record1[0] = "Corin" tuples do not allow item assignment


translation = {'A':'B','B':'C','C':'D'}

code = "abcbcaa"
out = ""
for ch in code.upper():
    out += translation[ch]

print(code)
print(out)

keys = list(translation.keys())
print(keys)
print(list(translation.values()))
for key in translation.keys():
    print(key, translation[key])

key = input("Enter a character and I'll translate it: ")
#if(translation.get(key) != None):
if key in translation:
    print(translation[key])
else:
    print("That key does not exist.")

print(translation.items())
for key,value in translation.items():
    print(key,value)