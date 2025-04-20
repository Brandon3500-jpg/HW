#i still dont fully understand dictionaries compared to everything else we have learned


stuinfo = {'name' : 'john', 'gpa' : 2.5, 'age' : 19}
for key, value in stuinfo.items():
    print(key, value)

print("\n")

stuinfo.update({'gpa' : 4.0})
print(stuinfo)

print("\n")

for key in stuinfo.keys(): #D
    print(key, stuinfo[key])

print("\n")

stuinfo.update({'major': 'CS'}) #E

for value in stuinfo.values(): #F
    print(value)

out = stuinfo.pop('gpa')


del stuinfo['age']
print(stuinfo)