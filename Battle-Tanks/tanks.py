import random
from turtle import Turtle

PLAYER_COLOR = "gold"
COM_COLOR = ["red", "blue", "yellow"]
PLAYER_POSITION = (-60, -280)
COM_POSITION = [(-280, 280), (280, 280)]
COM_HEAD = (90, 180, 270)


class Tank(Turtle):

    def __init__(self):
        super().__init__()
        self.all_com_tanks = []
        self.level = 1
        self.create_player_tank()
        self.create_com_tank()

    def create_player_tank(self):
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color(PLAYER_COLOR)
        self.setheading(90)
        self.goto(PLAYER_POSITION)

    def create_com_tank(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1 and len(self.all_com_tanks) < round(3 + self.level * 2):
            new_tank = Turtle("turtle")
            new_tank.penup()
            new_tank.shapesize(stretch_len=1.5, stretch_wid=1.5)
            new_tank.color(random.choice(COM_COLOR))
            new_tank.setheading(270)
            new_tank.goto(random.choice(COM_POSITION))
            self.all_com_tanks.append(new_tank)

    def com_move(self):
        for tanker in self.all_com_tanks:
            tanker.forward(3)
            tanker.shape("square")
            tanker.penup()
            tanker.color("white")
            tanker.setheading(270)
            tanker.shapesize(stretch_wid=0.2, stretch_len=0.5)
            tanker.forward(20)

    def find_wall(self):
        pass
