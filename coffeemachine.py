import os
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}


resources = {
    "water": 200,
    "milk": 300,
    "coffee": 100,
    "money": 0,
}


def take_order():
    """Takes the user's order and returns the choice."""
    while True:
        user_choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice in menu:
            return user_choice
        elif user_choice == "off" or user_choice == "report" or user_choice == "clear":
            return user_choice
        else:
            print("Invalid choice. Please select from the menu.")


def process_order():
    while True:
        user_choice = take_order()  

        if user_choice == "off":
            return False
        elif user_choice == "clear":
            os.system('cls')

        elif user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"taka:{resources['money']}")
            return True
        elif user_choice in menu:

            drink = menu[user_choice]
            if check_resourses(drink["ingredients"]):
                if process_payment(drink["cost"], user_choice):
                    resources["water"] -= drink["ingredients"]["water"]
                    if "milk" in drink["ingredients"]:
                        resources["milk"] -= drink["ingredients"]["milk"]
                    resources["coffee"] -= drink["ingredients"]["coffee"]
                return True

            return True


def check_resourses(drink_ingredients):

    if drink_ingredients["water"] > resources["water"]:
        print("Sorry there is not enough water.please wait.")
        return False
    elif "milk" in drink_ingredients and drink_ingredients["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.you can order espresso")
        return False
    elif drink_ingredients["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.please wait.")
        return False
    else:
        return True


def customer_payment():

    print("please insert Coins")
    five_taka = int(input("How many 5 taka coins? :"))
    two_taka = int(input("How many 2 taka coins? :"))
    one_taka = int(input("How many 1 taka Coins? :"))

    total = five_taka*5 + two_taka*2 + one_taka

    return total


def process_payment(drink_cost, user_choice):
    total = customer_payment()
    change = total - drink_cost
    if drink_cost <= total:
        print(f"Here is {change} in change ")
        print(f"Here is your {user_choice}.Enjoy.")
        resources["money"] += drink_cost
        return True
    else:
        print("Not Enough Money")
        return False


while True:
    if not process_order():
        break  # Exit the main loop if process_order returns False
