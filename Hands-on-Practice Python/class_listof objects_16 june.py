class Circle:
    def __init__(self,r=1):
        self.radius=r
    def perimeter(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*self.radius*self.radius
  
l=[]
for i in range(0,10):
    if (i==1):
        l.append(Circle(13))
    else:
        l.append(Circle(i))

for obj in range(0,len(l)):
    print("perimeter of circle",obj,l[obj].perimeter())
    print("area of circle",obj,l[obj].area())
    

