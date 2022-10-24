from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turns off the animation. Here refers to the padding going to right side

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:  # This while loop is simply to display what screen.tracer(0) has turned off
    time.sleep(0.1)  # to make the ball move slower
    screen.update()
    ball.move()

    # Detect collision with the upper wall or lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with right & left paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()
