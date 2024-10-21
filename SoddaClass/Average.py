class Average(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def arithmetic(self):
        return (self.x+self.y)/2
    def geometric(self):
        return (self.x*self.y)**0.5

ball=True
while ball:
    a=float(input("Enter firs number: "))
    b=float(input("Enter second leg: "))
    if a>=0 and b>=0:
        obj=Average(a,b)
        print(f"Average arithmetic:{obj.arithmetic()} , Average geometic:{obj.geometric()}")
        ball=False
    else:
        print(f"Average arithmetic:{obj.arithmetic()}Let number be greater than zero,because average geometric error! Enter again. ")