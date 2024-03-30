from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.teleport(-120, 260)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", False, "right", FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write("Game Over", True, "center", ("Courier", 28, "bold"))
