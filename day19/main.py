from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=1000, height=800)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


tim.up()
tim.goto(x=-460, y=-100)


screen.exitonclick()