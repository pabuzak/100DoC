from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -100
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.up()
    new_turtle.goto(x=-460, y=y)
    all_turtles.append(new_turtle)

    y += 40

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()