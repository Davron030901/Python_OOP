class Triangle(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def perimeter(self):
        return self.x+self.y+self.z
    def everage(self):
        return self.perimeter()/2
    def area(self):
        return (self.perimeter()*(self.everage()-self.x)*(self.everage()-self.y)*(self.everage()-self.z))**0.5

ball=True
while ball:
    a=float(input("Enter firs side: "))
    b=float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    if a>0 and b>0:
        obj1=Triangle(a,b,c)
        obj2=Triangle(a,b,c)
        obj3=Triangle(a,b,c)
        print(f"Area:{obj3.area()} , Perimeter:{obj1.perimeter()}, HalfPerimeter:{obj2.perimeter()}")
        ball=False
    else:
        print("Let leg be greater than zero! Enter again. ")