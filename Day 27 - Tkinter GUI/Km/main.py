from tkinter import *


windows = Tk()
windows.minsize(width=200, height=100)
windows.config(padx=20, pady=20)
windows.title("Mile to Km Converter")

#entery

input = Entry(width=10)
input.grid(column=2, row=1)

#label

mile_unit = Label(text="miles")
mile_unit.grid(column=3, row=1)

# Reads the miles input, converts to km, and updates the answer label
def convert():
    km = 1.60934 * float(input.get())

    answer.config(text=km)


#label

equal_label = Label(text="is equal to")
equal_label.grid(column=1, row=2)

#answer_label

answer  = Label(text="0")
answer.grid(column=2, row=2)

# KM label

KM_label = Label(text="Km")
KM_label.grid(column=3, row=2)


my_button = Button(text="Calculate", command=convert)
my_button.grid(column=2, row=3)






windows.mainloop()
