import math

class Circle:
    "Class representing a Circle"
    
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self):
        return math.pi * self.radius * self.radius
        
my_circle = Circle(10)
print(my_circle)
your_circle = Circle(20)
print(your_circle)
