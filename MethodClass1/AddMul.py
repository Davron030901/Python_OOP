class Num:
    def __init__(self,n):
        self.n=n
        self.sum=0
        self.mulsum=1
        self.div=[]
    def lists(self):
        self.div.append(self.n)
        self.n = self.n - 1
        if self.n!=0:
            return self.lists()
        else:
            return self.div
class Add(Num):
    def add(self):
        self.sum=self.sum+ self.n
        self.n = self.n - 1
        if self.n != 0:
            return self.add()
        else:
            return self.sum
class Multiply(Num):
    def mul(self):
        self.mulsum*=self.n
        self.n = self.n - 1
        if self.n != 0:
            return self.mul()
        else:
            return self.mulsum

num=int(input("Enter number: "))
obj=Add(num)
obj1=Multiply(num)
for i in range(1,num+1):
    if i!=num:
        print(f"{i}",end="+")
    else:
        print(f"{i}",end="=")
print(obj.add())
for i in range(1,num+1):
    if i!=num:
        print(f"{i}",end="*")
    else:
        print(f"{i}",end="=")
print(obj1.mul())