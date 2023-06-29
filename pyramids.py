import random

def control_center():
    while True:
        print("1, SINGLE SIDED PYRAMID")
        print("2, DOUBLE SIDED PYRAMID")
        print("3, RANDOMIZE")
        print("3, EXIT")
        choice = int(input("navigate using 1-2"))
        
        if choice == 1:
            single_sided()
        elif choice == 2:
            double_sided()
        elif choice == 3:
            random_layers()
        elif choice == 4:
            print("YOU HAVE EXITED THE PROGRAM GOODBYE!!")
        else:
            print("Invalid Input, try again")
            break

def single_sided():
    lines = int(input("Enter A Number: "))
    
    for i in range(1,lines + 1):
        print("*"*i)

def double_sided():
    lines = int(input("Enter A Number: "))
    
    for i in range(1,lines + 1):
        print(" "*(lines-i)+"*"*i+" "+"*"*i)
        
def random_layers():
    lines = random.randint(1,50)
    
    for i in range(lines):
        print(" "*(lines-i)+"*"*i+" "+"*"*i)
    
        
control_center()        