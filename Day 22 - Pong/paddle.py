from turtle import Turtle, TNavigator

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.setx(x)
        self.sety(y)
        self.color("white")
        self.penup()
        self.shapesize(5, 1)

    # Moves the paddle up by 30 units
    def moving_up(self):
        current_y = self.ycor()
        self.sety(current_y + 30)

    # Moves the paddle down by 30 units
    def moving_down(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y -30)
