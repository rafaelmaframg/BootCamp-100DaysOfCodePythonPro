import turtle as t
import random

timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)




for _ in range(72):
    timmy.color(((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))))
    timmy.circle(100)
    timmy.right(5)



screen = t.Screen()
screen.exitonclick()