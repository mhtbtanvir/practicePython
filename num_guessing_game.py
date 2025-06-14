import random



def guess_num(Chosen_num):
    guessed_num = int(input("make a guess: "))
    if guessed_num > Chosen_num:
        print("Too High")
        return False

    elif guessed_num < Chosen_num:
        print("Too Low")
        return False
    else:
        print("You've Got IT")
        return True


def easy_func(Chosen_num):
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number ")

        if guess_num(Chosen_num):
            play()
        attempts -= 1

    print(f"You've ran out of aattempts.Number is {Chosen_num}")


def hard_func(Chosen_num):
    attempts = 5
    while attempts > 0:

        print(f"You have {attempts} attempts remaining to guess the number ")
        if guess_num(Chosen_num):
            play()

        attempts -= 1

    print(f"You've run out of attempts, you lose.Number is {Chosen_num}")


def play():

    Chosen_num = random.randint(1, 100)
    print("im thinking of a number between 1 to 100")

    difficulty = input("choose  difficulty.type easy or hard : ").lower()
    if difficulty == "easy":
        easy_func(Chosen_num)
    else:
        hard_func(Chosen_num)


play()
