from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # Magic method
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(id(p1))
print(id(p2))

# Better way of coding
Point = namedtuple("Point", ["x", "y"])
m1 = Point(x=1, y=2)
m2 = Point(x=1, y=2)
# m1.x = 10  # we cant set attribute coz it is tuple instea
m1 = Point(x=10, y=6)

print(m1 == m2)
