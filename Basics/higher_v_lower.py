import random
follwer_set = {
    "naymer": 100,
    "messi": 98,
    "ronaldo": 95,
    "mbappe": 88,
    "kane": 87,
    "pogba": 85,
    "zidane": 80,
    "modric": 75,
    "xavi": 65,
    "cruyff": 50,
    "ronaldinho": 45,
    "zidane": 40,


}
pickerB = random.choice(list(follwer_set.keys()))

score = 0


def play(score, pickerB):  # Added score as a parameter with a default value of 1
    """Plays a round of the higher/lower game."""

    pickerA = pickerB
    pickerB = random.choice(list(follwer_set.keys()))

    person_a_value = follwer_set[pickerA]
    person_b_value = follwer_set[pickerB]

    print(f"person A : {pickerA}")
    print(f"person B : {pickerB}")

    # Convert input to uppercase
    choose = input("person A or person B? Who has higher follower: ").upper()

    if (choose == "A" and person_a_value > person_b_value):
        print("You win!")
        score += 1  # Increment score only if the player wins
        play(score, pickerB)  # Recursive call with the updated score
    elif (choose == "B" and person_b_value > person_a_value):

        print("You win!")
        score += 1  # Increment score only if the player wins
        play(score, pickerB)  # Recursive call with the updated score
    else:
        print(f"You're Wrong. Score is {score}")
        return


play(score, pickerB)
