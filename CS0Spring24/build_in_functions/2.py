import math
import random


print('max=', max(100, 8.9, 999, 1000.5, -2000))
print('min=', min(100, 8.9, 999, 1000.5, -2000))
print('2 to the 3rd power = ', pow(2,3))
print('2 to the 3rd power = ', 2**3)

print('hi', 'hello', end='=') #instead of a newline after the print this puts an '='
print('hi', 'hello', sep='', end='=') #instead of separating arguments by space, separate by nothing

print()
num1 = 1
num2 = 4
num3 = -6
print(num1,num2,num3, sep='+', end='=')
print(num1+num2+num3)

degrees = float(input("Enter and angle: "))
print("cos(",degrees,')=',math.cos(degrees*math.pi/180))
print("sin(",degrees,')=',math.sin(degrees*math.pi/180))

print(math.gcd(10, 5))
print("\nRandom numbers:")

for i in range(10): # this executes the code below 10 times
    random_number = random.randint(0, 10)
    print(random_number)

print()
print(list(range(11)))


