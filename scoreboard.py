from turtle import Turtle

FONT = {"Arial", 16, "Bold"}
ALIGNMENT = "Center"

class ScoreBoard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        if player == "L":
            self.goto(-45, 250)
        elif player == "R":
            self.goto(45, 250)
        self.score = 0
        self.show_score()

    def increment_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

