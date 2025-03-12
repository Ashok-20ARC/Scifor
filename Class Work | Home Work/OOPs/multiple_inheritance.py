class Father:
    def land(self):
        print("Had a land")

class Mother:
    def cook(self):
        print("Had cooking skill")

class Son(Father,Mother):
    def coding(self):
        print("Had a coding skill")

obj=Son()

obj.land()
obj.cook()
obj.coding()
