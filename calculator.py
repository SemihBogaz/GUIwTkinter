from tkinter import *

root = Tk()
root.title("Simple Calculator")
first_num = ""
operation = ""
field = Entry(root, width=40, borderwidth=5)
field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    # field.delete(0,END)
    field.insert(END, number)


def add_button():
    f_num = field.get()
    global first_num
    global operation
    operation = "add"
    first_num = int(f_num)
    field.delete(0, END)


def subs_button():
    f_num = field.get()
    global first_num
    global operation
    operation = "sub"
    first_num = int(f_num)
    field.delete(0, END)


def mult_button():
    f_num = field.get()
    global first_num
    global operation
    operation = "mul"
    first_num = int(f_num)
    field.delete(0, END)


def div_button():
    f_num = field.get()
    global first_num
    global operation
    operation = "div"
    first_num = int(f_num)
    field.delete(0, END)


def equals_button():
    # there is no switch case in python so we can use funcs, if or dict0
    second_num = field.get()
    field.delete(0, END)

    if operation == "add":
        field.insert(0, first_num + int(second_num))

    if operation == "subs":
        field.insert(0, first_num - int(second_num))

    if operation == "mul":
        field.insert(0, first_num * int(second_num))

    if operation == "div":
        try:
            res = first_num / int(second_num)
        except ZeroDivisionError as e:
            field.insert(0, e)
        else:
            field.insert(0, res)


# definitions of the buttons
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

# special buttons
button_add = Button(root, text="+", padx=39, pady=20, command=add_button)
button_subs = Button(root, text="-", padx=41, pady=20, command=subs_button)
button_div = Button(root, text="/", padx=40, pady=20, command=div_button)
button_mult = Button(root, text="*", padx=41, pady=20, command=mult_button)
button_equal = Button(root, text="=", padx=88, pady=20, command=equals_button)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: field.delete(0, END))

# putting them into the layout
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subs.grid(row=6, column=0)
button_div.grid(row=6, column=2)
button_mult.grid(row=6, column=1)
root.mainloop()
