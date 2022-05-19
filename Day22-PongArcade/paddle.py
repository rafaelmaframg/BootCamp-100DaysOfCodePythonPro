from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, player) -> None:
        super().__init__()
        self.player = player
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        if player == 1:
            self.goto(-350, 0)
        else:
            self.goto(350, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor()+20 )
        else:
           pass 
    
    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor()-20 )
        else:
            pass