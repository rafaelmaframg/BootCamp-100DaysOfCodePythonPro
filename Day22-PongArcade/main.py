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
timer = 10
divisor = 100
while game_on:
    if timer == 0:
        timer = 10
        divisor = 1000
    time.sleep(timer/divisor)
    screen.update()
    ball.moving()
    
    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        timer -= 1
        ball.bounce_x()

    if  ball.xcor() < -380:
        ball.reset_ball()
        p1.reset(1)
        p2.reset(2)
        timer = 10
        divisor = 100
        score.increment(2)
        score.show_score()

    elif ball.xcor() > 380:
        ball.reset_ball()
        p2.reset(2)
        p1.reset(1)
        timer = 10
        divisor = 100  
        score.increment(1) 
        score.show_score()
        



screen.exitonclick()
