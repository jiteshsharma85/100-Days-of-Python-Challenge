from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# --------------------------- PASSWORD GENERATOR --------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generator():

    password_list = []

    password_list += [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(symbols) for i in range(randint(2, 4))]
    password_list += [choice(numbers) for i in range(randint(2, 4))]

    shuffle(password_list)

    gen_pass = "".join(password_list)

    pass_entry.delete(0, "end")
    pass_entry.insert(0, gen_pass)
    pyperclip.copy(gen_pass)

# --------------------------- SAVE PASSWORD --------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"Website: {website} \nEmail: {email} \nPassword: {password} \n\nIs it Okay?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, "end")
            pass_entry.delete(0, "end")



# --------------------------- UI SETUP --------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=220, height=220)
img = PhotoImage(file="lock.png")

canvas.create_image(130, 110, image=img)
canvas.grid(row=1, column=2)


#label

website_text = Label(text="Website:")
website_text.grid(row=2, column=1)

email_text = Label(text="Email/Username:")
email_text.grid(row=3, column=1)

pass_text = Label(text="Password:")
pass_text.grid(row=4, column=1)


#entry

website_entry = Entry(width=40)
website_entry.grid(row=2, column=2, columnspan=3)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(0, "jitesh@email.com")

pass_entry = Entry(width=24)
pass_entry.grid(row=4, column=2)


#buttons

generate_button = Button(text="Generate Password", width=12, command=generator)
generate_button.grid(row=4, column=3)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=5, column=2, columnspan=2)



window.mainloop()
