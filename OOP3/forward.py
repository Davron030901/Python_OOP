class List:
    def __init__(self,massive,count):
        self.massive =massive
        self.count=count
        self.num=None


class Massive(List):
    def ordenal_count(self):
        self.massive.insert(0,self.massive[self.count-1])
        del self.massive[self.count]


        return self.massive
val=True
while val:
    count=int(input("Enter the list of count: "))
    A=[]
    for j in range(count):
        A.append(int(input(f"Enter the {j+1}-lift of value: ")))
    numer=int(input("How many items you want to push forward: "))
    if count>=numer:
        obj=Massive(A,numer)
        print(A)
        print(f"List ordinal {obj.ordenal_count()}")
        val=False
    else:
        print("Sorry error,repait!count >= forward.")
