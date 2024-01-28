COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        for i in range(1,3):
            chance = random.randint(i,6)
            if chance == 6:
                car = Turtle("square")
                car.shapesize(1, 2)
                car.color(random.choice(COLORS))
                car.penup()
                car.goto(300, random.randint(-250, 250))
                self.cars.append(car)

    def move_car(self):
        for i in self.cars:
            i.backward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT

