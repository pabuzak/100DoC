from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
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


game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    ball.move()

    #detect collision with ceiling and bounce
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()



    #detect collision with r_paddle
    if ball.distance(x=r_pad.pos[0], y=r_pad.pos[1]) < 50 and ball.xcor() > 330 or ball.distance(x=l_pad.pos[0], y=l_pad.pos[1]) < 50 and ball.xcor() > -600:
        ball.bounce_x()

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.setpos(0,0)

s.exitonclick()