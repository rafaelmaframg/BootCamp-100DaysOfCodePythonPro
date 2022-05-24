from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.player1 = 0
        self.player2 = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.show_score()
        
    def show_score(self):
        self.clear()
        self.write(f"Player 1 = {self.player1}     Player 2 = {self.player2}", False, align="center",  font=('Arial', 10, 'normal'))
    
    def increment(self, player):
        if player == 1:
           self.player1 += 1
        else:
            self.player2 += 1
