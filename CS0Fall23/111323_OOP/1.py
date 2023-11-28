class Point:
    """
    Point class to represent and manipulate x and y in 2D coordinates
    """
    count = 0 # class variable/attribute
    
    # constructor to customize the initial state of an object
    # first argument refers to the instance being manipulated;
    # it is customary to name this parameter self; but can be anything
    def __init__(self, xx=0, yy=0):
        """Create a new point with given x and y coords"""
        # x and y are object variables/attributes
        self.x = xx
        self.y = yy
        Point.count += 1 # increment class variable
        
    
    # destructor 
    def __del__(self):
        Point.count -= 1

    def distance_from_point(self,p2):
        return ((self.x-p2.x)**2 + (self.y-p2.y)**2)**0.5

# instantiate an object
def someFunction():
    p = Point()
    p.x = 12
    # what is the access specifier for attributes?
    print('p: x = {} and y = {}'.format(p.x, p.y))
    print("Total point objects = {}".format(Point.count)) # access class variable outside class
    #p.__del__() # call destructor explictly
    p1 = Point(10, 100)
    print("p1: x = {} and y = {}".format(p1.x, p1.y))
    print("Total point objects = {}".format(Point.count))

    # Run this cell few times and see the value of Point.count
    # How do you fix this problem? Use __del__ destructor method.

someFunction()
print("Total point objects = {}".format(Point.count))

p1 = Point()
p2 = Point(0,10)

print(p1.distance_from_point(p2))

