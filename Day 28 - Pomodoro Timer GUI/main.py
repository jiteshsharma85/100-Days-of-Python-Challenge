from pickle import GLOBAL
from tkinter import *
import math

# ------------------------------------ CONSTANTS ------------------------------------ #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
mark = ""
# ------------------------------------ TIMER RESET ------------------------------------ #

def press_reset():

    window.after_cancel(timer)
    global rep, mark
    rep = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    mark = ""
    check_mark.config(text=mark)


# ------------------------------------ TIMER MECHANISM ------------------------------------ #
def press_start():

        global rep
        rep += 1
        if rep % 8 == 0:
            count_down(LONG_BREAK_MIN*60)
            title_label.config(text="Long Break", fg=RED)
        elif rep % 2 != 0:
            count_down(WORK_MIN*60)
            title_label.config(text="Focus Time", fg=GREEN)

        else:
            count_down(SHORT_BREAK_MIN*60)
            title_label.config(text="Short Break", fg=PINK)


# ------------------------------------ COUNTDOWN MECHANISM ------------------------------------ #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60



    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        press_start()

        if rep % 2 == 0:
            global mark
            mark += "⍻"
            check_mark.config(text = mark)


# ------------------------------------ UI SETUP ------------------------------------ #
window = Tk()
window.title("My Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)




#buttons

button_start = Button(text="Start", font=(FONT_NAME, 15), highlightbackground=YELLOW, bg=YELLOW, command=press_start)
button_start.grid(row=3, column=1)

button_reset = Button(text="Reset", font=(FONT_NAME, 15), bg=YELLOW, highlightbackground=YELLOW, command=press_reset)
button_reset.grid(row=3, column=3)

# label

title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(row=1, column=2)

check_mark = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(row=4, column=2)

# canvas


canvas = Canvas(width=250, height=224, bg=YELLOW, highlightthickness=0)
tomo_img = PhotoImage(file="tomato.png")
canvas.create_image(120, 112, image=tomo_img)
timer_text = canvas.create_text(120, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


window.mainloop()