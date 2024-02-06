#chr return character from unicode number
print(chr(65))
print(chr(97))
print(chr(8364))
print(chr(176))

#ord returns unicode from given character
print(ord('°'))

a_number = 5
print(id(5))
a_number = 6
print(id(a_number))
print(id(6))

#order of calculations...
y=15
x=2*y
print(x)
y=30
x=2*y
print(x)


#divmod vs / and %
time = int(input("Enter in a time in minutes: "))
#print(divmod(time, 60)) # Return (quotient, remainder)
hours, minutes = divmod(time, 60) #returns integer division and remainder
one_big_string = "time = " + str(hours) + " minutes " + str(minutes)
print(one_big_string)

hours = time//60 #integer division (no decimals)
minutes = time%60 #remainder division (modulus)
print("time =", hours, "minutes", minutes)

