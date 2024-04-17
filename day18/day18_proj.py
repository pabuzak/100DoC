from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pd()


screen = Screen()
screen.exitonclick()

