from turtle import Turtle, Screen
import random
Screen = Screen()
Screen.setup(width=600, height=350)
colors = ["red", "orange", "yellow", "green",
          "blue", "purple", "black", "grey", "orange", "violet", "cyan", "magenta", "indigo", "pink", "brown"]
players = []
coordinates = [-280, -150]
end_line = 270

user_bet = Screen.textinput(
    "Make your bet", "Which turtle will win the race? Enter a color:").lower()


def create_players(number_of_players):
    for _ in range(number_of_players):
        player = Turtle(shape="turtle")
        player.color(colors[_])

        players.append(player)

    setup_race(players)


def setup_race(players):

    for player in players:
        player.penup()
        player.goto(coordinates)
        coordinates[1] += 330/len(players)
        # player.pendown()
        # player.pensize(30)


Screen.listen()


def start_game():
    # user_bet = Screen.textinput(
    #     "Make your bet", "Which turtle will win the race? Enter a color:").lower()

    Screen.onkey(key="space", fun=race)
    # race()


def race():

    while True:
        for player in players:

            player.forward(random.randint(1, 10))
            if player.xcor() >= end_line:
                if player.color()[0] == user_bet:
                    Screen.textinput(
                        "Congrats!! You won", "The winner is: "+player.color()[0])
                    return
                else:
                    Screen.textinput(
                        "Sorry", "The winner is: "+player.color()[0])
                    return


create_players(14)
start_game()

Screen.exitonclick()
