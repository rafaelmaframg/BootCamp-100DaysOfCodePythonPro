from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.level = 1
        self.write_screen(self.level)
    
    def write_screen(self, level):
        """
        Function to write the levels on the screen

        Args:
            level (int): the level to be shown on the screen
        """
        self.clear()
        self.write(f"Level: {level}", font=FONT)
    
    def write_game_over(self):
        """
        Function to write the game over when the turtle crash with a car
        """
        self.goto(-80,0)
        self.write("GAME OVER!!!", font=FONT)