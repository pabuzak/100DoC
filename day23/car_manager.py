from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.shape('square')
        self.turtle.color(random.choices(COLORS))
        self.turtle.setheading(180)
        self.turtle.speed(1)
        self.turtle.goto(x=310, y=random.randrange(-250, 250))
        self.turtle.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        xcor = self.turtle.xcor() - 10
        ycor = self.turtle.ycor()
        self.turtle.goto(x=xcor, y=ycor)

    def start(self):
        xcor = self.turtle.xcor() - STARTING_MOVE_DISTANCE
        ycor = self.turtle.ycor()
        self.turtle.goto(x=xcor, y = ycor)

    def positionx(self):
        return self.turtle.xcor()
    
    def positiony(self):
        return self.turtle.ycor()