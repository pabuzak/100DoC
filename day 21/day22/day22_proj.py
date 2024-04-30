from turtle import Turtle, Screen

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

s.listen()








s.exitonclick()