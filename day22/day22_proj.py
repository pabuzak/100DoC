from turtle import Turtle, Screen
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("Black")
s.title("Pong")

rpaddle = Turtle()
rpaddle.speed("fastest")
rpaddle.color("White")
rpaddle.shape("square")
rpaddle.up()
rpaddle.goto(x=350, y=0)
rpaddle.shapesize(stretch_len=1, stretch_wid=5)

def up():
    x, y = rpaddle.pos()
    rpaddle.goto(y=y-20, x=x)

def down():
    x, y = rpaddle.pos()
    rpaddle.goto(y=y+20, x=x)

s.listen()
s.onkey(key="Up", fun=down)
s.onkey(key="Down", fun=up)








s.exitonclick()