

def nameformat(first, last, middle = None): #A #Capital N in none
    if middle is not None:
        return f"{last.title()} {first.title()} {middle[0].upper()}"   
        
        
        
        #Jones Henry <built-in method upper
        #of str object at 0x00007FF848290160>
        #dont forget the ()

    else:
        return f"{last.title()} {first.title()}"


def main():
    one = nameformat(first = 'james', last = 'bond')
    two = nameformat(first = 'henry', middle = 'indiana', last = 'jones')
    
    print(one) #these print statements had to be indented
    print(two)

main()