from re import S
from tracemalloc import get_tracemalloc_memory
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

p1 = Paddle(1)
p2 = Paddle(2)
ball = Ball()
score = Score()



screen.onkey(p1.move_up,"Up")
screen.onkey(p1.move_down,"Down")
screen.onkey(p2.move_up,"w")
screen.onkey(p2.move_down,"s")



game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.moving()
    if ball.distance(p2) < 50 and ball.xcor() > 320 or ball.distance(p1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if  ball.xcor() < -400:
        ball.reset()
        p1.reset()
        score.increment(2)
        score.show_score()

    elif ball.xcor() > 400:
        p2.reset()
        ball.reset()
        score.increment(1)
        score.show_score()
        



screen.exitonclick()
