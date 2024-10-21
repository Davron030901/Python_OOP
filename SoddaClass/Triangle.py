class Triangle(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def hypotenuse(self):
        return (self.x**2+self.y**2)**0.5
    def area(self):
        return self.x*self.y*0.5
    def perimeter(self):
        return self.x+self.y+self.hypotenuse()

ball=True
while ball:
    a=float(input("Enter firs leg: "))
    b=float(input("Enter second leg: "))
    if a>0 and b>0:
        obj=Triangle(a,b)
        print(f"Area:{obj.area()} , Perimeter:{obj.perimeter()}")
        ball=False
    else:
        print("Let leg be greater than zero! Enter again. ")