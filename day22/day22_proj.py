from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


s = Screen()
s.setup(width=800, height=600)
s.bgcolor("Black")
s.title("Pong")
s.tracer(0)

r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))

s.listen()
s.onkey(key="Up", fun=r_pad.up)
s.onkey(key="Down", fun=r_pad.down)
s.onkey(key="w", fun=l_pad.up)
s.onkey(key="s", fun=l_pad.down)

ball = Ball()
scoreboard = ScoreBoard()


game_on = True
while game_on:
    s.update()
    time.sleep(ball.time)
    ball.move()

    #detect collision with ceiling and bounce
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()



    #detect collision with paddles
    if ball.distance(x=r_pad.pos[0], y=r_pad.pos[1]) < 50 and ball.xcor() > 330 or ball.distance(x=l_pad.pos[0], y=l_pad.pos[1]) < 30 and ball.xcor() > -400:
        ball.bounce_x()
        

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


s.exitonclick()