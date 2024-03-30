from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("YellowGreen")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)
