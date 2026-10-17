# Snake Game

A classic Snake game built with Python's Turtle graphics library. Eat food to grow, avoid the walls and your own tail. High score is saved between sessions.

## Controls

| Key | Action |
|---|---|
| `↑` | Move up |
| `↓` | Move down |
| `←` | Move left |
| `→` | Move right |

## How to Run

```bash
python main.py
```

> The high score is saved in `data.txt` — do not delete it or the high score will reset.

## Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Game loop, collision detection |
| `snake.py` | Snake creation, movement, and growth |
| `food.py` | Food placement |
| `Scoreboard.py` | Score display and high score persistence |
| `data.txt` | Persistent high score storage |

## Concepts Practiced

- Object-Oriented Programming with `Turtle` subclasses
- File I/O for persistent high score
- Collision detection (food, walls, self)
- Game loop with `tracer(0)` / `screen.update()`
