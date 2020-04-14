# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))
# print(isinstance(point, Point))


# creating new constructure

class Point:
    # class level attribute are accessinle all level of the class.
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
# print(point.x)
point.draw()
print(point.default_color)
print(Point.default_color)


# class and attribute refrence
another = Point(3, 4)
another.draw()
