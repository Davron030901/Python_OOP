class List:
    def __init__(self,massive):
        self.massive =massive
        self.sum=0
        self.multiply=1
        self.max=massive[0]
        self.min=massive[0]
class Massive(List):

    def add(self):
        for i in self.massive:
            self.sum+=i
        return self.sum
    def mult(self):
        for i in self.massive:
            self.multiply*=i
        return self.multiply
    def maximum(self):
        for i in self.massive:
            if i>self.max:
                self.max=i
        return self.max
    def minimum(self):
        for i in self.massive:
            if i<self.min:
                self.min=i
        return self.min
count=int(input("Enter the list of count: "))
A=[]
for j in range(count):
    A.append(int(input(f"Enter the {j+1}-lift of value: ")))
obj=Massive(A)
print(f"List multiply: {obj.mult()},List add: {obj.add()},List max: {obj.maximum()},List min: {obj.minimum()}")
