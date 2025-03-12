class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Lion(Animal):
    def sound(self):
        return "Roar"

d=Dog()
print(d.sound())

c=Cat()
print(c.sound())

l=Lion()
print(l.sound())
