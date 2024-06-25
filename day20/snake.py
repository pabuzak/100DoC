from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, positions):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.up()
        new_snake.goto(positions)
        self.snakes.append(new_snake)

    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for seg_num in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[seg_num-1].xcor()
            new_y = self.snakes[seg_num-1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

