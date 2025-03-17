#Question 2 
x = list(range(1, 101))
print(x)

print()

newlist = [num for num in x if num % 2 == 0] #this one was tricky
print(newlist[:5]) 
print()

print(newlist[-5:])
print()

print(newlist[9:15])