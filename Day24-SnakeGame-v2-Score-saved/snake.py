from turtle import Turtle

START_POSITIONS = [(0, 0),(-20, 0),(-40, 0),(-60, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        """
        Function to create a snake with each position point
        """
        for position in START_POSITIONS:
            self.add_segment(position)

    def delete_snake(self):
        """
        Function to make the snake invisble when the player loses the match
        """
        for segment in self.segments:
            segment.hideturtle()
    

    def add_segment(self, position):
        """Function to add a new piece of snake,
        each piece is a object type 

        Args:
            position (tuple): position x,y
        """
        self.new_segment= Turtle(shape="square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)

    def new_piece(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        