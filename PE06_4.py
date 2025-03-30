#Question 4 

current_users = ["Melanie", "Fermin", "Bernice", "Dante", "Jolene"]
ask = input("Enter a username: ")

if ask.lower() in [user.lower() for user in current_users]: #this is the ONLY line of code i needed help with
    print(f"Sorry {ask.title()}, that name is taken")
   
else: 
    print(f"Great, {ask.title()}, is still available")
current_users.append(ask)
print(current_users)

#this was very understanble and pretty complicated at the same time
#if that even makes sense