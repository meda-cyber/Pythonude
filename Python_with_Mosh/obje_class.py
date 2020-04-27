class Animal(object):
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: parent , Base
# Mammal: Child, Sub


class Mammal(Animal):

    def walk(self):
        Print("walk")


class Fish(Animal):
    def swimm(self):
        print("swimm")


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
