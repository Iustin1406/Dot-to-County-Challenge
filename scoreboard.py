from turtle import Turtle


class Header(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -3
        self.hideturtle()
        self.penup()
        self.goto(-100,350)
        self.current_county = "a"
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Click on {self.current_county} county\nYou guessed {self.score}/41", font=("Arial", 20, "normal"))

    def game_over(self):
        self.clear()
        self.write("Congratulations! You guessed all the counties!", font=("Arial", 20, "normal"))



