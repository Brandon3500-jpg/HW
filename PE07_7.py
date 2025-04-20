numbers = []

while True:
    ask = int(input("Enter any number, or enter 0 to stop: "))
    if ask == 0:
        break
    numbers.append(ask)

total = sum(numbers)
average = total / len(numbers) if len(numbers) > 0 else 0 #i had to get some help on this one

print(f"sum: {total}")
print(f"average: {average}")
print("number(s) entered: ")

for num in numbers:         #i had to get some help on this one
    print(num, end=" ")

#i could not understand how to make it so the user could also enter decimals