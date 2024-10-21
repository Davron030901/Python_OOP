import math


class Circle(object):
    def __init__(self,x):
        self.x=x
    def area(self):
        return self.x**2*math.pi
    def perimeter(self):
        return self.x*2*math.pi

ball=True
while ball:
    R=float(input("Enter radius of circle: "))
    if R>0:
        obj=Circle(R)
        print(f"Area:{obj.area()} , Length:{obj.perimeter()}")
        ball=False
    else:
        print("Let radius be greater than zero! Enter again. ")