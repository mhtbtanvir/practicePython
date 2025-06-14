height = (int(input("wall height:")))
width = (int(input("wall width: ")))
covarage = 5


def calc_can_of_paint(height, width, covarge):
    can_needed = (height*width)/covarage
    print(f"need {round(can_needed)} can of paint")


calc_can_of_paint(height, width, covarage)
############################################################################
Your_number = int(input("enter a number to check if its a prime number:"))


def prime_number_checker(Your_number):
    count = 0
    is_prime = True

    for i in range(2, Your_number):
        if Your_number % i == 0:
            print(f"its not a prime number.sorry .can be divided by:{i}")
            count += 1
            is_prime = False
    if count == 0 and is_prime == True:
        print(f"{Your_number} is indeed a prime ! nice job!wow!")


prime_number_checker(Your_number)
