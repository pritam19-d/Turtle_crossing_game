import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_COR = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.move_car()

    def create_car(self):
        num = random.randint(0,6)
        if num == 3 or num == 4:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.teleport(320, random.choice(Y_COR))
            car.shapesize(1, 2)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT


class RoadMark(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(3)
        self.teleport(-320,Y_COR[0]-20)
        self.forward(630)
        for y in Y_COR[1:]:
            self.teleport(-360, y - 20)
            self.draw_dotted_line()
        self.teleport(-320, Y_COR[len(Y_COR)-1]+20)
        self.forward(630)

    def draw_dotted_line(self):
        for _ in range(25):
            self.penup()
            self.forward(10)
            self.pendown()
            self.forward(20)
