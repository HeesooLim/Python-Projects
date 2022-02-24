# ----------------------------------------------------------------------------
# File name   : main.py
# Created By  : Heesoo Lim
# Created Date: 31/01/2022
# ---------------------------------------------------------------------------
import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(screen)
food = Food()
score = Scoreboard(screen)

screen.listen()

screen.onkey(snake.head_up, "Up")
screen.onkey(snake.head_down, "Down")
screen.onkey(snake.head_left, "Left")
screen.onkey(snake.head_right, "Right")

while snake.is_game_over():
    snake.move()
    screen.update()
    time.sleep(0.1)

    x, y = food.get_position()

    # check if the snake touched the food
    if snake.head.distance(x, y) <= 15:
        snake.extend_snake()
        food.regen_food()
        score.update_score()

score.game_over()
screen.exitonclick()
