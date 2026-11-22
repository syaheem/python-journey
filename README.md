# 🐍 Python Journey: Zero to Data & AI Engineering

Personal roadmap and progress log tracking my journey from zero programming experience to professional Data Engineering and ML/LLM Engineering.

- **Target:** 72-Week Python & AI Mastery Roadmap
- **Methodology:** Hands-on coding, writing my own code from scratch, tracking everything via Git.

---

## 📁 Repository Structure

```text
├── Week 1/                     # Foundations & Core Python Syntax
│   ├── Hello World.py          # Lesson 1: First program, strings, input()
│   ├── Calculator basic.py     # Lesson 1: Type casting (int), arithmetic
│   ├── Function basic.py       # Lesson 1: Custom functions (def, return)
│   ├── Average.py              # Lesson 1: Function parameters & math
│   ├── Conversion usd to myr.py# Lesson 2: Constants, float formatting (:.2f)
│   ├── Double.py               # Lesson 2: For-loops and range()
│   ├── Age.py                  # Lesson 2: Conditionals (if/elif/else)
│   ├── Lists.py                # Lesson 3: Slicing, indexing, sum(), min(), max()
│   ├── Dicts.py                # Lesson 3: Dictionaries & list-of-dicts
│   ├── Grade.py                # Lesson 3: Multi-subject grade analyzer & stats
│   ├── Number.py               # Lesson 4: Sentinel while-loops ("done" exit)
│   └── ValueError_FUnction.py  # Lesson 4: Reusable input validation functions
│
├── Mini Project/               # Week 1 Capstone Project
│   └── CLI Expense Tracker.py  # Lesson 5: Multi-menu tracker with file I/O & group-by stats
│
├── Week 2/                     # Control Flow, Algorithmic Logic & Loops
│   ├── Lesson 1 - camel_to_snake.py       # String parsing & case conversion
│   └── Lesson 2 - number_guessing_game.py # While-loops, state tracking & random module
│
├── expenses.txt                # Persistent data storage for Expense Tracker
├── .gitignore                  # Git hygiene (ignoring __pycache__)
└── README.md                   # Progress documentation & learning notes
```

---

## 📅 Week 1 Progress Log

### Lesson 1: The Basics & Functions
- **Concepts:** `print()`, `input()`, string concatenation vs f-strings, type casting (`int`), defining functions with `def` and returning values with `return`.
- **Files:** `Hello World.py`, `Calculator basic.py`, `Function basic.py`, `Average.py`.

### Lesson 2: Branching & Loops
- **Concepts:** Decisions with `if` / `elif` / `else`, assignment `=` vs equality `==`, `for` loops with `range()`, and formatted strings `:.2f`.
- **Key Lesson:** The order of conditions in an `elif` ladder matters—more specific conditions must precede general ones.
- **Files:** `Conversion usd to myr.py`, `Double.py`, `Age.py`.

### Lesson 3: Data Structures (Lists & Dictionaries)
- **Concepts:** Lists (indexing from 0, `.append()`, slicing `[1:4]`, `sum()`, `max()`, `min()`, `len()`), dictionaries (key-value pairs, adding keys dynamically on the fly), and nesting dictionaries inside lists (`[ {..}, {..} ]`).
- **Mini-Project:** `Grade.py` (calculates averages, custom comments, best subject, and formatted table).
- **Files:** `Lists.py`, `Dicts.py`, `Grade.py`.

### Lesson 4: Defensive Coding & Error Handling
- **Concepts:** Infinite loops (`while True`), sentinel exits (`"done"` / `"exit"`), exception handling with `try` / `except ValueError` to prevent crashes from bad user input, and modularizing input validation into reusable helper functions.
- **Files:** `Number.py`, `ValueError_FUnction.py`.

### Lesson 5: Capstone Mini-Project (CLI Expense Tracker)
- **Concepts:**
  - Multi-level interactive CLI menu navigation.
  - Persistent File I/O: Writing with `with open(..., "a")` and reading with `with open(..., "r")`.
  - Text parsing and unpacking using `.strip()` and `.split(",")`.
  - Data Aggregation ("Group By"): Using a dictionary tally (`category_totals[category] += num`) to calculate category breakdowns.
  - Overall analytics: `sum()`, `average`, `max()`, `min()`.
  - Exception handling for `FileNotFoundError` and `ValueError`.
  - Initialized Git and synced local repository with GitHub.
- **Files:** `Mini Project/CLI Expense Tracker.py`, `expenses.txt`.

---

## 📅 Week 2 Progress Log: Control Flow & Algorithmic Problem Solving

### Lesson 1: String Parsing & `camelCase` to `snake_case` Converter
- **Concepts:** String immutability, iterating through character streams (`for char in word:`), character case detection (`char.isupper()`), string transformation (`char.lower()`), and standard module entry points (`if __name__ == "__main__":`).
- **Files:** `Week 2/Lesson 1 - camel_to_snake.py`.

### Lesson 2: `while` Loops, State Tracking & Random Number Game
- **Concepts:** Indefinite iteration with `while True`, loop termination with `break`, state tracking across iterations (attempts counter), standard library `random.randint()`.
- **Files:** `Week 2/Lesson 2 - number_guessing_game.py`.

---

## 💡 Key Engineering Lessons Learned
1. **Lists vs. Dictionaries:** Lists are ordered collections indexed by numeric position `[0]`; Dictionaries are key-value mappings accessed by label `["type"]`.
2. **Functions vs. Methods:** Standalone functions (`len()`, `sum()`, `print()`) take data as arguments; Methods (`list.append()`, `str.split()`) belong to specific objects and use the dot `.` operator.
3. **Guard Clauses / Early Returns:** Returning early from a function eliminates the need for deeply nested `else` statements.
4. **Data Aggregation:** Dictionaries are the fundamental data structure for group-by operations before graduating to SQL or Pandas.
5. **Git Workflow:** `git add .` stages all changes without duplicating files, `git commit` records snapshots, and `git push` syncs with GitHub.
