# ----------------------------------------------------------------------------
# File name   : snake.py
# Created By  : Heesoo Lim
# Created Date: 31/01/2022
# ---------------------------------------------------------------------------
from turtle import Turtle

STARTING_COORDS = [(0, 0), (-20, 0), (-40, 0)]
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.coords = STARTING_COORDS
        self.snake_pieces = []
        self.create_snake()
        self.head = self.snake_pieces[0]

    def create_snake(self):
        """Create a snake"""
        for c in self.coords:
            self.add_piece(c)

    def update_coords(self):
        """Update current coordinates"""
        coords = []
        for s in self.snake_pieces:
            coords.append(s.position())
        self.coords = coords

    def move(self):
        self.update_coords()
        # change the value of coordinate[i] to coordinate[i - 1]
        for i in range(len(self.snake_pieces) - 1, 0, -1):
            self.snake_pieces[i].goto(self.coords[i - 1])
        self.head.forward(20)

    def add_piece(self, position):
        """Add a snake piece"""
        turtle = Turtle("square")
        turtle.color("white")
        turtle.speed(0)
        turtle.penup()
        turtle.setpos(position)
        self.snake_pieces.append(turtle)

    def extend_snake(self):
        """Add a snake piece at the end of the list"""
        self.add_piece(self.snake_pieces[-1].position())

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

    def reset(self):
        for s in self.snake_pieces:
            s.hideturtle()
        self.coords = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_pieces = []
        self.create_snake()
        self.head = self.snake_pieces[0]

    def is_game_over(self):
        """Check if the game is over (hit the wall or body)"""
        # head's coordinates
        x, y = self.coords[0]
        # if the snake hits the wall
        if -280 < x < 280 and -280 < y < 280:
            # if the snake hits its body
            for c in self.coords[1:]:
                if self.head.distance(c) < 10:
                    return False
            return True
        return False
