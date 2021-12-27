from turtle import Turtle

STARTING_POSITION = [(0, 0), (-30, 0), (-30, 0)]


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_net()

    def create_net(self):
        for position in range(20):
            new_net = Turtle("square")
            new_net.color("white")
            new_net.penup()
            new_net.goto(0, -280 + position*30)
            new_net.shapesize(stretch_len=0.25, stretch_wid=0.5)
            self.segments.append(new_net)
