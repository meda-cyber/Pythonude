class Cars:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


ford = Cars(250, "green")
nissan = Cars(300, "red")
toyta = Cars(350, "blue")


ford.set_speed(450)
print(ford.set_speed)


# ford.speed = 500
# print(ford.speed)
# print(ford.color)
print(ford.get_speed())
