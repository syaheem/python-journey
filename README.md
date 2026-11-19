# Python Journey

Learning Python from scratch, aiming for data engineering and AI.

## Day 1
- hello.py: first program
- functions.py: functions and f-strings
- converter.py: USD to MYR converter# python-journey
- 
## Day 2: Conditionals and Loops

**What I learned**
- Decisions with `if` / `elif` / `else`, and `=` (assign) vs `==` (compare)
- `for` loops with `range()`, and `while` loops
- `break` to exit a loop, and `.lower()` for case-insensitive input

**Files**
- `Number.py`: adds numbers until the user types "done"
- `Grade.py`: grade calculator with validation (grades must be 0 to 100) and a comment based on the average

**Mistakes I learned from**
- `range(1, 11)` stops before 11, so the stop number is never included
- Check for the stop word before converting input to a number
- Divide once after the loop, not inside it, or the average is wrong
- In an `elif` chain, the order of conditions matters

## Day 3: Lists and Dictionaries

**What I learned**
- Lists: indexing from 0, `append`, `remove`, slicing, `sum()`, `max()`, `min()`, `len()`
- Dictionaries: key/value pairs, adding and changing values
- A list of dictionaries, the usual way to store records

**Files**
- `Lists.py`: list operations and slicing practice
- `Dicts.py`: collects student records (name, age, email, phone) in a list of dictionaries
- `Grade.py` (upgraded): stores each subject as a dictionary in a list, then prints every subject, the average, a comment, and the best subject

**Mistakes I learned from**
- Only add a record to the list after its data is validated
- Use a separate variable for each purpose instead of reusing a leftover loop variable
- Use single quotes inside f-strings so the code runs on every Python version

**Next:** reading and writing files, and handling errors with `try` / `except`
