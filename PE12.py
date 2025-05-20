# 1. File Reading

def read_with_loop(filename):
    print("Using Loop ------")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

def read_with_list(filename):
    print("Using List ------")
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

# 2. File Writing

def create_file_one():
    with open("PresidentOne.txt", 'w') as file:
        file.write("George Washington\n")

def create_file_two():
    with open("PresidentTwo.txt", 'w') as file:
        file.write("John Adams\n")
        file.write("Thomas Jefferson\n")

def create_uspres_file():
    with open("USPres.txt", 'w') as file:
        file.write("George Washington\n")
        file.write("John Adams\n")
        file.write("Thomas Jefferson\n")

# 3. File Appending

def append_to_file():
    with open("USPres.txt", 'a') as file:
        file.write("James Madison\n")


# Running all functions

create_file_one()
create_file_two()
create_uspres_file()     # <- Add this to write the base content
append_to_file()
read_with_loop("USPres.txt")
read_with_list("USPres.txt")