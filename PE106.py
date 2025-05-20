def average(*grades): #a
    return sum(grades) / len(grades)


def main():  #b
    r = average(95, 87, 83, 74)
    x = -12
    y = 44
    a = average(x, y)

    print(f"average of (95, 87, ,83, 74): {r:.2f}") #print statements needed to be inside of def
    print (f"x = {x}, y = {y}")
    print(f"average of (x, y): {a:.2f}")


main()