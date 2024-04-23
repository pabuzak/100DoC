from turtle import Turtle

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.up()
            new_snake.goto(y=0, x=(i*-20))
            self.snakes.append(new_snake)

    def move(self):
        for seg_num in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[seg_num-1].xcor()
            new_y = self.snakes[seg_num-1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.snakes[0].forward(20)


