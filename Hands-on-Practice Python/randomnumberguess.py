def lottery(num,x):
    if(num==x):
        print("You are first winner ")
        return
    digit1=list(map(int,(str(x).split())))
    print(digit1)
    digit2=list(map(int,"".join(str(num).split())))
    print(digit2)
    if(len(digit1)==len(digit2)):
        print("Second runner up ")
        return
    for i in digit1:
        for j in digit2:
            if(i==j):
                print("Third runner up")
                return
            
import random
ran=random.randint(1,500)
num=int(input("Enter the number from 1 to 499"))
lottery(num,ran)
