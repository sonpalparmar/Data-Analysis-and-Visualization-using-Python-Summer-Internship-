class Circle:
    def __init__(self,r=1):
        self.radius=r
    def perimiter(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*self.radius*self.radius
  
c1=Circle()
c2=Circle(6)
print(c1.perimiter())
print(c2.perimiter())
print(c1.area())
print(c2.area())
