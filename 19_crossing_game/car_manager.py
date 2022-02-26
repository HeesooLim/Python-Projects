from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def create_car():
    car = Turtle()
    car.penup()
    car.setpos(random.randint(300, 1500), random.randint(-160, 250))
    car.shape('square')
    car.shapesize(stretch_wid=1, stretch_len=2)
    color = random.choice(COLORS)
    car.pencolor(color)
    car.fillcolor(color)
    return car


def check_distance(car, player_x, player_y):
    if car.ycor() + 20 > player_y > car.ycor() - 20 and car.xcor() + 25 > player_x > car.xcor() - 25:
        return True
    else:
        return False


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        for i in range(50):
            self.cars.append(create_car())

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.speed, car.ycor())
        self.manage_cars()

    def manage_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)
                self.cars.append(create_car())

    def level_up(self):
        self.speed += MOVE_INCREMENT
