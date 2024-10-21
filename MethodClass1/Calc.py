class Calc:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def dev(self):
        return self.x/self.y
class Calculator(Calc):
    def max(self):
        if self.x>self.y:
            return self.x
        else:
            return self.y
    def min(self):
        if self.x<self.y:
            return self.x
        else:
            return self.y
    def arith(self):
        return self.add()/2
    def geom(self):
        return self.mul()**0.5
    def pow(self):
        return self.x**self.y


ball=True
while ball:
    num1=float(input("Enter firs number: "))
    num2=float(input("Enter second number not zero: "))
    if num2 != 0:
        ob1=Calculator(num1,num2)
        ob2=Calculator(num2,num1)
        obj=Calculator(num1,num2)
        calc={"+":obj.add(),"-":obj.sub(),"*":obj.mul(),":":obj.dev(),"max":obj.max(),"min":obj.min(),"pow":obj.pow(),"arithmetic":obj.arith(),"geometric":obj.geom(),}
        for key in calc.keys():
            print(f"'{key}',",end="")

        action=input("Enter action: ").lower()
        if action in calc.keys():
            print(ob1.x,f"{action}",end="")
            print(ob2.x,"=",end="")
            print(calc[action])
            ball=False
        else:
            ball=True
    else:
        print("Not zero enter other second number")
        ball=True