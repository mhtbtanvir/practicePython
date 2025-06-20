from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []

    def create_a_car(self):
        rand = random.randint(1, 7)
        if rand == 1:

            New_car = Turtle("square")

            New_car.shapesize(stretch_wid=1, stretch_len=2)
            New_car.penup()
            New_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            New_car.goto(300, random_y)
            self.cars.append(New_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
