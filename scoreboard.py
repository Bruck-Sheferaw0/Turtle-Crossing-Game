FONT = ("Courier", 24, "bold")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.updatescore()

    def updatescore(self):
        self.hideturtle()
        self.penup()
        self.goto(-290, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1


    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Courier", 24, "bold"))