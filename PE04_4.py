#Question 4 

grades = []
grades.append(80)
grades.append(50)
grades.append(85)
grades.append(50)
grades.append(100)
print(grades)

total_grades = grades[0] + grades[1] + grades[2] + grades[3] + grades[4]

average = total_grades / len(grades)
print(f"Average is: {average:.2f}")

method_1 = grades.copy()
method_1.pop(1)
method_1.pop(2)
print("Method 1 using the .pop function gives us:", method_1)

method_2 = grades.copy()
method_2.remove(50)
method_2.remove(50)
print("Method 2 using the .remove function gives us:", method_2)

print("Current list:", grades)
print(f"Average of grades: {sum(grades) / len(grades):.3f}")

print("Updated list", method_1)
print(f"Updated Average: {sum(method_1) /len(method_1):.3f}")
      