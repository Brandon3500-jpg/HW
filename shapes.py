class rectangle:  #A
    def __init__(self, width = 1, height = 1, O = None):       #B
        self.width = width
        self.height = height 
    
    def display(self): #C
        print(f"Width: {self.width}, Height: {self.height}")
            
    def setWH(self, w, h): #D, E
        self.width = w
        self.height = h
    
    def getWH(self): #F, G
        return self.width, self.height 
    
    def area(self): #H
        return self.width * self.height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getWidth(self):
        return self.width 

    def getHeight(self):
        return self.height


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

#THIS TOOK ME 3 HOURS
