from turtle import Turtle
import random
import time


INITIAL_BALL_SIZE = 20
BALL_WIDTH = 20
BALL_HEIGHT = 20
INITIAL_POS_X = 0
INITIAL_POS_Y = 0
MOVE_INCREMENT = 1
SLEEP_AMOUNT = 0.002

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_HEIGHT/BALL_WIDTH, stretch_len=BALL_WIDTH/BALL_WIDTH)
        self.fillcolor("white")
        self.penup()
        self.reset_game()
        self.new_heading = self.heading()
        self.speed("slow")
        self.winner = ""

    def rotate_ball(self, direction):
        # Rotate a random angle for the initial trajectory
        random.seed()
        random_heading = random.randint(-90, 90)
        # Determine new heading based on direction of travel
        # Think clockwise movement
        if direction == "R":
            if random_heading > 0:
                random_heading = 360 - random_heading
            elif random_heading < 0:
                random_heading = 90 + random_heading
            else:
                pass
        elif direction == "L":
            if random_heading > 0:
                random_heading = 180 - random_heading
            elif random_heading < 0:
                random_heading = 270 + random_heading
            else:
                random_heading = 180
        # Set random heading
        self.setheading(random_heading)

    def invert_ball_y(self, blnReverse):
        """will invert the ball if it hits the top or bottom edge"""
        # Determine new heading based on direction of travel
        # Think clockwise movement
        if self.heading() > 0 and self.heading() < 90:
            if blnReverse:
                self.new_heading = 180 - self.heading()
            else:
                self.new_heading = 360 - self.heading()
        elif self.heading() > 90 and self.heading() < 180:
            if blnReverse:
                self.new_heading = 90 - (self.heading() - 90)
            else:
                self.new_heading = 270 - (self.heading() - 90)
        elif self.heading() > 180 and self.heading() < 270:
            if blnReverse:
                self.new_heading = 360 - (self.heading() - 180)
            else:
                self.new_heading = 180 - (self.heading() - 180)
        elif self.heading() > 270 and self.heading() < 360:
            if blnReverse:
                self.new_heading = 270 - (self.heading() - 270)
            else:
                self.new_heading = 90 - (self.heading() - 270)
        else:
            pass
        # Set new heading
        self.setheading(self.new_heading)
    def input_paddle_locations(self, left_paddle, right_paddle):
        self.left_paddle = left_paddle

        self.right_paddle = right_paddle

    def set_ball_ends(self):
        self.ball_top_y = self.ycor() + self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.ball_bottom_y = self.ycor() - self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.ball_left_x = self.xcor() - self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.ball_right_x = self.xcor() + self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.ball_left_y = self.ycor()
        self.ball_right_y = self.ycor()

    def change_direction(self):
        if self.direction == "L":
            self.direction = "R"
        elif self.direction == "R":
            self.direction = "L"

    def reset_game(self):
        self.goto(x=INITIAL_POS_X, y=INITIAL_POS_Y)
        self.set_ball_ends()
        self.direction = "R"
        self.rotate_ball(self.direction)

    def move(self):
        """function will move the ball if it doesn't hit a wall"""
        """returns true if was able to move, false otherwise"""

        if abs(self.ball_left_x) >= 400:
            # LEFT edge reached, add a point to the other side and reset the game
            self.winner = "R"
            return False
        elif abs(self.ball_right_x) >= 400:
            # RIGHT edge reached, add a point to the other side and reset the game
            self.winner = "L"
            # LEFT/RIGHT edge reached, add a point to the other side and reset the game
            return False
        elif self.left_paddle[0][1] <= self.ball_left_x <= self.left_paddle[0][0] and \
                self.left_paddle[1][0] <= self.ball_left_y <= self.left_paddle[1][1] or \
                self.right_paddle[0][1] >= self.ball_right_x >= self.right_paddle[0][0] and \
                self.right_paddle[1][0] <= self.ball_right_y <= self.right_paddle[1][1]:
            # change direction and invert y
            self.change_direction()
            self.invert_ball_y(True)
            self.forward(MOVE_INCREMENT)
            self.set_ball_ends()
            self.winner = ""
            return True
        elif abs(self.ball_top_y) >= 300 or abs(self.ball_bottom_y) >= 300:
            self.invert_ball_y(False)
            time.sleep(SLEEP_AMOUNT)
            self.forward(MOVE_INCREMENT)
            self.set_ball_ends()
            self.winner = ""
            return True

        else:
            time.sleep(SLEEP_AMOUNT)
            self.forward(MOVE_INCREMENT)
            self.set_ball_ends()
            self.winner = ""
            return True
