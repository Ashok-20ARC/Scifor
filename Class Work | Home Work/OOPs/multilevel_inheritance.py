class Grand_Father:
    def house(self):
        print("Had 2bhk house")

class Father(Grand_Father):
    def car(self):
        print("Had BMW car")

class Son(Father):
    def bike(self):
        print("Had Apache RTR bike")


obj=Son()
obj.bike()
obj.car()
obj.house()
