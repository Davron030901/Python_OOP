class List:
    def __init__(self,massive):
        self.massive =massive
        self.cont_p=0
        self.cont_m=0


class Massive(List):
    def ordenal_count(self):
        for i in self.massive:
            if i<0:
                self.cont_m+=1
            else:
                self.cont_p+=1
        return f"Count minus: {self.cont_m},Count plus: {self.cont_p}"

count=int(input("Enter the list of count: "))
A=[]
for j in range(count):
    A.append(int(input(f"Enter the {j+1}-lift of value: ")))
obj=Massive(A)
print(f"List ordinal {obj.ordenal_count()}")
