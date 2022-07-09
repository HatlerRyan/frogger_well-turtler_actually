from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
gen_car = 0


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        new_car = CarManager()
        new_car.shape("square")
        new_car.penup()
        new_car.resizemode("user")
        new_car.shapesize(1, 2)
        new_car.setheading(180)
        rand_color = random.choice(COLORS)
        new_car.color(rand_color)
        y_cor = random.randint(-250, 250)
        new_car.goto(280, y_cor)
        self.all_cars.append(new_car)

    def move_car(self, level):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + level)

    # def detect_collision(self, pc_ycor):
    #     for car in self.all_cars:
    #  def speed_up(self, increase):



