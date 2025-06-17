from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time


random_xcor = random.randint(-350, 350)
random_ycor = random.randint(-280, 280)

screen = Screen()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
Turtle().speed("fastest")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


border = Turtle()
border.color("white")
border.pensize(5)
border.penup()
border.goto(0, -300)
border.setheading(90)
for i in range(16):
    border.pendown()
    border.forward(20)
    border.penup()
    border.forward(20)
border.hideturtle()


screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() < -320 or ball.xcor() > 320:

        if ball.distance(l_paddle) < 50:

            ball.bounce_x()
            scoreboard.l_score += 1
            scoreboard.update_scoreboard()

        elif ball.distance(r_paddle) < 50:
            ball.bounce_x()
            scoreboard.r_score += 1
            scoreboard.update_scoreboard()
        else:
            scoreboard.goto(0, 0)

            scoreboard.write("Game Over.Ball out of bounds.", align="center",
                             font=("Courier", 24, "normal"))

            game_is_on = False


screen.exitonclick()
