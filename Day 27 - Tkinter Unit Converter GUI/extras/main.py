
from tkinter import *


# Updates the label with whatever is currently typed in the input field
def button_clicked():
    my_label.config(text = input.get())


windows = Tk()
windows.title("My first GUI")
windows.minsize(height=500, width=500)


#label
my_label = Label(text="this is the first label")
#my_label.pack()
my_label.grid(column=1, row=1)



#button
my_button = Button(text="Press me to START", command=button_clicked)
#my_button.pack()
my_button.grid(column=2, row=2)


button_2 = Button(text="New Button")
button_2.grid(column=3, row=1)


#input field

input = Entry(width=15)
input.grid(column=4, row=4)

windows.mainloop()