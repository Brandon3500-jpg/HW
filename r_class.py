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
