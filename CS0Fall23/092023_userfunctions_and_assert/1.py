'''
User defined functions examples and assert examples
9/20/23
'''

# FIXME Write a function that divides 2 numbers and returns the answer
def div2(num1, num2):
    answer = num1/num2
    print(num1, "divided by", num2, "=", answer)
    return answer

def test():
    assert div2(1,2) == 0.5, "Should be 0.5"
    assert div2(10,5) == 2

def findAreaAndPerimeter(length, width):
    """
    Take length and width of a rectangle.
    Find and return area and perimeter of the rectangle.
    """
    
    area = length*width
    perimeter = 2*(length+width)
    return area, perimeter

print("Hello")
a=1
b=3
ans = div2(a,b)
print(ans)

test()

print("Goodbye")

area, perimeter = findAreaAndPerimeter(4, 3)
print(area)
print(perimeter)
