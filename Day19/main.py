import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)

choice = screen.textinput("Make your bet", "Who will win the race? Enter a colour:")

list_turtles = {"red": t.Turtle(shape="turtle"), "blue": t.Turtle(shape="turtle"), "yellow": t.Turtle(shape="turtle"), "green": t.Turtle(shape="turtle"), "orange": t.Turtle(shape="turtle"), "purple": t.Turtle(shape="turtle")}

y = -120
for color,turtle in list_turtles.items():
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-200, y=y)
    y += 50

if choice:
    race_on = True

    while race_on:
        for color,turtle in list_turtles.items():
            turtle.forward(random.randint(1,10))
            if turtle.xcor() >= 215:
                winner = color
                race_on = False
    print(f"The turtle {winner} is the winner!")            
    if choice == winner:
        print("You've Win!!! ")
    else:
        print("You've Lost!!!") 

screen.exitonclick()