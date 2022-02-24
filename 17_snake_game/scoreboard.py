from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        """Display current score"""
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 15, 'normal'))

    def update_score(self):
        """Add and display the score"""
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        """Display the game over screen"""
        self.screen.clearscreen()
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.goto(0, 15)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 15, 'normal'))
        self.goto(0, -15)
        self.write(f"Final Score: {self.score}", move=False, align='center', font=('Arial', 15, 'normal'))


