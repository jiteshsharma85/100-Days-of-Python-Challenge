from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)
# color = colorgram.extract("hirst.jpg", 20)
#
# rgb_final = []
#
# for i in color:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     tuple = (r, g, b)
#     rgb_final.append(tuple)
#
# print(type(rgb_final))
# print(r)
#
# print(rgb_final)



extracted_colors = [(219, 148, 91), (55, 104, 134), (145, 85, 60), (122, 162, 186), (216, 85, 62), (145, 67, 92), (205, 128, 153), (53, 123, 88), (151, 147, 63), (197, 86, 115), (78, 159, 121), (116, 180, 152), (29, 52, 74), (230, 199, 118), (42, 57, 105), (50, 43, 32)]


paint = Turtle()
paint.width(1)
paint.setx(-100)
paint.sety(-100)

# Moves to the start of the next row and draws another round of dots
def ps():
    k = 0
    for i in range(5):
        paint.penup()
        paint.setx(-100)
        k += 50
        paint.sety(k)
        repitition_one_round()

# Draws 10 dots in a horizontal row using random colours from the extracted palette
def repitition_one_round():
    for i in range(10):
        #paint.color(choice(extracted_colors))
        paint.dot(20, choice(extracted_colors))
        paint.penup()
        paint.forward(50)


for i in range(4):
    repitition_one_round()

    ps()


my_screen = Screen()
my_screen.exitonclick()