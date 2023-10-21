import math
import random
import string

def radians_to_degrees(degrees_input):
    radians = math.pi*degrees_input/180
    return radians

#print(math.pi)

#print( 199999.0/math.inf)

#print( random.randint(0, 10) )

degrees = float(input('Enter the number of degrees: '))

print( math.radians(degrees) )
print( math.cos(math.radians(degrees)))
print( math.sin(math.radians(degrees)))
print( radians_to_degrees(degrees) )
print(degrees)


