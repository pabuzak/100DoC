from turtle import Screen, Turtle

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake")

snakes = []
for i in range(3):
    new_turtle = Turtle()
    new_turtle.color("white")
    new_turtle.shape("square")
    new_turtle.goto(y=0, x=(i*-20))
    snakes.append(new_turtle)




















s.exitonclick()


