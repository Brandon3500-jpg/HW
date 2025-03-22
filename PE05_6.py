#A-E

""""
before 


fruits = ["apple", "banana", "cherry"]
for item in fruits
print(item)
"""
fruits = ["apple", "banana", "cherry"] #after
for item in fruits:      #forgot : and an indent in print(item)
    print(item)

for i in range (1, 4):      #im assuming they wanted their answered to be 
    print("\t", i + 2**i)   #tabbed

#Why is there no output when you run the code?
for j in range (1, 6, -1):
    print(j)
# i think its because we are asking it to start
# at 1 and stop at 6 going down but it cant do that
#because 6 is greater than 1 

#How to display all the elements in uppercase?
"""letters = ['a', 'b', 'c']
for letter in letters:
    letter = letter.upper()
print(letters)"""

letters = ['a', 'b', 'c']      #this one was a little hard
for value in range(len(letters)):
    letters[value] = letters[value].upper()
print(letters)

"""fruits = ('apple', 'banana', 'cherry')
print(fruits)
fruits[0] = 'orange'
fruits.append('pineapple')
print(fruits)"""

fruits = ['apple', 'bannana', 'cherry']
print(fruits)
new_fruit = 'orange'
fruits.append('pineapple')
fruits.insert(0, new_fruit)
print(fruits)

#im assuming they wanted orange to be the first
#thing in the list and wanted pineapple in the end