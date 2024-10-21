from abc import ABC, abstractmethod

class Form(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Triangle(Form):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def perimeter(self):
        return self.x+self.y+self.z
    def area(self):
        return (self.perimeter()/2*(self.perimeter()/2-self.x)*(self.perimeter()/2-self.y)*(self.perimeter()/2-self.z))**0.5
obj=Triangle(2,2,3)
print(obj.area())


