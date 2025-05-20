class rectangle:#A
    def __init__(self, width = 1, height = 1, O = None):       #B
        self.w = width
        self.h = height


       
    def display(self): #C
                print(f"Width: {self.w}, Height: {self.h}")
            
r1 = rectangle(4, 5)
r1.display()

r2 = rectangle()
r2.display()

print(f"Width of r1 and r2:\n {r1.w} & {r2.w}")
print(f"Height of r1 and r2:\n {r1.h} & {r2.h}")





