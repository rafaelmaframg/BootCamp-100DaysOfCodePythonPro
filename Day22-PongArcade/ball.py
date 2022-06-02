from turtle import Turtle


class Ball(Turtle):

    velocity = 5

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.y_increment = 10
        self.x_increment = 10
        self.penup()

    def moving(self):
        """
        Function to move the ball along the screen
        """
        new_y = self.ycor() + self.y_increment
        new_x = self.xcor() + self.x_increment
        self.goto(new_x, new_y)
        if self.ycor() == 280 or self.ycor() == -280:
            self.y_increment *= -1

    def bounce_x(self):
        """
        Function to change the ball direction
        """
        self.x_increment *= -1

    def reset_ball(self) -> None:
        """
        Function to Reset the ball to initial position when the ball disappears on the screen
        """
        self.goto(0,0)
        self.bounce_x()

    def increment_velocity(self):
        """
        Function that increases speed each time the ball is hit 
        """
        self.y_increment += 10
        self.x_increment += 10



