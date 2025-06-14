import random
import os

logo = ("""
       

 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
""")

# Declare globals
player_score = 0
computer_score = 0
player = []
computer = []


def draw():

    return random.randint(2, 11)


def calculate_score(hand):
    score = sum(hand)
    return score


def blackjack(player_score, computer_score, player, computer):
    player_score = 0
    computer_score = 0
    player = []
    computer = []

    for i in range(2):
        player.append(draw())
        computer.append(draw())
    print(logo)

    player_score = calculate_score(player)
    computer_score = calculate_score(computer)
    print("")

    print(f"\nplayer hand:{player} score :{player_score}")
    print(f"computer hand:{computer} score :{computer_score}\n")
    if player_score >= 21 or computer_score >= 21:
        determine_winner(player_score, computer_score)

    players_turn(player_score, computer_score, player, computer)


def players_turn(player_score, computer_score, player, computer):

    while player_score < 21:
        choice = input(
            f"\nplayer : Hit or Stand?:Type 'h' to hit.any key to stand:  ").lower()
        if choice == "h":
            player.append(draw())
            player_score = calculate_score(player)
            print(f"\nHit:player hand:{player} score :{player_score}")
            print(f"Computer's hand: {computer}, score: {computer_score}\n")
            if player_score >= 21:
                determine_winner(player_score, computer_score)

        else:
            computers_turn(player_score, computer_score, player, computer)


def computers_turn(player_score, computer_score, player, computer):

    while computer_score < 17 or player_score > computer_score:
        computer.append(draw())
        computer_score = calculate_score(computer)
        print(f"\nHit:Computer's hand: {computer}, score: {computer_score}")
        print(f"player hand:{player} score :{player_score}\n")

        if computer_score >= 21:
            determine_winner(player_score, computer_score)
            return

    determine_winner(player_score, computer_score)


def determine_winner(player_score, computer_score):
    if player_score == 21:
        print("""
         **PLAYER WINS!**
        """)
    elif computer_score == 21:
        print("""
         **COMPUTER WINS!**
        """)

    elif player_score > 21:
        print("""
         **COMPUTER WINS!**
        """)

    elif computer_score > 21:
        print("""
         **PLAYER WINS!**
        """)

    elif computer_score > player_score:
        print("""
         **COMPUTER WINS!**
        """)

    elif player_score > computer_score:
        print("""
         **PLAYER WINS!**
        """)

    else:
        print("It's a Tie!")

    repeat = input("\npress x to quit any other key to continue:")

    if repeat != "x":
        os.system('cls')
        blackjack(player_score, computer_score, player, computer)

    else:
        return


blackjack(player_score, computer_score, player, computer)
