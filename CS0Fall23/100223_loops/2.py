'''
Looping through strings or containers
'''

n = '1234'
print(len(str(n)))
digits = 0
for i in range(len(n)):
    if(n[i].isdigit()):
        digits+=1

print(digits)

digits = 0
for character in n:
    if(character.isdigit()):
        digits += 1

print(digits)

names = input("Enter some names separtated by a space").split()
print(names)
for name in names:
    print(name)
    pass #empty code, does not pass anything, just a filler
    print(name)

def addtwo():
    pass # just filler until code is put in here

print('pritn')

