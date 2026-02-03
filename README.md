# Snake Water Gun Game (Python)

This is a simple **Snake Water Gun** game implemented in Python.

I initially built this project while learning from the *Code With Harry* YouTube tutorial.  
Later, I revisited the same project to understand the logic more deeply and experiment with improvements and variations.

This repository reflects that learning process.

---

## About the Project

The game allows a user to play Snake Water Gun against the computer.

To understand the logic better, I implemented the same game in **two different ways**:

- **Short version** – uses compact conditions and minimal code
- **Long version** – uses clear `if-elif` statements for better readability

Writing both versions helped me compare:
- brevity vs clarity
- how the same problem can be solved in different ways
- why readable code matters when revisiting old projects

---

## What I Learned

While modifying this project beyond the tutorial, I encountered and fixed several issues:

- Placing user input outside loops caused repeated choices
- Generating random computer choices only once led to incorrect gameplay
- Using functions without proper parameters caused scope-related bugs
- Modifying global variables inside functions made the logic harder to reason about
- Missing input validation caused crashes for unexpected inputs

These mistakes helped me understand **program flow, scope, and design decisions** better than simply following a tutorial.

---

## Why This Project Exists

This project is not meant to showcase advanced Python skills.

It exists to:
- document my learning process
- practice improving and refactoring existing code
- build the habit of understanding *why* code works (or breaks)

---

## How to Run

1. Make sure Python is installed
2. Clone the repository
3. Run the Python file using:
   ```bash
   python filename.py


## Notes
I plan to revisit this project again to:
refactor the logic using proper functions
improve structure and data flow
handle input validation more cleanly