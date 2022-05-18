from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.show_score()
    
    def show_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"SCORE: {self.score}",move=False, align='center', font=("Arial", 10, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", move=False, align="center", font=("Arial", 14, "normal"))

    def sum_score(self):
        self.score += 1
        self.show_score()