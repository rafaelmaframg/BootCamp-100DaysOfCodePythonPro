from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
machine = CoffeeMaker()
drinks = Menu()
while True:
    choice = str(input(f"What would you like? ({drinks.get_items()}):")).lower()
    if choice == "off":
        break
    elif choice == "report":
        machine.report()
        money.report()
    else:
        choice = drinks.find_drink(choice)
        if machine.is_resource_sufficient(choice):
            if money.make_payment(choice.cost):

                machine.make_coffee(choice)
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("Sorry there is not enough water.")
