import time
from snake import Snake
from turtle import Screen
from food import Food
from Scoreboard import Score

game_is_on = True


screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Score()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



    # snake collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.adding_score()
        snake.adding_snake_block()


    # collision with wall
    if snake.head.xcor() > 585 or snake.head.xcor() < -585 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.update_high_score()
        snake.snake_reset()


    # collision with self
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            score.update_high_score()
            snake.snake_reset()













screen.exitonclick()