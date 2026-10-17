
from turtle import Turtle, Screen
my_screen = Screen()
my_screen.listen()
jim = Turtle()


# Moves the turtle forward by 50 units
def forward():
    jim.forward(50)

# Moves the turtle backward by 50 units
def backward():
    jim.backward(50)

# Turns the turtle left by 20 degrees
def left_move():
    jim.left(20)

# Turns the turtle right by 20 degrees
def right_move():
    jim.right(20)

# Sends the turtle home and clears all drawings
def clear():
    jim.home()
    jim.clear()


my_screen.onkey(forward, "w")
my_screen.onkey(backward, "s")
my_screen.onkey(left_move, "a")
my_screen.onkey(right_move, "d")
my_screen.onkey(clear, "c")


my_screen.exitonclick()