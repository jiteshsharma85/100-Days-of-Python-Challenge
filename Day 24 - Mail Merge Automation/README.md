# Day 24 — Mail Merge

A mail merge script that generates personalised invitation letters for a list of names.

## How it Works

1. Reads a template letter from `Input/Letters/starting_letter.txt`
2. Reads a list of names from `Names/invited_names.txt`
3. Replaces the `[name]` placeholder in the template with each person's name
4. Saves each personalised letter to `Output/ReadyToSend/`

## How to Run

```bash
python main.py
```

The generated letters will appear in `Output/ReadyToSend/` as `letter_for_<Name>.txt`.

## Concepts Practiced

- File reading and writing
- String `.replace()` for templating
- Iterating over lines in a file
- Organising files into input/output folders
