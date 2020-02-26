from itertools import cycle
import tkinter as tk


class App(tk.Tk):
    # TK window/label adjust to size of images
    def __init__(self, image_file, x, y, delay):

        tk.Tk.__init__(self)

        self.geometry("+{}+{}"format(x, y))
        self.delay = delay

        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_file)

        self.pictures_display = tk.Label(self)
        self.pictures_display.pack()

    def show_slides(self):
        # cycle through the images and display them

        img_object, img_name = next(self.pictures)
        self.pictures_display.config(image=img_object)

        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


# set milliseconds time between slides
delay = 3500
# get a series of gif images you have in the working folder
# or use full path, or set diretory to wher ther images are
image_file = [
    "1.gif",
    "2.gif",
    "3.gif",
    "4.gif",
    "5.gif",
    "6.gif",
    "7.gif"
]

x = 100
y = 50
app = App(image_file, x, y, delay)
app.show_slides()
app.run()
