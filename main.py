from turtle import Screen
from paddle import Paddle
from ball import Ball
from centreline import CentreLine
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Pong")

screen.tracer(0)

# Initialise Paddles
paddle_L = Paddle("L")
paddle_R = Paddle("R")



# Initialise Ball
ball = Ball()


# Initialise centre line
centre_line = CentreLine()

# Initialise Left Player Score Board
scoreboard_L = ScoreBoard(player="L")

# Initialise Right Player Score Board
scoreboard_R = ScoreBoard(player="R")

screen.listen()
screen.onkey(fun=paddle_L.move_up, key="w")
screen.onkey(fun=paddle_L.move_down, key="s")
screen.onkey(fun=paddle_R.move_up, key="Up")
screen.onkey(fun=paddle_R.move_down, key="Down")

game_is_on = True
while game_is_on:
    # Allows the ball to know where the paddles are
    left_paddle_location = [
                             [paddle_L.paddle_inside_x, paddle_L.paddle_outside_x],
                             [paddle_L.paddle_bottom_y, paddle_L.paddle_top_y]
                            ]
    right_paddle_location = [
                             [paddle_R.paddle_inside_x, paddle_R.paddle_outside_x],
                             [paddle_R.paddle_bottom_y, paddle_R.paddle_top_y]
                            ]
    ball.input_paddle_locations(left_paddle=left_paddle_location, right_paddle=right_paddle_location)
    # Update the screen
    screen.update()

    if ball.move():
        # Ball is able to move
        pass
    else:
        # Ball is unable to move, declare winner and reset game
        round_winner = ball.winner
        # TODO 2: update scoreboard
        if round_winner == "L":
            scoreboard_L.increment_score()
            scoreboard_L.clear()
            scoreboard_L.show_score()
        elif round_winner == "R":
            scoreboard_R.increment_score()
            scoreboard_R.clear()
            scoreboard_R.show_score()
        ball.reset_game()

screen.exitonclick()
