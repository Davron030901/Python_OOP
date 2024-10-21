class List:
    def __init__(self,massive):
        self.massive =massive


class Massive(List):
    def ordenal_count(self):
        return self.massive[::-1]
count=int(input("Enter the list of count: "))
A=[]
for j in range(count):
    A.append(int(input(f"Enter the {j+1}-lift of value: ")))
obj=Massive(A)
print(A)
print(f"List ordinal {obj.ordenal_count()}")
