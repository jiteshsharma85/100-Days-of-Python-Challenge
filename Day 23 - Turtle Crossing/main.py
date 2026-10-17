import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Turtle crossing game")


player = Player()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, key="Left")
screen.onkey(player.move_right, "Right")

car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()


    for car in car_manager.car_list:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()



    if player.ycor() > 260:
        player.rest_player()
        car_manager.level_up()
        scoreboard.next_level()

    car_manager.car_move()

screen.exitonclick()