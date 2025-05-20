from math import pi #a

class circle: #b
    def __init__(self, radius = 1, O = None): #C
        self.radius = radius
    
    def display(self): #D
        print(f"Radius: {self.radius}")
        
    def setRadius(self, r): #E
        self.radius = r

    def getRadius(self): #F
        return self.radius

    def area(self): #G
        return pi * (self.radius ** 2)
    
    def circumference(self): #H
        return 2 * pi * self.radius


