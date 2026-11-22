# 🐍 Python Journey: Zero to Data & AI Engineering

Personal roadmap and progress log tracking my journey from zero programming experience to professional Data Engineering and ML/LLM Engineering.

- **Target:** 72-Week Python & AI Mastery Roadmap
- **Methodology:** Hands-on coding, writing my own code from scratch, tracking everything via Git.

---

## 📁 Repository Structure

```text
├── Week 1/                     # Foundations & Core Python Syntax
│   ├── Hello World.py          # Day 1: First program, strings, input()
│   ├── Calculator basic.py     # Day 1: Type casting (int), arithmetic
│   ├── Function basic.py       # Day 1: Custom functions (def, return)
│   ├── Average.py              # Day 1: Function parameters & math
│   ├── Conversion usd to myr.py# Day 2: Constants, float formatting (:.2f)
│   ├── Double.py               # Day 2: For-loops and range()
│   ├── Age.py                  # Day 2: Conditionals (if/elif/else)
│   ├── Lists.py                # Day 3: Slicing, indexing, sum(), min(), max()
│   ├── Dicts.py                # Day 3: Dictionaries & list-of-dicts
│   ├── Grade.py                # Day 3: Multi-subject grade analyzer & stats
│   ├── Number.py               # Day 4: Sentinel while-loops ("done" exit)
│   └── ValueError_FUnction.py  # Day 4: Reusable input validation functions
│
├── Mini Project/               # Week 1 Capstone Project
│   └── CLI Expense Tracker.py  # Day 5: Multi-menu tracker with file I/O & group-by stats
│
├── expenses.txt                # Persistent data storage for Expense Tracker
├── .gitignore                  # Git hygiene (ignoring __pycache__)
└── README.md                   # Progress documentation & learning notes
```

---

## 📅 Week 1 Progress Log

### Day 1: The Basics & Functions
- **Concepts:** `print()`, `input()`, string concatenation vs f-strings, type casting (`int`), defining functions with `def` and returning values with `return`.
- **Files:** `Hello World.py`, `Calculator basic.py`, `Function basic.py`, `Average.py`.

### Day 2: Branching & Loops
- **Concepts:** Decisions with `if` / `elif` / `else`, assignment `=` vs equality `==`, `for` loops with `range()`, and formatted strings `:.2f`.
- **Key Lesson:** The order of conditions in an `elif` ladder matters—more specific conditions must precede general ones.
- **Files:** `Conversion usd to myr.py`, `Double.py`, `Age.py`.

### Day 3: Data Structures (Lists & Dictionaries)
- **Concepts:** Lists (indexing from 0, `.append()`, slicing `[1:4]`, `sum()`, `max()`, `min()`, `len()`), dictionaries (key-value pairs, adding keys dynamically on the fly), and nesting dictionaries inside lists (`[ {..}, {..} ]`).
- **Mini-Project:** `Grade.py` (calculates averages, custom comments, best subject, and formatted table).
- **Files:** `Lists.py`, `Dicts.py`, `Grade.py`.

### Day 4: Defensive Coding & Error Handling
- **Concepts:** Infinite loops (`while True`), sentinel exits (`"done"` / `"exit"`), exception handling with `try` / `except ValueError` to prevent crashes from bad user input, and modularizing input validation into reusable helper functions.
- **Files:** `Number.py`, `ValueError_FUnction.py`.

### Day 5: Week 1 Capstone Mini-Project (CLI Expense Tracker)
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

## 💡 Key Engineering Lessons Learned in Week 1
1. **Lists vs. Dictionaries:** Lists are ordered collections indexed by numeric position `[0]`; Dictionaries are key-value mappings accessed by label `["type"]`.
2. **Functions vs. Methods:** Standalone functions (`len()`, `sum()`, `print()`) take data as arguments; Methods (`list.append()`, `str.split()`) belong to specific objects and use the dot `.` operator.
3. **Guard Clauses / Early Returns:** Returning early from a function eliminates the need for deeply nested `else` statements.
4. **Data Aggregation:** Dictionaries are the fundamental data structure for group-by operations before graduating to SQL or Pandas.
5. **Git Workflow:** `git add .` stages all changes without duplicating files, `git commit` records snapshots, and `git push` syncs with GitHub.

---

## 🎯 Next Up: Week 2
**Topic:** Conditionals, Loops & Algorithmic Problem Solving.  
**Target:** Solving 10 classic algorithmic practice problems independently to build problem-solving intuition.
