from tkinter import *


class CurrencyConverter:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")  # Add title to application window
        # Add background color to application window
        window.configure(bg="yellow")

        # Adding Label widgets to application window
        Label(window, font="Helvetica 12 bold", bg="yellow",
              text="Amount to convert").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="yellow",
              text="Conversion Rate").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="yellow",
              text="Converted Amount").grid(row=3, column=1, sticky=W)

       #  Create objects and add entry function
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable=self.amounttoConvertVar,
              justify=RIGHT).grid(row=1, column=2)
        self.conversionRatVar = StringVar()
        Entry(window, textvariable=self.amounttoConvertVar,
              justify=RIGHT).grid(row=2, column=2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window, font="Helvetica 12 bold", bg="yellow",
                                   textvariable=self.convertedAmountVar).grid(row=3, column=1, sticky=E)

        # Create convert and clear buttons. when clicked they will call their respective functions.
        btConvertedAmount = Button(window, text="Convert", font="Helvetica 12 bold", bg="blue",
                                   fg="white", command=self.convertedAmount).grid(row=4, column=2, sticky=E)
        btdelete_all = Button(window, text="clear", font="Helvetica 12 bold", bg="blue",
                              fg="white", command=self.delete_all).grid(row=4, column=6, padx=25, pady=25, sticky=E)
