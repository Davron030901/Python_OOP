from abc import ABC, abstractmethod

class Sanoq_Sistema(ABC):
    @abstractmethod
    def __init__(self,sistema):
        self.sistema =sistema
        self.son=[]
    @abstractmethod
    def sanoq(self):
        pass
class Ikkilik(Sanoq_Sistema):
    def __init__(self,sistema):
        super().__init__(sistema)
        self.sistema = sistema
        self.son = []
    def sanoq(self):
        if self.sistema>1:
            self.son.insert(0,self.sistema%2)
            self.sistema = self.sistema // 2
            return self.sanoq()
        else:
            self.son.insert(0, self.sistema)
            return self.son
class Tortlik(Sanoq_Sistema):
    def __init__(self,sistema):
        super().__init__(sistema)
        self.sistema = sistema
        self.son = []
    def sanoq(self):
        if self.sistema>3:
            self.son.insert(0,self.sistema%4)
            self.sistema=self.sistema//4
            return self.sanoq()
        else:
            self.son.insert(0, self.sistema)
            return self.son

class Sakkizlik(Sanoq_Sistema):
    def __init__(self,sistema):
        super().__init__(sistema)
        self.sistema = sistema
        self.son = []
    def sanoq(self):
        if self.sistema>7:
            self.son.insert(0,self.sistema%8)
            self.sistema=self.sistema//8
            return self.sanoq()
        else:
            self.son.insert(0, self.sistema)
            return self.son
class Onoltiilik(Sanoq_Sistema):
    def __init__(self,sistema):
        super().__init__(sistema)
        self.sistema = sistema
        self.onolti={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        self.son = []
    def sanoq(self):
        if self.sistema>15:
            self.son.insert(0, self.onolti[self.sistema %16])
            self.sistema=self.sistema//16
            return self.sanoq()
        else:
            self.son.insert(0, self.onolti[self.sistema %16])
            return self.son

number=int(input("Enter integer number: "))

print(f"Onlik: {number} -->Ikkilik: ",end="")
n2=Ikkilik(number)
for i in n2.sanoq():
    print(i,end="")
print(f"\nOnlik: {number} -->Tortlik: ",end="")
n4=Tortlik(number)
for i in n4.sanoq():
    print(i,end="")
print(f"\nOnlik: {number} -->Sakkizlik: ",end="")
n8=Sakkizlik(number)
for i in n8.sanoq():
    print(i,end="")
print(f"\nOnlik: {number} -->Onoltiilik: ",end="")
nu=Onoltiilik(number)
for i in nu.sanoq():
    print(i,end="")
