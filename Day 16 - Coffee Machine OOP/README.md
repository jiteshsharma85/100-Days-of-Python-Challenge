# Coffee Machine (OOP)

A command-line coffee machine simulator built with Python using Object-Oriented Programming principles.

## Features

- Order espresso, latte, or cappuccino
- Coin-based payment system (quarters, dimes, nickels, pennies)
- Tracks machine resources (water, milk, coffee)
- Persists total profit across orders
- Type `report` to view current resources and earnings
- Type `off` to shut down the machine

## How to Run

```bash
python main.py
```

## Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Entry point — main game loop |
| `menu.py` | `MenuItem` and `Menu` classes |
| `coffee_maker.py` | Resource tracking and coffee brewing |
| `money_machine.py` | Coin processing and payment validation |

## Concepts Practiced

- Object-Oriented Programming (classes, methods, encapsulation)
- Class constants
- Separation of concerns across multiple modules
