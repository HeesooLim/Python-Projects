from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.display_score()

    def display_score(self):
        """Display current score"""
        self.clear()
        self.setpos(-280, 270)
        self.write(f"Score: {self.score}", move=False, align='left', font=('Arial', 15, 'normal'))
        self.setpos(280, 270)
        self.write(f"High score: {self.high_score}", move=False, align='right', font=('Arial', 15, 'normal'))

    def update_score(self):
        """Add and display the score"""
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.score))
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

    def reset(self):
        self.score = 0
        self.display_score()

