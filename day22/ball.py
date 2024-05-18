from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=1)
        self.setposition(x=0, y=0)
        self.ymovement = 10
        self.xmovement = 10
        self.time = 0.1

    def move(self):
        y = self.ycor() + self.ymovement
        x = self.xcor() + self.xmovement
        return self.setposition(x=x, y=y)


    def bounce_y(self):
        self.ymovement  *= -1
    
    def bounce_x(self):
        self.xmovement  *= -1
        self.time *= 0.9
    
    def reset_position(self):
        self.goto(0, 0)
        self.time = 0.1
        self.bounce_x()
