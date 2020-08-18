from tkinter import *

root = Tk()

field = Entry(root, width=50, borderwidth=5)
field.pack()
field.insert(0, "Enter name")


def Clicker():
    hello ="Hello "+field.get()
    action = Label(root, text=hello)
    action.pack()


button = Button(root, text="Enter your name", command=Clicker).pack()


root.mainloop()
