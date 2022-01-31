# ----------------------------------------------------------------------------
# File name   : snake.py
# Created By  : Heesoo Lim
# Created Date: 31/01/2022
# ---------------------------------------------------------------------------
import time
from turtle import Turtle, Screen

STARTING_COORDS = [(0, 0), (-20, 0), (-40, 0)]
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.coords = STARTING_COORDS
        self.snake_pieces = self.create_snake()
        self.head = self.snake_pieces[0]

    def create_snake(self):
        snake_pieces = []
        for c in self.coords:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.speed(0)
            turtle.penup()
            turtle.goto(c)
            snake_pieces.append(turtle)
        return snake_pieces

    def update_coords(self):
        coords = []
        for s in self.snake_pieces:
            coords.append(s.position())
        self.coords = coords

    def move(self):
        self.update_coords()
        # change the value of coordinate[i] to coordinate[i - 1]
        for i in range(len(self.snake_pieces) - 1, 0, -1):
            self.snake_pieces[i].goto(self.coords[i - 1])
        # self.snake_pieces[0].seth(heading)
        self.head.forward(20)

    def head_left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.seth(LEFT)

    def head_right(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def head_up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.seth(UP)

    def head_down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.seth(DOWN)

    def is_on_screen(self):
        x, y = self.coords[0]

        if -300 < x < 300 and -300 < y < 300:
            return True
        return False
