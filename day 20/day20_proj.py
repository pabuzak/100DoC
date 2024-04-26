from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

s.listen()
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Down", fun=snake.down)
s.onkey(key="Left", fun=snake.left)
s.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()


s.exitonclick()


