MENU = {
    "expresso": {
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

sum = 0
#TODO: defining the functions

def coffee_maker(coffee_type):
        RESOURCES["water"] = RESOURCES["water"] - MENU[coffee_type]["ingredients"]["water"]
        RESOURCES["milk"] = RESOURCES["milk"] - MENU[coffee_type]["ingredients"]["milk"]
        RESOURCES["coffee"] = RESOURCES["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
        return RESOURCES


def cost_of_coffee(Total_money, coffee_type):
    balance = Total_money - MENU[coffee_type]["cost"]
    return balance

def check_resources():
    if RESOURCES["water"] <= 0:
        print("Please add more water.")
        return False
    elif RESOURCES["milk"] <= 0:
        print("Please add more milk.")
        return False
    elif RESOURCES["coffee"] <= 0:
        print("Please add more coffee bean.")
        return False
    else:
        return True

# TODO: Taking the input from the user and call the relevant function

while check_resources():

    user_input = input("What would you like? (expresso/latte/cappuccino): ")

    # TODO: Check if resources are sufficient

    if user_input == "report":
        print(f"The available resources in the machine are: \n Water: {RESOURCES["water"]} ml, \n Milk: {RESOURCES["milk"]} ml \n Coffee: {RESOURCES['coffee']} g \n Money: ${sum}")
        user_input = input("What would you like? (expresso/latte/cappuccino): ")
    elif user_input == "off":
        break

    # TODO: Process the Coins
    if check_resources():
        print("Please  insert coins.")
    else:
        break

    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    Total_money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    print(f" you added total sum of ${Total_money}")

    balance = cost_of_coffee(Total_money, user_input)



    #TODO: Check if transaction is successful
    if balance > 0:
        print(f"Here is ${balance} in change.")
    elif balance < 0:
        print("Balance is insufficient. Please try again!")
        break


    #TODO: Make coffee and deduct resources.

    if user_input == "expresso":
        print(coffee_maker("expresso"))
        sum += MENU["expresso"]["cost"]
        print("Here's your expresso: ☕️")
        check_resources()
    elif user_input == "latte":
        print(coffee_maker("latte"))
        print("Here's your Latte!: ☕️ ! enjoy")
        sum += MENU["latte"]["cost"]
        check_resources()
    elif user_input == "cappuccino":
        print(coffee_maker("cappuccino"))
        print("Here's your cappuccino: ☕️")
        sum += MENU["cappuccino"]["cost"]
        check_resources()
    else:
        print(f"The available resources in the machine are: \n Water: {RESOURCES["water"]} ml, \n Milk: {RESOURCES["milk"]} ml \n Coffee: {RESOURCES['coffee']} g \n Money: $0")