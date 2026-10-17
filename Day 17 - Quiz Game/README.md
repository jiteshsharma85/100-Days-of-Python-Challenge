# Quiz Game (OOP)

A command-line True/False quiz game built with Python using Object-Oriented Programming.

## Features

- 10 General Knowledge True/False questions
- Live score feedback after each answer
- Type `quit` at any time to exit early
- Final score displayed at the end

## How to Run

```bash
python main.py
```

## Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Entry point — builds question bank and runs quiz |
| `data.py` | Raw question data (list of dicts) |
| `question_model.py` | `Question` class (text + answer) |
| `quiz_brain.py` | `QuizBrain` class — question flow and scoring |

## Concepts Practiced

- Object-Oriented Programming (classes, encapsulation)
- List comprehensions
- Working with external data structures
