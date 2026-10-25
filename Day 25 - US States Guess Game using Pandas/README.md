# Day 25 — Pandas Data Analysis

Two data analysis projects from Day 25 of the 100 Days of Code challenge.

## Projects

### `main.py` — Squirrel Census Analysis
Reads NYC squirrel census data and counts squirrels by primary fur colour, then exports the summary to `count.csv`.

```bash
python main.py
```

**Data file:** `squirl_data.csv`

---

### `US states-project/main.py` — US States Quiz
An interactive geography game — guess all 50 US state names. Correct guesses are plotted on a map. Type `Exit` to stop and save a list of states you missed to `remaining.csv`.

```bash
cd "US states-project"
python main.py
```

**Data files:** `50_states.csv`, `blank_states_img.gif`

## Requirements

```bash
pip install pandas turtle
```

## Concepts Practiced

- Reading and filtering CSV files with pandas
- `DataFrame.to_csv()` for export
- List comprehensions with pandas Series
- Turtle graphics with custom background images
