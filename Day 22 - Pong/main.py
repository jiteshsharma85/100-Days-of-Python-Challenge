from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Ping Pong Game")
screen.listen()
screen.tracer(0)

# right paddle (player 1) — arrow keys
right_paddle = Paddle(350, 0)
screen.onkey(right_paddle.moving_up, "Up")
screen.onkey(right_paddle.moving_down, "Down")

# left paddle (player 2) — WASD
left_paddle = Paddle(-350, 0)
screen.onkey(left_paddle.moving_up, "w")
screen.onkey(left_paddle.moving_down, "s")

#score
score = Score()

ball = Ball()



game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()

    if ball.xcor() > 380:
        ball.ball_reset()
        score.left_add()
    elif ball.xcor() < -380:
        ball.ball_reset()
        score.right_add()
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_touch()
    elif right_paddle.distance(ball) < 50 and ball.xcor() > 340:
        ball.x_touch()
        ball.speed_up()
    elif left_paddle.distance(ball) < 50 and ball.xcor() < -340:
        ball.x_touch()
        ball.speed_up()

    ball.move()

screen.exitonclick()