#Question 2 
age = int(input("What is your age?: ")) #a

if ( age <= 0): #B
    print("Invalid age") 

elif (age < 2): #c
    print("You're a baby")


elif (2 <= age < 4):          #D
    print("You're a toddler")

elif (4 <= age < 13):
    print("You're a kid") #E


elif (13 <= age < 20):
    print("You're a teenager") #F

elif (20 <= age < 65): #G
    print("You're an adult, get a job")

elif (65 <= age): #H 
    print("You're an elder")

#not too bad of a question
