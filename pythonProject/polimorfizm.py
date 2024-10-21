from math import pi

class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,length):
        super().__init__("Circle")
        self.length = length
    def area(self):
        return self.length**2*pi
    def __str__(self):
        return f"Circle area : {self.area()}"
obj = Circle(4)
print(obj)