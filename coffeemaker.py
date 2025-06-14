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
    "water": 300,
    "milk": 300,
    "coffee": 100,
    "money": 0,
}


def take_order():
    drink_choice = input(
        "what would you like? (espresso/latte/cappuccino): ").lower()
    if drink_choice in menu:
        return drink_choice
    elif drink_choice == "off":
        return drink_choice

    elif drink_choice == "report" or drink_choice == "clear":
        return drink_choice
    else:
        print("invalid choice")
        return True


def process_order():
    while True:
        coffee_choice = take_order()
        if coffee_choice == "off":

            return False
        elif coffee_choice == "report":
            print(f"water :{resources["water"]}")
            print(f"milk :{resources["milk"]}")
            print(f"coffee :{resources["coffee"]}")
            print(f"money :{resources["money"]}")
            return True
        elif coffee_choice == "clear":
            os.system("cls")
        elif coffee_choice in menu:
            user_drink = menu[coffee_choice]
            if check_resources(user_drink["ingredients"]):
                if process_payment(user_drink["cost"], coffee_choice):
                    resources["water"] -= user_drink["ingredients"]["water"]
                    resources["coffee"] -= user_drink["ingredients"]["coffee"]
                    if "milk" in user_drink["ingredients"]:
                        resources["milk"] -= user_drink["ingredients"]["milk"]
                    resources["money"] = +user_drink["cost"]
                return True
            return True


def check_resources(ingredients):
    if ingredients["water"] > resources["water"]:
        print("Sorry.nt enough water")
        return False
    elif "milk " in ingredients and ingredients["milk"] > resources["milk"]:
        print("Sorry.not enough milk")
        return False
    if ingredients["coffee"] > resources["coffee"]:
        print("Sorry.nt enough coffee")
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
        print(f"Here is {change} taka in change ")
        print(f"Here is your {user_choice}.Enjoy.")
        resources["money"] += drink_cost
        return True
    else:
        print("Not Enough Money")
        return False


while True:
    if not process_order():
        break  # Exit the main loop if process_order returns False
