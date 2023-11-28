# Corin Chepko
# 2/6/23
# Kattis Problem Triarea: Calculates the area of a triangle using the formula Area=1/2*base*height
numbers = input()

height, base = numbers.split()


base = int(base)
height = int(height)

print(1/2*base*height)  #Kattis expects an integer output, so converting answer to int