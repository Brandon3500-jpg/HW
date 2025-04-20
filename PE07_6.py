ask = int(input("Enter the number of grades in the list: "))
grades = []
# i have NO clue how to do random numbers
# so i decided to let the user put in whatever numbers they wanted
i = 0
while i < ask :
    grade = int(input("Enter a grade 1-100: "))
    grades.append(grade)
    i += 1  

d = int(input("Please enter a passing grade: "))
passgrades = []

while d <= 100:
    passgrades.append(d)
    d += 1

print("Original List:", grades )
print("Updated List:", passgrades)