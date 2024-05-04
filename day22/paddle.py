from turtle import Turtle

class Paddle:
    def __init__(self, pos):
        self.pos = pos
        self.paddle = []
        self.create_paddle()

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.up()
        paddle.goto(self.pos)
        paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.append(paddle)

    def up(self):
        p = self.paddle[0]
        y = p.ycor() + 20
        p.goto(y=y, x=p.xcor())

    def down(self):
        p = self.paddle[0]
        y = p.ycor() - 20
        p.goto(y=y, x=p.xcor())
