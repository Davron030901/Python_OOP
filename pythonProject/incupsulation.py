class Car:
    model='Malibu'
    __price=25000
    color='black'
    def getter(self):
        return self.__price
    def setter(self,new_price):
        self.__price=new_price
        return self.__price
    def __hello(self):
        return 'Hello World'
    def getterH(self):
        return self.__hello()
    def setterH(self,new_hello):
        self.__hello()==new_hello
        return self.__hello()

car1=Car()
print(car1.getter())
print(car1.setter(26000))
print(car1.getterH())
print(car1.setterH("25000"))