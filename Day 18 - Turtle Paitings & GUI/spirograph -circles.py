from turtle import Turtle, Screen, colormode
from random import randint

jim = Turtle()
jim.speed("fastest")
colormode(255)


# Returns a random RGB colour tuple
def color():
    x = randint(0,255)
    y = randint(0,255)
    z = randint(0,255)
    return x, y, z

step = randint(15, 115)
angle = [0, 45, 90, 180, 225, 270]

# Draws a full spirograph by rotating a circle by the given gap angle each step
def spirograph(gap):
    for i in range(int(360/gap)):
        jim.color(color())
        jim.circle(100)
        jim.setheading(jim.heading() + gap)

spirograph(1)

my_screen = Screen()
my_screen.exitonclick()


