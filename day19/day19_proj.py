from turtle import Turtle, Screen

tim = Turtle()
s = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    angle = tim.heading()
    tim.setheading(angle + 5)


def clockwise():
    angle = tim.heading()
    tim.setheading(angle - 5)

def clear():
    tim.up()
    tim.home()
    tim.clear()
    tim.setheading(0)
    tim.down()
    

s.listen()
s.onkey(key="w", fun=move_forwards)
s.onkey(key="s", fun=move_backwards)
s.onkey(key="d", fun=counter_clockwise)
s.onkey(key="a", fun=clockwise)
s.onkey(key="c", fun=clear)
s.exitonclick()

