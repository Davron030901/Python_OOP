class List:
    def __init__(self,massive):
        self.massive =massive
        self.max=massive[0]
        self.min=1
        self.count=0

class Massive(List):
    def maximum(self):
        for i in self.massive:
            self.count+=1
            if i>self.max:
                self.max=i
                self.min=self.count
        return self.min

count=int(input("Enter the list of count: "))
A=[]
for j in range(count):
    A.append(int(input(f"Enter the {j+1}-lift of value: ")))
obj=Massive(A)
print(f"List max index: {obj.maximum()}")
