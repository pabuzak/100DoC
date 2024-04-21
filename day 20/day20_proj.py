from turtle import Screen, Turtle
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake")
s.tracer(0)

snakes = []
for i in range(3):
    new_turtle = Turtle()
    new_turtle.color("white")
    new_turtle.shape("square")
    new_turtle.up()
    new_turtle.goto(y=0, x=(i*-20))
    snakes.append(new_turtle)

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    
    for seg_num in range(len(snakes)-1, 0, -1):
        new_x = snakes[seg_num-1].xcor()
        new_y = snakes[seg_num-1].ycor()
        snakes[seg_num].goto(new_x, new_y)
    snakes[0].forward(20)


















s.exitonclick()


