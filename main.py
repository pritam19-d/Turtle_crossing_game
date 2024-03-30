import time
from turtle import Screen
from player import Player
from car_manager import CarManager, RoadMark
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("gray40")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Rode-Crossing Game")

scoreboard = Scoreboard()
turtle = Player()
car_manager = CarManager()
RoadMark()
screen.listen()
screen.onkeypress(turtle.move_up, "Up")
screen.onkeypress(turtle.move_down, "Down")

game_is_on = True
while game_is_on:
    if turtle.ycor() > 300:
        scoreboard.update_level()
        car_manager.level_up()
        turtle.teleport(0, -280)
    for each in car_manager.all_cars:
        if turtle.distance(each) < 21:
            scoreboard.game_over()
            game_is_on = False
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_car()
    screen.update()

screen.exitonclick()
