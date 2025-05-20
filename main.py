from r_class import rectangle

r1 = rectangle(4, 5)
r1.display() #2

print("area of r1:", r1.area())

print("\n")

r2 = rectangle() #3
r2.display()
print("area of r2: ", r2.area())

print("\n")

r2.setWidth(6) #4
r2.setHeight(6)

r2.display()

print("new width:", r2.getWidth()) #5
print("new height:", r2.getHeight()) #6

print("area:", r2.area())











#r = rectangle         # This assigns the class itself, not an object
#r.display()           # Error: you're calling display() on the class, not on an instance
#Traceback (most recent call last):
#File "c:\Users\Brandon\Downloads\TEST\main.py", line 3, in <module>
#r1 = rectangle(4, 5)
#typeError: 'module' object is not callable. Did you mean: 'rectangle.rectangle(...)'?

#had to from rectangle import rectangle 
