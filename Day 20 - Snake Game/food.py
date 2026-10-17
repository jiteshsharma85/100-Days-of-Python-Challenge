from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(1.00, 1.00)
        self.refresh()

    # Moves the food to a new random position on the screen
    def refresh(self):
        x = randint(-280, 280)
        y = randint(-280, 275)
        self.goto(x, y)





