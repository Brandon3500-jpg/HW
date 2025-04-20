n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
#this section made a lot more sense to me than the other 2 so far
numbers = []
#to be fair this one is probably the easiest one out of the homework

if n1 == n2: #this added line made me add elif and else:
    print("n1 = n2")

elif n1 < n2:
    while n1 <= n2:
        print(n1, end="|")
        n1 += 1 

else: 
    while n1 >= n2:
        numbers.append(n1)
        n1 -= 1   

for num in numbers:
    print(num, end="|") 



