# ----------------------------------------------------------------------------
# File name   : main.py
# Created By  : Heesoo Lim
# Created Date: 31/01/2022
# ---------------------------------------------------------------------------
import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(screen)

screen.listen()

screen.onkey(snake.head_up, "Up")
screen.onkey(snake.head_down, "Down")
screen.onkey(snake.head_left, "Left")
screen.onkey(snake.head_right, "Right")
# up = snake.turn(90)
# down = snake.turn(270)
# left = snake.turn(180)
# right = snake.turn(0)

while snake.is_on_screen():
    snake.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
