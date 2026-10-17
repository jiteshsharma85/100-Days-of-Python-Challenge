
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    # Creates the initial 3-segment snake
    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.penup()
            tim.color("white")
            tim.setx(-20 * i)
            self.segment.append(tim)


    # Moves each segment to the position of the one in front, then advances the head
    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Turns the snake up (ignores if already going down)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Turns the snake down (ignores if already going up)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Turns the snake left (ignores if already going right)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Turns the snake right (ignores if already going left)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Hides all segments off-screen and rebuilds the snake from scratch
    def snake_reset(self):
        for seg in self.segment:
            seg.goto(350, 350)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]


    # Adds a new segment to the end of the snake
    def adding_snake_block(self):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        last_segment = self.segment[-1]
        tim.goto(last_segment.xcor(), last_segment.ycor())
        self.segment.append(tim)
