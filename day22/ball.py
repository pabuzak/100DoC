from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=1)
        self.setposition(x=0, y=0)

    def move(self):
        y = self.ycor() + 5
        x = self.xcor() + 7
        return self.setposition(x=x, y=y)


