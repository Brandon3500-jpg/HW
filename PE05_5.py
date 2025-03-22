#question 5

first = int(input("Enter a range: "))
print("")
x = list(range(1, first + 1))

integer = int(input("Enter an integer: "))
print("")

print(f"Multiplication table of {integer}")
for num in x:  
    print(f"{integer} X {num} = {integer * num}") 

"""    just putting this here
for future use 

instead of using an f string

print("{} X {} = {}".format(integer, num, integer * num))

print(integer, "X", num, "=", integer * num)

"""