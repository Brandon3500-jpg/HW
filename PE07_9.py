lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
incVal = int(input("Enter a number to increment by: "))

while lower <= upper:
    print(lower)
    lower += incVal

for x in range(lower, upper + 1, incVal): #i had to get some help on this one
    print(x)                              #have not used the range function in a while
