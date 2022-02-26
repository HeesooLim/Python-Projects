import time
from turtle import Screen
from turtle import Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    scoreboard.display_level()
    is_crashed = False
    for car in car_manager.cars:
        if car.ycor() + 20 > turtle.ycor() > car.ycor() - 20 and car.xcor() + 25 > turtle.xcor() > car.xcor() - 25:
            is_crashed = True

    car_manager.move_cars()

    if is_crashed:
        scoreboard.game_over()
        break

    if turtle.ycor() > 300:
        turtle.reset_position()
        car_manager.level_up()
        scoreboard.level_up()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
