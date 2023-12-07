#inheritance
'''class Person:   #parent class
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)

p1=Person("Riya","Singh")
p1.display()

class Teacher(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

t1=Teacher("Vishu","Madaan")
t1.display()'''


#super function 
class Person:   #parent class
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)

p1=Person("Riya","Singh")
p1.display()

class Teacher(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
    def study(self):
        print("You are welcome to study")

t1=Teacher("Vishu","Madaan")
t1.display()
t1.study()
p1.study()

