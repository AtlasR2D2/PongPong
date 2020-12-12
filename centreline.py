from turtle import Turtle

DASH_LENGTH = 30
SPACE_LENGTH = 10
START_POSITION_X = 0
START_POSITION_Y = -300
END_POSITION_X = 0
END_POSITION_Y = 300
HEADING_SOUTH = 90

class CentreLine(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        # Draw a dashed line through the middle
        self.penup()
        self.goto(x=START_POSITION_X, y=START_POSITION_Y)
        self.setheading(HEADING_SOUTH)
        blnDash = True
        blnExit = False
        while self.ycor() < END_POSITION_Y and not blnExit:
            if blnDash:
                blnExit = (self.ycor() + DASH_LENGTH > END_POSITION_Y)
                if blnExit:
                    continue
                self.pendown()
                self.forward(DASH_LENGTH)
                blnDash = False
            else:
                blnExit = (self.ycor() + SPACE_LENGTH > END_POSITION_Y)
                if blnExit:
                    continue
                self.penup()
                self.forward(SPACE_LENGTH)
                blnDash = True