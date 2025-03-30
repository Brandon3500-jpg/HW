#Question 6 

'''
n = eval(input("Enter a number: "))
if n == 7:
    print("The square is", n*2)
'''
n = eval(input("Enter a number: ")) #error was no ==
if n == 7:
    print("The square is", n*2)

'''
n = 6
if n > 5 and < 9:
    print("Yes")
else:
    print("No")
'''

n = 6
if n > 5 and n < 9: #error was no n before < 9
    print("Yes")
else:
    print("No")

'''
major = "Computer Science"
if major == "Engineering Technology" Or "Computer Technology")
    print("Yes")
'''

major = "Computer Science" #error was a capital o in or and a parenthesis instead of a : at the end of line 33
if major == "Engineering Technology" or "Computer Technology":
    print("Yes")

'''
a, b = 1, 1.0
if a == b:
    print("same") 
'''

a, b = 1, 1.0 #error was no == 
if a == b:
    print("same")  