from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        turtle = Turtle()
        turtle.penup()
        turtle.shape('square')
        turtle.color("black")
        turtle.setheading(180)
        turtle.speed(1)
        turtle.goto(x=310, y=0)
        
        while turtle.xcor() > -300:
            turtle.forward(MOVE_INCREMENT)