from turtle import Screen
from turtle import Turtle
from player import Player
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard(screen)
player1 = Player(-360, screen)
player2 = Player(360, screen)

screen.onkey(player2.move_up, "Up")
screen.onkey(player2.move_down, "Down")

screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")

turtle = Turtle()

screen.listen()

while True:
    screen.update()

    ball.move()
    if not (240 > ball.ycor() > -240):
        ball.bounce_y()

    if (not (340 > ball.xcor() > -340)) and (ball.distance(player1.pos()) < 50 or ball.distance(player2.pos()) < 50):
        ball.bounce_x()

    if ball.xcor() > 385:
        scoreboard.player1_win()
        ball.reset_ball()
    if ball.xcor() < -385:
        scoreboard.player2_win()
        ball.reset_ball()
