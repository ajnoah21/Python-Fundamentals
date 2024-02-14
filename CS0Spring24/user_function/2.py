def findAreaAndPerimeter(length, width):
    """
    Take length and width of a rectangle.
    Find and return area and perimeter of the rectangle.
    """
    
    area = length*width
    perimeter = 2*(length+width)
    print(area)
    return area, perimeter  # Example of returning multiple values

area, perim = findAreaAndPerimeter(2, 3) # Example of function call returning multiple values
print(f"Area = {area} and Perimeter = {perim}")