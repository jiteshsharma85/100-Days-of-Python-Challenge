from turtle import Turtle, Screen, colormode
from random import randint

jimmy = Turtle()

jimmy.shape("turtle")
colormode(255)

side = 3




# Returns a random RGB colour tuple
def color():
    x = randint(0,255)
    y = randint(0,255)
    z = randint(0,255)
    return x, y, z



# Calculates the exterior angle for a regular polygon with the given number of sides
def angle_of_shape(side):
    return 360/side


for i in range(50):
    side += i
    for i in range(side):
        jimmy.forward(100)
        jimmy.left(angle_of_shape(side))
    jimmy.color(color())











mano_screen = Screen()
mano_screen.exitonclick()