#list-mutable , []
#tuples- immutable, ()

'''fruits=('apples','grapes','oranges')
print(fruits)
meats=('fish','poultry')
print(meats)
food=meats+fruits
print(food)
veggies=['beans','capsicum']
#tuple(veggies)
print(tuple(veggies))
candies=('marshmallow',)
print(candies)'''

'''#functions
import math
print(math.sqrt(24))
#user-defined functions

def display():
    print("hello")

#display()
#display()
#display()

for i in range(10):
    display()

#positional arguments
    
def result(name,math,eng,hindi):
    result=math+eng+hindi
    result=(result/300)*100
    print('result of',name,'=',format(result,'.2f'),'%')

result('sumit',90,67,79)
result('Amit',70,60,75)'''

'''#return statement

def addition(a,b):
    c=a+b
    return c
def multiplication(x,y):
    z=x*y
    return z
addition(2,3)
#multiplication(addition(4,5),7)
print(multiplication(addition(4,5),7))

#boolean functions

def odd(x):
    if(x%2!=0):
        return True
    else:
        return False

print(odd(33))
print(odd(34))

#positional arguments
#default arguments
#keyword arguments

#variable length arguments #arbitrary positional arguments
#arbitrary keyword arguments

#default arguments
def add(a,b=2):
    print(a+b)
add(3)
add(3,12)

#keyword argument- no need to maintain the same order
#kwarg=value

def add(a,b=4,c=3):
    print(a+b+c)
add(b=10,c=15,a=20)

#default arguments should follow non-default arguments
def add(b,c,a=5):
    return a+b+c
print(add(6,7))

#keyword arguments should follow positional arguments

def add(a,b,c):
    return a+b+c

print(add(a=10,3,4)
#print(add(3,4,10))

#all keyword arguments passed must match one of the arguments accepted
#by the function and their order is not important

#print(add(a=10,b1=5,c=12))
print(add(a=10,c=12,b=4))'''

#no arguments should recieve a value more than once.


#arbitrary positional
'''def add(*numbers):
    print(numbers)
    sum=0
    for i in numbers:
        sum=sum+i
    return sum

print(add(1,2,3,4,5,6,78,2,4,5,6,3,5))

def students(*n):
    print(n)
students('amit','sumit','abhi','riya')'''

#arbitrary keyword

def students(**n):
    print(n)
students(n3='amit',n2='sumit',n1='abhi')









    






    




