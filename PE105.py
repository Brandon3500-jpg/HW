



def createUser(**info): #A        # ** accepts any number of keyword arguments #createUser had to match
    return info

def printuser(user): #B
    for key, value in user.items():
        print(f"{key}: {value}")

def main():
    user1 = createUser(name = 'john', age =  43, job = 'programmer', hobby = 'biking') #C #createUser had to match
    print(user1)                          #NameError: name 'create' is not defined

    user2 = createUser(name = 'sara', age = 24, school = 'QCC', major = 'CSIS')
    print(user2)

main()  #we need this or else nothing will print