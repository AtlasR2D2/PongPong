from turtle import Turtle

INITIAL_PADDLE_SIZE = 20
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
X_POS_R = 350
Y_POS_R = 0
X_POS_L = -350
Y_POS_L = 0
MOVE_INCREMENT = 20


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_HEIGHT/PADDLE_WIDTH, stretch_len=PADDLE_WIDTH/PADDLE_WIDTH)
        self.fillcolor("white")
        self.penup()
        # Position Paddle
        if player == "L":
            self.goto(x=X_POS_L, y=Y_POS_L)
        elif player == "R":
            self.goto(x=X_POS_R, y=Y_POS_R)
        self.set_paddle_ends()

    def set_paddle_ends(self):
        self.paddle_top_y = self.ycor() + self.shapesize()[0] * INITIAL_PADDLE_SIZE / 2
        self.paddle_bottom_y = self.ycor() - self.shapesize()[0] * INITIAL_PADDLE_SIZE / 2
        if self.player == "L":
            paddle_side_ind = 1
        elif self.player == "R":
            paddle_side_ind = -1
        self.paddle_inside_x = self.xcor() + self.shapesize()[1] * INITIAL_PADDLE_SIZE / 2 * paddle_side_ind
        paddle_side_ind *= -1
        self.paddle_outside_x = self.xcor() + self.shapesize()[1] * INITIAL_PADDLE_SIZE / 2 * paddle_side_ind

        # print(f"Player: {self.player} inside paddle edge {self.paddle_inside_x}")
    def move_up(self):
        if not self.paddle_top_y + MOVE_INCREMENT > self.getscreen().window_height() / 2:
            self.goto(x=self.xcor(), y=self.ycor()+MOVE_INCREMENT)
            self.set_paddle_ends()

    def move_down(self):
        if not self.paddle_bottom_y - MOVE_INCREMENT < self.getscreen().window_height() / 2 * -1:
            self.goto(x=self.xcor(), y=self.ycor()-MOVE_INCREMENT)
            self.set_paddle_ends()
