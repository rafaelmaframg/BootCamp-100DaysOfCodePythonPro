from turtle import Turtle, Screen
import random

timmy =Turtle()
timmy.color("red")
colors = ["cornflower blue", "lime", "orchid", "gold"]
num_sides = 5

def drawn_shaper(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side in range(3,11):
    timmy.color(random.choice(colors))
    drawn_shaper(shape_side)









screen = Screen()
screen.exitonclick()