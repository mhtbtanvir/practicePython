from turtle import Turtle, Screen
import food

FONT = ("Arial", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()

        with open("data.txt") as data:
            self.Highscore = data.read()

        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def reset(self):
        self.update_scoreboard()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.Highscore = int(self.Highscore)
        if self.score > self.Highscore:
            self.Highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.Highscore}")

        self.write(f"Score: {self.score}  Highscore: {self.Highscore}",
                   align="center",
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)

        self.write(f"Game Over",
                   align="center",
                   font=FONT)

    # def boundary(self):
    #     self.hideturtle()
    #     self.pendown()
    #     self.color("white")
    #     self.speed("fastest")
    #     self.goto(-290, 270)
    #     self.forward(580)  # Corrected length to 580
    #     self.setheading(270)
    #     self.forward(540)  # Corrected length to 540
    #     self.setheading(180)
    #     self.forward(580)  # Corrected length to 580
    #     self.setheading(90)  # Corrected heading to 90
    #     self.forward(540)  # Corrected length to 540
    #     self.penup()
    #       # Hide the turtle after drawing the boundary

    def increase_score(self):
        self.score += 1
        self.clear()

        self.update_scoreboard()
