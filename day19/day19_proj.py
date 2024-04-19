from turtle import Turtle, Screen

tim = Turtle()
s = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    angle -= 1
    tim.seth(angle)

s.listen()
s.onkey(key="w", fun=move_forwards)
s.onkey(key="s", fun=move_backwards)
s.onkey(key="d", fun=counter_clockwise)
s.exitonclick()