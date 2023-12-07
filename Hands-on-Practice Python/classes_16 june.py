#classes and objects

'''class Fruits:
    print("fruit")

mango=Fruits()#object1
grapes=Fruits()#object2
melon=Fruits()#object3'''


'''class Fruits:
    mango=1
    grapes=3
    melon=8
fruit1=Fruits()#object1
fruit2=Fruits()#object2
fruit3=Fruits()#object3
print(fruit1.mango)
print(fruit1.grapes)'''


#__init__() initializer


class Person:
    def __init__(p1,n,a,s):
        p1.name=n
        p1.age=a
        p1.status=s
o1=Person("abhi",23,'single')
o2=Person("Kabir",22,'single')
print(o1.age)
print(o2.age)
o1.age=27
print(o1.age)
        




















