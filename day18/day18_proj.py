from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

for _ in range(4):
    timmy.right(90)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()