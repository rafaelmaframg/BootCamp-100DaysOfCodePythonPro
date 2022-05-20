from tracemalloc import get_tracemalloc_memory
from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

p1 = Paddle(1)
p2 = Paddle(2)
ball = Ball()

ball.moving(True)

screen.onkey(p1.move_up,"Up")
screen.onkey(p1.move_down,"Down")
screen.onkey(p2.move_up,"w")
screen.onkey(p2.move_down,"s")



game_on = True
while game_on:
    screen.update()




screen.exitonclick()
