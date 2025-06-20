import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

scoreboard = Scoreboard()

Cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    Cars.create_a_car()
    Cars.move_cars()

    for car in Cars.cars:
        if car.distance(player) < 20:
            game_is_on = False

            scoreboard.game_over()

    if player.player_at_finish_line():
        player.goto_start()
        Cars.level_up()
        scoreboard.increase_score()


screen.exitonclick()
