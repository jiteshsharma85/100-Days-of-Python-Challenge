from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE


    # Randomly spawns a new car on the right side of the screen
    def create_car(self):
        random_chance  = randint(1, 6)
        if random_chance == 1:
            self.new_car = Turtle()
            self.new_car.shape("square")
            self.new_car.shapesize(1, 2)
            self.new_car.penup()
            self.new_car.color(choice(COLORS))
            self.new_car.goto(320, randint(-250, 250))
            self.car_list.append(self.new_car)


    # Moves all cars to the left by the current speed
    def car_move(self):

        for car in self.car_list:
            car.backward(self.car_speed)


    # Removes cars that have gone off the left edge of the screen
    def car_reset(self):
        self.car_list = [car for car in self.car_list if car.xcor() >= -320]


    # Increases car speed when the player reaches the next level
    def level_up(self):
        self.car_speed += MOVE_INCREMENT