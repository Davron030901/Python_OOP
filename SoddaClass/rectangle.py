class Rectangle(object):
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        self.x4=x4
        self.y4=y4
    def distanceA(self):
        return ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**0.5
    def distanceB(self):
        return ((self.x3-self.x2)**2+(self.y3-self.y2)**2)**0.5
    def distanceC(self):
        return ((self.x4-self.x3)**2+(self.y4-self.y3)**2)**0.5
    def distanceS(self):
        return ((self.x1-self.x4)**2+(self.y1-self.y4)**2)**0.5
    def distanceD1(self):
        return ((self.x2-self.x4)**2+(self.y2-self.y4)**2)**0.5
    def distanceD2(self):
        return ((self.x1-self.x3)**2+(self.y1-self.y3)**2)**0.5
    def area(self):
        if self.distanceA()==self.distanceC() and self.distanceS()==self.distanceB() and self.distanceD1()==self.distanceD2():
            return self.distanceA()*self.distanceB()
        else:
            return f"This is not a rectangular"


ball=True
while ball:
    x1 = float(input("Enter firs x: "))
    y1 = float(input("Enter firs y: "))
    x2 = float(input("Enter second x: "))
    y2 = float(input("Enter second y: "))
    x3 = float(input("Enter third x: "))
    y3 = float(input("Enter third y: "))
    x4 = float(input("Enter fourth x: "))
    y4 = float(input("Enter fourth y: "))
    obj=Rectangle(x1,y1,x2,y2,x3,y3,x4,y4)
    check_number =obj.area()
    class Check:
        def __init__(self,checks):
            self.checks=checks
        def check(self):
            try:
                chak=float(self.checks)
                return True
            except ValueError:
                return False
    boool=Check(check_number)

    if boool.check():
        print(check_number)
        ball=False
    else:
        print(check_number)