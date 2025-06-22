# Rock Paper Scissors ASCII Art

import random
Rock = ''' Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = ''' Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = ''' Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def rockpapersissor():
    # Rock Paper Scissors Game
    choices = [Rock, Paper, Scissors]
    print("Welcome to Rock, Paper, Scissors!")
    print("Rock = 0, Paper = 1, Scissors = 2")
    print("You have 3 choices to play the game.")
    print("You can choose Rock, Paper, or Scissors.")

    person_choice = int(
        input(f"What do you choose? \nType 0 for Rock, 1 for Paper, or 2 for Scissors.Here :\n"))
    computer_choice = random.randint(0, 2)
    if (person_choice < 0 or person_choice > 2):
        print("Invalid choice! Please choose 0, 1 or 2 next time.You lose }!")
        rockpapersissor()
    else:
        print(f"person chose :{choices[person_choice]}")
        print(f"Computer chose :{choices[computer_choice]}")

        if computer_choice == person_choice:
            print("It's a draw!")
        elif (computer_choice == 0 and person_choice == 2) or \
            (computer_choice == 1 and person_choice == 0) or \
                (computer_choice == 2 and person_choice == 1):
            print("You lose!")
        else:
            print("You win!")
    if input(f"To play agin type Y:").lower() == "y":
        rockpapersissor()


rockpapersissor()
