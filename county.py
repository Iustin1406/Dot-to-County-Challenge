from turtle import Turtle


class County(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_cor = 0
        self.y_cor = 0