
import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.setup(730, 500)
screen.title("USA States name game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:

    answer = screen.textinput(f"{len(guessed_states)}/50 -Enter your Guess", prompt="What would be the next State?").title()

    file = pandas.read_csv("50_states.csv")
    all_state = file["state"].tolist()

    if answer == "Exit":
        missed_states = [state for state in all_state if state not in guessed_states]
        kobo = pandas.DataFrame(missed_states)
        kobo.to_csv("remaining.csv")
        break

    if answer in all_state:
        match = file[file.state == answer]

        state_name = match.state.item()
        x = int(match.x.item())
        y = int(match.y.item())


        tim = Turtle()

        tim.hideturtle()
        tim.penup()
        tim.goto(x, y)
        tim.write(state_name)
        guessed_states.append(state_name)





#print(match)




screen.exitonclick()