from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, player) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.reset(player)
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def move_up(self):
        """
        Function to move up the paddle
        """
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor()+20 )
        else:
           pass 
    
    def move_down(self):
        """
        Function to move down the paddle
        """
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor()-20 )
        else:
            pass

    def reset(self, player) -> None:
        """
        Function to reset the paddle to initial postion

        Args:
            player (Int): Player number
        """
        if player == 2:
            self.goto(-350, 0)
        else:
            self.goto(350, 0)
        