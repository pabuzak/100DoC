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

cars = []

count = 6
game_is_on = True
while game_is_on:
    if count == 6:
        car = CarManager()
        cars.append(car)
        count = 0


    for car in cars:
        car.move()

    time.sleep(0.1)
    screen.update()

    
    
    if player.finish():
        pass

    count += 1
        
        

    

