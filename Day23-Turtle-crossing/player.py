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
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        self.goto(STARTING_POSITION)