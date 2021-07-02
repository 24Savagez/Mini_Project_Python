from turtle import Screen
from turtle import Turtle

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Turtle("square")
paddle.penup()
paddle.color("white")
# paddle.setheading(90)
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
    # paddle.forward(20)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
    # paddle.backward(20)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
