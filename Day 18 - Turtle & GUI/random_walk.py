from turtle import Turtle, Screen, colormode
from random import randint, choice

jim = Turtle()
jim.shapesize(5,3,2)
jim.pensize(20)
jim.speed(20)
colormode(255)


# Returns a random RGB colour tuple
def color():
    x = randint(0,255)
    y = randint(0,255)
    z = randint(0,255)
    return x, y, z

step = randint(15, 115)
angle = [0, 45, 90, 180, 225, 270]


for i in range(500):
    jim.forward(step)
    jim.setheading(choice(angle))
    jim.color(color())

my_screen = Screen()
my_screen.exitonclick()


