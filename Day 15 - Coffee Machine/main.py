MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    },
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_profit = 0


# Checks if the machine has enough of each ingredient for the order
def is_resource_sufficient(order_ingredients):
    for item, amount in order_ingredients.items():
        if amount > RESOURCES[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Asks user to insert coins and returns the total value
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


# Checks if the money inserted covers the cost and gives change
def is_transaction_ok(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change.")
    return True


# Deducts used ingredients from resources and serves the drink
def make_coffee(drink_name, order_ingredients):
    for item, amount in order_ingredients.items():
        RESOURCES[item] -= amount
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    if user_input == "report":
        print(f"Water: {RESOURCES['water']}ml")
        print(f"Milk: {RESOURCES['milk']}ml")
        print(f"Coffee: {RESOURCES['coffee']}g")
        print(f"Money: ${total_profit}")
    elif user_input == "off":
        is_on = False
    elif user_input in MENU:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_ok(payment, drink["cost"]):
                total_profit += drink["cost"]
                make_coffee(user_input, drink["ingredients"])
    else:
        print(f"'{user_input}' is not on the menu. Please choose espresso, latte, or cappuccino.")
