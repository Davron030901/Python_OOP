import math


class Digit():
    def __init__(self,x):
        self.x=x
        self.sum=0
        self.multiplication=1
    def add(self):
        for i in self.x:
            self.sum=self.sum+int(i)
        return self.sum

    def multiply(self):
        for j in self.x:
            self.multiplication=self.multiplication*int(j)
        return self.multiplication
def check(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

boool=True
while boool:



    number = input("Enter a three-digit number: ")
    three_digit = Digit(number)
    if check(number):
        print(f"ADD number:{three_digit.add()}, MULTIPLICATION number:{three_digit.multiply()}")
        boool=False
    else:
        print("Number is not a three-digit number")