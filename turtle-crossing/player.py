from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.finish = FINISH_LINE_Y

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def new_game(self):
        self.goto(STARTING_POSITION)
