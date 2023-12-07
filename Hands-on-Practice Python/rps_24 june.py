#Rock paper scissor
#R vs S -> R
#R vs P -> P
#P vs S -> S
import random
print("Enter 1 for rock")
print("Enter 2 for paper")
print("Enter 3 for scissor")
choice=int(input("Enter your selection"))
if(choice!=1 and choice!=2 and choice!=3):
    print("enter valid choice")
elif(choice==1):
    choice='rock'
    print("your choice is",choice)
elif(choice==2):
    choice='paper'
    print("your choice is",choice)
elif(choice==3):
    choice='scissor'
    print("your choice is",choice)
print("Now its turn of computer")
system=random.choice(['rock','paper','scissor'])
print(system)


    
    
