#there was a LOT of back and forth on this one
stuinfo1 = {'name' : 'johm', 'gpa' : 3.0}
stuinfo2 = {'name' : 'Алек', 'gpa' : 4.0}
stuinfo3 = {'name' : 'eric', 'gpa' : 2.5}

stuClass = []

stuClass.append(stuinfo1)
stuClass.append(stuinfo2)
stuClass.append(stuinfo3)

print(stuClass)

for student in stuClass: #c
    print(student['name'])

for grade in stuClass: #D
    print(grade['gpa'])

stuinfo3.update({'gpa' : 4.0}) #E
print(stuClass)

print("\n")

x = ['alex'] #F
y = [3.5]
new = {'name' : x[0], 'gpa' : y[0]}
stuClass.append(new)
print(stuClass)

print("\n")

print("all the updated info")
for student in stuClass: #g
    print(student['name'], str(student['gpa']).rjust(15)) #this last line was a bit confusing

