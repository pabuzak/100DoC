import turtle as t
from turtle import Turtle, Screen, Shape
import random

timmy = Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.color("red")

# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pd()

# color = ["deep pink", "midnight blue", "dark red"]
# degree = 360
# for i in range(3,10):
#     sides = i
#     angle = degree / sides

#     for _ in range(i):
#         timmy.color(random.choice(color))
#         timmy.right(angle)
#         timmy.forward(100)

timmy.speed(0)
timmy.pensize(1)

def pick_direction():
    direction = [0, 90, 180, 270]
    return direction[random.randint(0, 3)]

def pick_color():
    color_tuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return timmy.pencolor(color_tuple)

# for _ in range(50):
#     direction = pick_direction()
#     pick_color()
#     timmy.seth(direction)
#     timmy.forward(25)



### my take on Challenge 5
# angle = 0
# for _ in range(75):
#     if angle == 360:
#         break   
#     pick_color()
#     timmy.circle(100)
#     timmy.seth(angle)
#     angle += 5


### answer:
def draw(gap):
    for _ in range (int(360/gap)):
        pick_color()
        timmy.circle(100)
        timmy.seth(timmy.heading() + gap)




    

screen = Screen()
screen.exitonclick()



