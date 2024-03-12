import math

class Geometry(): 
    def __init__(self, x = 0.0, y = 0.0): 
        self.x = x 
        self.y = y 
 
    def computeArea(self): 
        pass
 
    def computePerimeter(self): 
        pass
 
    def move(self, deltaX, deltaY): 
        self.x += deltaX 
        self.y += deltaY 
 
    def __str__(self): 
        return "Abstract class Geometry should not be instantiated and derived classes should override this method!"

class Circle(Geometry): 
    def __init__(self, x = 0.0, y = 0.0, radius = 1.0): 
        super(Circle,self).__init__(x,y) 
        self.radius = radius 
 
    def computeArea(self): 
        return math.pi * self.radius ** 2
 
    def computePerimeter (self): 
        return 2 * math.pi * self.radius 
 
    def __str__(self): 
        return "Circle with coordinates {}, {} and radius {}".format(self.x, self.y, self.radius)

class Rectangle(Geometry): 
    def __init__(self, x = 0.0, y = 0.0, width = 1.0, height = 1.0): 
        super(Rectangle, self).__init__(x,y) 
        self.width = width 
        self.height = height 
 
    def computeArea(self): 
        return self.width * self.height 
 
    def computePerimeter (self): 
        return 2 * (self.width + self.height) 
 
    def __str__(self): 
        return "Rectangle with coordinates {}, {}, width {} and height {}".format(self.x, self.y, self.width, self.height )
    
class Pentagon(Geometry):
    def __init__(self, x = 0.0, y = 0.0, width = 1.0, height = 1.0):
        super(Pentagon, self).__init__(x,y) 
        self.width = width 
        self.height = height
    
    def computeArea(self): 
        return (self.computePerimeter() * self.height) / 2
 
    def computePerimeter (self): 
        return 2 * self.width
 
    def __str__(self): 
        return "Pentagon with coordinates {}, {}, width {} and height {}".format(self.x, self.y, self.width, self.height )

circle1 = Circle(10,4,3) 
print(circle1) 
print("The circle1's area is {:.3f}".format(circle1.computeArea())) 
circle1.move(3,-1) 
print(circle1)
print()

rectangle1 = Rectangle(10,10,3,2) 
print(rectangle1) 
print("The rectangle1's area is {:.3f}".format(rectangle1.computeArea()) )
rectangle1.move(2,2) 
print(rectangle1) 
print()

pentagon1 = Pentagon(15, 15, 4, 4)
print(pentagon1)
print("The pentagon1's area is {:.3f}".format(pentagon1.computeArea()) )
pentagon1.move(1, 2)
print(pentagon1)
print()