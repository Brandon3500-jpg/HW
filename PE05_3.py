#Question 3 

list = []
for value in range (0,11):
    list.append(value*4)
print(list)

otherlist = []  #i got this line working on the first attempt i was very happy
for value in list:
    otherlist.append(value//2)
print(otherlist)

newlist = otherlist[:]
print(newlist)

for value in newlist:
    newlist.append(value//5)
print(newlist)