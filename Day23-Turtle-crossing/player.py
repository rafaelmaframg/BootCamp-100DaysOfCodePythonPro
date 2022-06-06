from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self, shape = "turtle"):
        super().__init__(shape)
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def move_up(self):
        """
            Function to move the player along the screen
        """
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        """
            Function to check if the player reached the finish line
        """
        self.goto(STARTING_POSITION)