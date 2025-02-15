#Question 3 
height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))

BMI = (weight / height**2) * 703
print(f"\n BMI: {BMI:.3f}") 
