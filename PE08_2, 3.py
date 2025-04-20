#questions 2 and 3 will be here since they are short

keys = ['ten', 'twenty', 'thirty']
values = [10, 20, 30]

other = dict(zip(keys, values))
print(other)

dict1 = {'ten' : 10, 'twenty' : 20, 'thirty' : 30}
dict2 = {'thirty' : 30, 'forty' : 40, 'fifty' : 50}
dict1.update(dict2)
print(dict1)