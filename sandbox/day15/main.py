from machine_menu import MENU
from machine_money import MONEY
from machine_resources import *


def calculate_change(money, beverage):
    beverage_cost = MENU[beverage]["cost"]
    if money > beverage_cost:
        change = money - beverage_cost
        print(f"Here is ${change:.2f} dollars in change.")


def update_resources(beverage):
    global machine_money
    for key in resources:
        resources[key] -= MENU[beverage]["ingredients"][key]
    machine_money += MENU[beverage]["cost"]
    get_machine_report()


def is_resources_available(beverage):
    """Receives the beverage that the user wants to order and returns true
     if there is enough resources to produce the beverage, returns false otherwise.
     """
    missing_resources = []
    beverage = MENU[beverage]["ingredients"]
    available_resources = resources
    if beverage["water"] > available_resources["water"]:
        missing_resources.append("water")
    if beverage["coffee"] > available_resources["coffee"]:
        missing_resources.append("coffee")
    if "milk" in beverage and beverage["milk"] > available_resources["milk"]:
        missing_resources.append("milk")

    if len(missing_resources) == 0:
        return True
    else:
        print(f"Sorry there is not enough {', '.join([str(i) for i in missing_resources])}.")
        return False

def get_machine_report():
    """Prints the machine current resources available and current money values."""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${machine_money}')


def get_user_money():
    """Prompts the user to provide the money wants to enter in dimes, quarters,
    nickles, pennies and calculates the final result."""
    money = 0
    print("Please insert coins.")

    for coin in MONEY:
        money += int(input(f"How many {coin}? : ")) * MONEY[coin]
    print(f"You've entered ${money:.2f} dollars.")
    return money


def is_user_money_enough(input_money, beverage):
    if input_money >= MENU[beverage]["cost"]:
        return True
    return False


machine_status = True

while machine_status:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while choice not in ("espresso", "latte", "cappuccino", "off", "report"):
        choice = input("Unknown option. What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
        machine_status = False

    elif choice == 'report':
        get_machine_report()

    else:
        if is_resources_available(choice):

            user_money = get_user_money()

            if is_user_money_enough(user_money, choice):
                calculate_change(user_money, choice)
                update_resources(choice)
                print(f"Here's your {choice} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
