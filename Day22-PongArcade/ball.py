from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
    
    def moving(self, status):
        game_on = status
        while game_on:
            if self.xcor() <= 360:
                new_y = self.ycor() -10
                new_x = self.xcor() -10
                self.goto(new_x, new_y)
            else:
                new_y = self.ycor() +10
                new_x = self.xcor() +10
                self.goto(new_x, new_y)


