import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
from turtle import Turtle
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# setting up the object
turtle = Player()
screen.listen()
screen.onkeypress(turtle.go_up,"Up")
# setting up car object
car = CarManager()
#score
score = Scoreboard()
# car speed generation
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for i in car.cars:
        if i.distance(turtle) < 20:
            game_is_on = False
            score.game_over()

    if turtle.did_player_win():
        turtle.restart()
        car.next_level()
        score.increase_score()
        score.clear()
        score.updatescore()

screen.exitonclick()