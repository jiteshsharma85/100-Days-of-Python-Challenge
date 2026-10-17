class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    # Prints the total profit earned so far
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    # Asks user to insert coins and returns the total amount
    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        self.money_received = 0
        print("Please insert coins.")
        for coin, value in self.COIN_VALUES.items():
            self.money_received += int(input(f"How many {coin}?: ")) * value
        return self.money_received

    # Processes payment and returns True if sufficient, False otherwise
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
