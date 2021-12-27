# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append({r, g, b})
#
# print(rgb_colors)
import random
import turtle as turtle_module

color_list = [{132, 205, 166}, {106, 148, 221}, {32, 42, 61}, {135, 148, 199}, {48, 58, 166}, {184, 162, 141},
              {105, 157, 39}, {90, 212, 237}, {66, 59, 150}, {216, 82, 71}, {168, 33, 29}, {235, 165, 157},
              {90, 51, 111}, {35, 61, 55}, {33, 156, 31}, {17, 97, 71}, {49, 52, 44}, {161, 166, 230}, {170, 188, 221},
              {48, 57, 51}, {184, 113, 103}, {32, 60, 109}, {105, 126, 159}, {200, 188, 175}, {210, 34, 151},
              {56, 65, 66}]

tim = turtle_module.Turtle()
# tim.pen(pendown=False)
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
