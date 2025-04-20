
#this one wasnt too terrible of a question
rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}

ask = int(input("Enter the # of years in the school (1-4): "))

if ask in rank:
    print(rank[ask])

else: 
    print("Invalid Years")