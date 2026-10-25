
from turtle import Turtle, Screen
from random import choice, randint

my_screen = Screen()
my_screen.setup(width=500, height=400)
my_screen.listen()

is_on = False
colors = ["red", "blue", "green", "yellow", "orange", "purple", "indigo"]
y = [ 100, 60, 20, -20, -60, -100]
all_turtles =[]

# Creates a turtle at a fixed y-position with the colour at index x
def turtle_body(x):
    jim = Turtle(shape="turtle")
    jim.penup()
    jim.goto(-230, y[x])
    jim.color(colors[x])
    all_turtles.append(jim)

for i in range(0, 6):
    turtle_body(i)





user_input = my_screen.textinput("What is your bet?", "Enter the color of winning turtle?")


if user_input:
    is_on = True

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winner = turtle.pencolor()
            is_on = False
            if winner == user_input:
                print(f"you guessed it right! The winner is {winner}")
            else:
                print(f"you guessed it wrong! The winner is {winner}")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)











my_screen.exitonclick()