import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.onkey(player.move_up, "Up")
    screen.update()
    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
    if player.ycor() > 280:
        player.finish_line()
        cars.level_up()

screen.exitonclick()