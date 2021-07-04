import time
from turtle import Turtle, Screen
from tanks import Tank

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)

base = Turtle("classic")
base.penup()
base.setheading(90)
base.color("gray")
base.shapesize(stretch_len=3, stretch_wid=3)
base.goto(0, -260)
screen.tracer(0)

for x in range(8):
    wall_base = Turtle("square")
    wall_base.penup()
    wall_base.color("saddle brown")
    if 2 <= x <= 5:
        wall_base.goto(-30 + (20 * (x - 2)), - 240)
    elif 6 <= x <= 7:
        wall_base.goto(30, -(260 + 20 * (x - 6)))
    else:
        wall_base.goto(-30, -(280 - 20 * x))

player = Tank()
player.create_player_tank()
player.create_com_tank()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.create_com_tank()
    player.com_move()




screen.exitonclick()
