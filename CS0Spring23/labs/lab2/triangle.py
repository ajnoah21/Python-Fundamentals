# Created by: Corin Chepko
# Date: 2/7/23
# Program info: Calculate the area and perimeter of a triangle using
# Heron's formula.

# Algorithm Steps:
# input 3 sides of triangle, they should probably be floats
# Use Heron's formula to calculate area:
# First calculate semiperimeter as 1/2*(a+b+c)
# Area = sqrt( semi*(semi-a)*(semi-b)*(semi-c) )
# Add sides to calculate perimeter
# Maybe check to see if it's a real triangle to extra credit:
# if (side1+side2) < side3 or 

import math

side1 = float(input('Enter the length of side1: '))
side2 = float(input('Enter the length of side2: '))
side3 = float(input('Enter the length of side3: '))

print( "side1 = ", side1)
print( "side2 = ", side2)
print( "side3 = ", side3)

if (side1+side2) < side3 or (side3+side2) < side2 or (side3+side2) < side1:
    print("Invalid triangle.")
else:
    perimeter = side1+side2+side3
    semi_perimeter = perimeter/2
    area = math.sqrt( semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3) )

    print('The perimeter is ', perimeter)
    print('The area = ', area)

