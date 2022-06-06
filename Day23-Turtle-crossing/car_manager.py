from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        """
            Function to generate a random car list
        """
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.turtlesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """
            Function to move each car in the car list on the screen
        """
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        """
        Function to increment the car speed each level up
        """
        self.speed += 5