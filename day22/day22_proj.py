from turtle import Turtle, Screen
from paddle import Paddle
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

game_on = True
while game_on:
    s.update()






s.exitonclick()