number = int(input("type a number:")) #asks for user input and stores it as an int

for i in range(1,number+1): #makes sure it starts at 1 and ends at the number we types since we start counting at 0
    print(" "*(number-i)+"*"*i+" "+"*"*i)#when you multipy a string it repeats it