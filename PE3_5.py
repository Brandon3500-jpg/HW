#Question 5 
letters = input("Enter a 6 letter word: ")
print("\n")
print("The word you entered is:", letters)
print("\n")
print("The word", letters, "will now be written in reverse order") 
print("\n")
input("Type ok to continue: ")
letters = letters[::-1]
print("\n")
print("Your new word is:", letters)