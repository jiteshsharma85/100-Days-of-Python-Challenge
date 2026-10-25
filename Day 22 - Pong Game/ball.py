from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(45)
        self.ball_speed = 0.1

    # Moves the ball forward by 1 step in the current direction
    def move(self):
        self.forward(1)

    # Bounces the ball off the top or bottom wall
    def y_touch(self):
        new_angle = self.heading()
        self.setheading(-new_angle)


    # Bounces the ball off a paddle (reverses horizontal direction)
    def x_touch(self):
        new_angle = self.heading()
        self.setheading(180-new_angle)

    # Resets the ball to the centre and flips direction
    def ball_reset(self):
        self.goto(0,0)
        self.x_touch()

    # Increases ball speed after each paddle hit
    def speed_up(self):
        self.ball_speed *= 0.9
