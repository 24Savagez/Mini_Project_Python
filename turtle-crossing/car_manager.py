from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.segment = []
        self.hideturtle()
        self.create_car()
        self.move()

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_y = random.randrange(-240, 260, 60)
        new_car.goto(320, new_y)
        self.segment.append(new_car)

    def move(self):
        for number in range(1, len(self.segment), STARTING_MOVE_DISTANCE):
            new_x = self.segment[number].xcor() - MOVE_INCREMENT
            new_y = self.segment[number].ycor()
            self.segment[number].goto(new_x, new_y)
