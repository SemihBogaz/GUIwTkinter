from tkinter import *


root = Tk()


def Clicker():
    action  = Label(root, text  = "Oops i clicked a button!").pack()


button = Button(root,text = "Click me!",padx = 30,command = Clicker, fg= "white" ,bg = "red").pack()
button2 = Button(root,text = "Don't click me!", state = DISABLED,padx = 15).pack()

root.mainloop()