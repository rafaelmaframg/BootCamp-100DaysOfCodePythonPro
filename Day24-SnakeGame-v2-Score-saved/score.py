from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        print(self.highscore)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.show_score()
    
    def read_highscore(self):
        with open("highscore.txt", 'r') as file:
            return int(file.readline())

    def show_score(self):
        """Function to show the score on the screen
        """
        self.clear()
        self.goto(0, 280)
        self.write(f"SCORE: {self.score}  HIGH SCORE {self.highscore}",move=False, align='center', font=("Arial", 10, "normal"))
    
    def update_highscore(self):
        """Function to update the high score if the score is greater than highscore
        """
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.show_score()

    def sum_score(self):
        """Function to sum +1 to score each food the snake eats
        """
        self.score += 1
        self.show_score()