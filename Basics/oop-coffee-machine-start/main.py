from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


MoneyMachine = MoneyMachine()
CoffeeMaker = CoffeeMaker()
machine_on = True
while machine_on == True:

    print(Menu().get_items())
    choose = input("whats your drink?:").lower()
    choice = Menu().find_drink(choose)

    if choose == "off":
        print("off.\n.\n.\n.\n.\n.off")
        machine_on = False
    elif choose == "report":
        CoffeeMaker.report()
        MoneyMachine.report()

    elif choice:
        if CoffeeMaker.is_resource_sufficient(choice):
            if MoneyMachine.make_payment(choice.cost):

                CoffeeMaker.make_coffee(choice)

    else:
        print("invalid choice")
