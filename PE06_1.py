#Questions A-O 
#a = 2
#b = 3 
#c = 0 
print(2 ** 3 == 3 ** 2)

print(2 < 3 or 3 < 2)

print('dog' > 'cat' + 'mouse')

print('Car' < 'Train')

print((2 == 3) and ((2 * 2 < 3 * 3) or (3 < 2) and (2 * 2 < 3)))

print((2 <= 3) or ((2 * 2 < 3 * 3) or (3 < 2) and (2 * 2 < 3)))

print(not ((2 < 3) and (2 < (3 + 2))))

print("small" > "large" and (not 0 ))

print(isinstance(0, int))

print(isinstance(3.14, float))

if (2 < 3 < 0):
    b = 0 + 2
else:
    b = 3 * 2
print(b)

if ('A' in 'apple'):
    print("A as apple." )
else:
    print('Oops, not there.')

x = 6
if (x < 0):
    print('negative')
else:
    if (x == 0):
        print('zero')
    else:
        print('positive')

n = 1
if n <= 9:
    print ("Less than ten.")
elif n == 1:
    print("Equal to one.")

let = input("Enter A, B or C: \n")
let = let.upper()

if (let == 'A'):
    print('\nA, my name is Alice.')
elif (let == 'B'):
    print('\nTo be, or not to be.')
elif (let == 'C'):
    print('\nOh, say, can you see.')
else:
    print('\nInvalid letter.')