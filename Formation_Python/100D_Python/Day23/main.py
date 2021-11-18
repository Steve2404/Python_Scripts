import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
new_car = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car.create_car()
    new_car.move_car()
    for car in new_car.all_car:
        if car.distance(player) < 25:
            game_is_on = False
    if player.is_at_finish_line():
        player.go_to_star()