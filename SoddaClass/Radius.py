import math

class Radius(object):
    def __init__(self,x):
        self.x=x
    def radius(self):
        return (self.x/math.pi)**0.5

ball=True
while ball:
    s=float(input("Enter radius of circle: "))
    if s>0:
        obj=Radius(s)
        print(f"Radius:{obj.radius()}")
        ball=False
    else:
        print("Let radius be greater than zero! Enter again. ")