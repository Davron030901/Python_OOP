class Calc:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

class Calculator(Calc):
    def max(self):
        if self.x>self.y:
            if self.x>self.z:
                return self.x
            else:
                return self.z
        else:
            if self.y>self.z:
                return self.y
            else:
                return self.z

    def min(self):
        if self.x<self.y:
            return self.x
        else:
            return self.y



num1=float(input("Enter firs number: "))
num2=float(input("Enter second number : "))
num3=float(input("Enter third number"))
first=Calculator(num1,num2,num3)
second=Calculator(num1,num2,num3)
third=Calculator(num1,num2,num3)
fourth=Calculator(num1,num2,num3)
print(f"1-number:{first.x},2-number:{second.y} 3- number:{third.z}The maximum is: {fourth.max()}")
