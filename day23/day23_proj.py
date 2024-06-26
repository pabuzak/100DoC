### hard version
import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

# scoreboard
score = Scoreboard()

# cars list
cars = []

finish_count = 0
count = 6
game_is_on = True
while game_is_on:

    # detect if player has finished
    if player.finish():
        finish_count += 1
        # update move to increment by 10
        for car in cars:
            car.finish(finish_count)

        score.update_level()

    time.sleep(0.1)
    screen.update()

    # add cars every 6 iterations
    if count == 6:
        car = CarManager()
        cars.append(car)
        car.finish(finish_count)
        count = 0

    # move all cars
    for car in cars:
        car.move()

    # detect collisions
    for car in cars:
        if player.distance(x=car.positionx(), y=car.positiony()) < 20:
            game_is_on = False
            score.game_over()

            
    count += 1
        

screen.exitonclick()

