from turtle import Turtle


class Name_Writter(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()

    def show_state(self, name, x, y):
        """Function to write on screen the state

        Args:
            name (Str): State name from the Df
            x (int): position x 
            y (int): position y
        """
        self.goto(x,y)
        self.write(name)