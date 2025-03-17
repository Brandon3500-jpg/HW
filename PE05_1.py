#A-D

a = list(range(5))
print(a)
print("\n")

b = []
for i in range (5):
    b.append(i)
print(b) 
print("\n")

x = list(range(-10, 10))
print(x)
print(min(x), max(x), sum(x))
print("\n")

even_num = list(range(2, 11, 2))
print(even_num[0], even_num[-1])
print("\n")

#E-G
odd_num = []          #i was very proud of this one
for num in range(1, 10, 2):
      odd_num.append(num)
print(odd_num)
print("\n")

cubes = []               #some of this was taken from ex3
for value in range(1,11):
    cubes.append(value**3) 

for whatever in cubes[:11]:
    print(f"{whatever}")

print()

for whatever in cubes[:11]:
    print(f"{whatever}", end = "|") 



