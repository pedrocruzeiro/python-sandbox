from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while choice not in ("espresso", "latte", "cappuccino", "off", "report"):
        choice = input("Unknown option. What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
        machine_is_on = False

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:

        beverage = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(beverage):

            if money_machine.make_payment(beverage.cost):
                coffee_maker.make_coffee(beverage)
