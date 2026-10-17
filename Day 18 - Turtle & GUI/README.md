# Day 18 — Turtle & GUI

Introduction to Python's Turtle graphics library. Covers basic turtle controls through to intermediate generative art sketches.

## Sketches

| File | Description |
|---|---|
| `timmy.py` | Turtle basics + PrettyTable demo |
| `main.py` | Draws progressively larger multi-sided shapes with random colours |
| `random_walk.py` | A turtle that walks randomly in random colours |
| `spirograph -circles.py` | Draws a spirograph by rotating circles through 360° |
| `painting.py` | Recreates a Damien Hirst-style dot painting from extracted image colours |

## How to Run each sketch

```bash
python timmy.py
python main.py
python random_walk.py
python "spirograph -circles.py"
python painting.py
```

## Requirements

```bash
pip install prettytable colorgram.py
```

## Concepts Practiced

- `colormode(255)` for RGB colours
- `randint` for random colour generation
- Nested loops and geometric shapes
- `Screen.exitonclick()`
- Third-party libraries (`prettytable`, `colorgram`)
