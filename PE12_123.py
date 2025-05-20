# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def read_and_display_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # Display each line, removing trailing newline characters
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An error occurred while reading the file.")

# Usage example:
filename = input("Enter the name of the file to read: ")
read_and_display_file(filename)

#PE11_2

def create_file_with_content(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File '{filename}' created successfully with the provided content.")
    except IOError:
        print("An error occurred while creating the file.")

def create_empty_file(filename):
    try:
        with open(filename, 'w') as file:
            pass  # Creating an empty file
        print(f"Empty file '{filename}' created successfully.")
    except IOError:
        print("An error occurred while creating the file.")

# Usage example:
filename_with_content = input("Enter the name of the file to create (with content): ")
content = input("Enter the content for the file: ")
create_file_with_content(filename_with_content, content)

filename_empty = input("Enter the name of the empty file to create: ")
create_empty_file(filename_empty)

#PE!!_3
def append_lines_to_file(filename, lines):
    try:
        with open(filename, 'a') as file:
            file.writelines(lines)
        print("Lines appended successfully to the file.")
    except IOError:
        print("An error occurred while appending lines to the file.")

# Usage example:
filename = input("Enter the name of the file to append lines: ")
lines = []
num_lines = int(input("Enter the number of lines to append: "))

for i in range(num_lines):
    line = input(f"Enter line {i+1}: ")
    lines.append(line + '\n')

append_lines_to_file(filename, lines)
