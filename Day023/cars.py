from turtle import Turtle
from random import choice, randint

X = 300
SPEED = 10
COLORS = ('black', 'yellow', 'green', 'brown', 'orange', 'red', 'purple', 'blue')


class Car:
    def __init__(self):
        self.all_cars = []
        self.get_new_car()
        self.go_forward()
        self.car_speed = 0.5

    def get_new_car(self):
        if randint(0, 50) == 25:
            ran_y = randint(-250, 280)
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(X, ran_y)
            self.all_cars.append(new_car)

    def go_forward(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def level_up(self):
        self.car_speed += 0.2


