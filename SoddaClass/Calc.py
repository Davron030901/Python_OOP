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

ball=True
while ball:
    num1=float(input("Enter firs number: "))
    num2=float(input("Enter second number not zero: "))
    if num2 != 0:
        obj=Calc(num1,num2)
        calc={"+":obj.add(),"-":obj.sub(),"*":obj.mul(),":":obj.dev()}
        for key in calc.keys():
            print(f"'{key}',",end="")

        action=input("Enter action: ")
        if action in calc.keys():
            print(calc[action])
            ball=False
        else:
            ball=True
    else:
        print("Not zero enter other second number")
        ball=True
