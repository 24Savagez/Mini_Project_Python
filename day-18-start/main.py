# Turtle Intro
from turtle import Screen
import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = t.Turtle()
t.colormode(255)
tim.width(1)
tim.speed("fastest")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]


# tim.shape("arrow")
# tim.color("red")

# Basic move
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

# Challenge 1 - Draw a Square
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)

# Challenge 2 - draw dash-line
# for _ in range(4):
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.left(90)

# Challenge 3 - draw other sharp
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# Challenge 4 - draw a random walk
# for _ in range(2000):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(20)

# Challenge 5 - draw a spirograph
def draw_spirograph(radium, size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.pencolor(random_color())
        tim.circle(radium)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(120, 5)
screen = Screen()
screen.exitonclick()
