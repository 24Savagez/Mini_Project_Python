# Turtle Intro
from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
colors = ["deep sky blue", "pale green", "firebrick", "medium violet red",
          "orchid", "gold", "rosy brown", "pale violet red"]


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


screen = Screen()
screen.exitonclick()
