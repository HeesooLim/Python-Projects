# ----------------------------------------------------------------------------
# File name   : food.py
# Created By  : Heesoo Lim
# Created Date: 01/02/2022
# ---------------------------------------------------------------------------


from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        self.COLORS = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
                  'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white']

        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color(random.choice(self.COLORS))
        self.speed("fastest")
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.goto(self.x, self.y)

    def get_position(self):
        """Get the current position of the food"""
        return (self.x, self.y)

    def regen_food(self):
        """Regenerate the food"""
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.goto(self.x, self.y)
        self.color(random.choice(self.COLORS))
