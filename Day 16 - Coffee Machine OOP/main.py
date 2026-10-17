from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    order_name = input(f"What would you like? ({options}): ").lower().strip()

    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name == "off":
        is_on = False
    else:
        drink = menu.find_drink(order_name)
        if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

