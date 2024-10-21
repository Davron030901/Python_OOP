class Area(object):
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
    def distanceA(self):
        return ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**0.5
    def distanceB(self):
        return ((self.x3-self.x2)**2+(self.y3-self.y2)**2)**0.5
    def distanceS(self):
        return ((self.x1-self.x3)**2+(self.y1-self.y3)**2)**0.5
    def average(self):
        return (self.distanceA()+self.distanceB()+self.distanceS())/2
    def area(self):
        if (self.distanceA()+self.distanceB())>self.distanceS() and (self.distanceS()+self.distanceB())>self.distanceA() and (self.distanceA()+self.distanceS())>self.distanceB():
            return (self.average()*(self.average()-self.distanceA())*(self.average()-self.distanceB())*(self.average()-self.distanceS()))**0.5
        else:
            return f"This is liner not a triangle , this is length is {self.distanceA()+self.distanceB()}"


x1=float(input("Enter firs x: "))
y1=float(input("Enter firs y: "))
x2 = float(input("Enter second x: "))
y2 = float(input("Enter second y: "))
x3 = float(input("Enter third x: "))
y3 = float(input("Enter third y: "))
obj=Area(x1,y1,x2,y2,x3,y3)
print(obj.area())