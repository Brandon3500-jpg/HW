#Question 2

n = [] #A

n.append(2) #B
n.append(4)
print(n)

extra = [0, 1 ,3] #D
n.extend(extra)
n.sort()
print(n)

n.append(5) #F
print(n)

n.remove(0) #H
print(n)

popped_number = n.pop(n.index(2)) #J
print(n)
print("Our removed number is", popped_number)

popped_number2 = n.pop(n.index(4)) #I
print(n)
print("Our removed number is", popped_number2)

sum = 0 + popped_number + popped_number2 #N
print("Sum of removed numbers is", sum)

n.insert(0, 100) #O
n.insert(6, 9.9)
print(n)

newnum = n.copy()   #P
print("our new list", newnum)
print("our old list"), n.clear() #Q 
print(n)

del n #S
print(n)