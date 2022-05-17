MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": (300, "ml"),
    "milk": (200, "ml"),
    "coffee": (100, "g"),
    "money": ("$",0 ),
}

def report():
    """
        Function to generate a report that shows the current resource values.
        e.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g 
        Money: $2.5
  
        Returns:
            list with keys and values from resources dict
    """
    return [x.capitalize() + ": " + str(y[0]) + str(y[1]) +"\n" for x,y in resources.items()]

def turn_off(status):
    """
        Function to turn on or turn off the coffee machine.
  
        Parameters:
            status(bool): Actual machine status.
          
        Returns:
            (bool): return True or False to turn on or turn off the machine.
    """
    if status == True:
        return False
    return True

def check_resources(choice):
    """
        Function to check resource to make the choice.

        Parameters:
            choice: (str) string that contains the choice
        Returns:
            (bool) True if the resources is enough False if no
    """
    resource_choice = MENU[choice]["ingredients"]
    for item, value in resource_choice.items():
        if resources[item][0] < value:
            print(f"Sorry there is not enough {item}.")
            return False 
        else:
            continue
    return True

def process_coins(choice):
    """
        Function to contabilize the coins and return True if the ammount is enough.
        
        Parameters:
            choice: (str) string that contains the choice
        Returns:
            (bool) True if the ammount is enough False if no
    """
    print('Please, insert the coins!')
    quarters = int(input("How many quarters ?"))
    dimes = int(input("How many dimes?")) 
    nickles = int(input("How many Nickles?"))
    pennies = int(input("How many pennies?"))
    money = (quarters * 0.25)+(dimes * 0.1)+(nickles * 0.05)+(pennies * 0.01)
    
    if money < MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources['money'] =  ("$", (resources['money'][1] + MENU[choice]['cost']))
        print(f"Here is ${round(money - MENU[choice]['cost'],2)} dollars in change.")
        return True

def make_coffee(choice):
    """
        Function to make the coffee and deduce the resources

        Parameters:
            choice: (str) string that contains the choice
            
    """
    coffe_choice = MENU[choice]["ingredients"]
    for item, value in coffe_choice.items():
        resources[item] = (( resources[item][0] - value), resources[item][1])


MACHINE_FUNCTIONS = {"off": turn_off, "report": report}

def run():
    machine_on = True
    while machine_on:
        choice = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

        if choice in MENU:
            if check_resources(choice) and process_coins(choice):
                make_coffee(choice)
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                continue

        elif choice in MACHINE_FUNCTIONS:
            if choice == "off":
                machine_on =  MACHINE_FUNCTIONS['off'](machine_on)
            else:
                print(" ".join(MACHINE_FUNCTIONS['report']()))
        else:
            print('Please, enter a valid option')



if __name__ == "__main__":
    run()