#passing list as an argument
def add(a,b,d):
    c=a+b
    print(d)
    return c

print(add(3,4,['apple','mango']))

#function call as an argument
def x():
    x=3
    return x
def y(p):
    return p

print(y(x()))


#pass statement
def func():
    pass
func()

#nested functions
def a():
    print("hello")
    def b():
        print("students")
    b()
a()


def func1(a,b):
    c=a+b
    return c
def func2(c,d=2):
    result=c*d
    return result
print(func2(func1(3,2)))

# Recursive function
#function is calling itself

def display():
    print("hello")
    display()
#display()

#recursion example
'''def recur(k):
    if(k>0):
        result=k+recur(k-1)
        print(result)
    else:
        result=0
    return result
recur(6)'''

#closure
def num1(x):
    def num2(y):
        return x+y
    return num2
print(num1(20)(5))


#sets
first_set={"apple","mango","litchi"}
print(first_set)

first_set={"apple",3.0,"apple",True,1,"mango","litchi"}
print(first_set)
print(len(first_set))
print(type(first_set))
newset=set((1,2,3,'abc',4,5))
print(newset)

for i in newset:
    if (i=='abc'):
        print("found")
    else:
        print("missing")


for i in newset:
    if (i=='abc'):
        print("found")
    else:
        pass  #multiple missing print will be avoided


newset.add(90.2)
print(newset)
first_set.update(newset)
l=['choclate','candies','chips']
first_set.update(l)
print(first_set)
first_set.discard('chips') #discrad/remove
print(first_set)
first_set.pop()
print(first_set)
newset.clear()
print(newset)
del newset


#join two sets - union()
set1={1,2,3}
set2={3,4,5}
set3=set1.union(set2)
print(set3)


#intersection_update() #update the existing set
#set1.intersection_update(set2)
print(set1)


#intersection() #create the new set
set3=set1.intersection(set2)
print(set3)

#remove duplicates symmetric_difference_update()
set1.symmetric_difference_update(set2)
print(set1)

#new set- symmetric_difference()






    
    

