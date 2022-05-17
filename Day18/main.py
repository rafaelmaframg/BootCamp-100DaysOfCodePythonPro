import colorgram
import turtle as t
import random

colors = colorgram.extract('Dots-scaled.jpg',30)
list_colors = []

for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    list_colors.append((r,g,b))

t.colormode(255)
list_colors = list_colors[2:]
timmy = t.Turtle()
timmy.speed("fastest")
timmy.hideturtle()
y = -220
for _ in range(10):
    timmy.penup()
    timmy.setx(-250)    
    timmy.sety(y)
    timmy.pendown()
    y += 50
    for _ in range(10):
        timmy.dot(20, random.choice(list_colors))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

t.done()


