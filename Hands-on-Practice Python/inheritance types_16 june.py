# 5 types of inheritance in python
#1. single inheritance- one parent, one child
#2. multiple inheritance
'''class Parent1:
    def __init__(self):
        self.message1="parent1"
        print(self.message1)
class Parent2:
    def __init__(self):
        self.message2="parent2"
        print(self.message2)
class Child(Parent1,Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
    def fun_child(self):
        print("I am from child class")
        print(self.message1)
        print(self.message2)
p1=Parent1()
c1=Child()
c1.fun_child()'''

#3. Multilevel Inheritance

class Parent:
    def __init__(self,name):
        self.name=name
class Child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name)
        self.age=age
class Grandchild(Child):
    def __init__(self,name,age):
        Child.__init__(self,name,age)
    def display(self):
        print(self.name)
        print(self.age)
g1=Grandchild('abhi',23)
g1.display()

