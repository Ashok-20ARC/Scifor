class Parent:
    def parent(self):
        print("This is a parent class")


class Child(Parent):
    def child(self):
        print("This is a child class")

obj=Child()
obj.parent()
obj.child()
