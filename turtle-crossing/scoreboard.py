from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 250)
        self.update_scoreboard()
        self.move_speed = 0.1

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.move_speed *= 0.8
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

