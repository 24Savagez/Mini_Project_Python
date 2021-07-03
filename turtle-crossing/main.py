import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(score.move_speed)
    screen.update()
    car.create_car()
    car.move()

    if player.ycor() == 280:
        score.increase_score()
        player.new_game()

    for cars in car.segment:
        if player.distance(cars) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
