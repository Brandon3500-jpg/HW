


def nameformat(first, middle, last): #A
    print(f"{first.title()} {middle[0].upper()} {last.title()}")
    

def main(): #B
    nameformat('john', 'stu', 'smith') 
    nameformat(last = 'kennedy', first = 'john', middle = 'fitzgerald')

main() #C