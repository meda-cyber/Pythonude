from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):  # This is type of polymorphism
    for control in controls:
        control.draw()


ddl = DropDownList()
# draw(ddl)
texbox = TextBox()
# draw(texbox)
draw([ddl, texbox])
