#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m=int(input("Set your password"))
c=m
attempt=1
n=int(input("Enter your password"))
for i in range(0,2):
    if c==n:
        print("Entered password is correct")
        break
    elif c!=0:
        print("enter password is not correct")
        print("try again")
        n=int(input("enter password again"))
        attempt+=1
        if c==n:
            print("Entered password is correct")
            break
            
        if attempt==3:
            print("3 incorrect attempts")
            print("try again later")
                                     
                                 
    


# In[ ]:


#question3 factorial using recusion
def recur(n):
    if n==1:
        return 1
    else:
        return n*recur(n-1)
n=int(input("Enter number"))    
if n==0:
    print("The sum is 0")
else:
    print("the sum of",n,"=",recur(n))


# In[ ]:


#question 4 fibonacci series
first=0
second=1
n=int(input("Enter the range you want"))
for i in range(0,n):
    print(first,end=" ")
    first,second=second,first+second 

    

