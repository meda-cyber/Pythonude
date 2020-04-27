class Animal(object):
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: parent , Base
# Mammal: Child, Sub


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        Print("walk")


class Fish(Animal):
    def swimm(self):
        print("swimm")


m = Mammal()
print(m.age)
print(m.weight)
