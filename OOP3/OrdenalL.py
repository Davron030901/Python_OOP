class List:
    def __init__(self,massive):
        self.massive =massive
        self.max=[]


class Massive(List):
    def ordenal(self):
        for i in self.massive:
            if i<0:
                self.max.insert(0,i)
            else:
                self.max.append(i)
        return self.max

count=int(input("Enter the list of count: "))
A=[]
for j in range(count):
    A.append(int(input(f"Enter the {j+1}-lift of value: ")))
obj=Massive(A)
print(f"List ordinal: {obj.ordenal()}")
