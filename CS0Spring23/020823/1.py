some_string = chr(0x2103)

print(type(some_string))
print(some_string)

print(  bin( ord(some_string) ) )

seconds = 3601

print(seconds//60, seconds%60)

minutes, seconds_r = divmod(seconds, 60)
print(minutes, seconds_r)

hours, minutes_r = divmod(minutes, 60)

print(hours)
print(minutes_r)
print(seconds_r)

a = 2
b = 3

print( a**b )
print( pow(a,b) )

c = 3
d=4
e=5

print(a,b,c,d,e,sep=',',end=';')
print(a,b,c,d,e)

