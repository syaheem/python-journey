# 🐍 Python Mastery Roadmap: The Unlearned Curriculum

> **Learning Philosophy:**  
> - **Self-Paced by Phases, Not Weeks:** Advance only when you can write the code and pass the checkpoint without looking up solutions.  
> - **High-Volume Practice:** Each lesson requires writing 2 to 3 real coding drills before moving to the next.  
> - **Git-Tracked Proof of Work:** Every lesson has a dedicated `.py` file committed to GitHub.

---

## 🧭 Milestone Overview

```
Phase 0: Foundations & First Capstone  [COMPLETED]
├── Lesson 1–5: Syntax, Functions, Lists/Dicts, Files, CLI Expense Tracker
└── Status: 100% Pushed to GitHub

Phase 1: Flow Control, Algorithmic Logic & Defensive Input [CURRENT]
Phase 2: Advanced Data Structures, Mutability & Collections
Phase 3: File Systems, Structured Formats & Databases (CSV, JSON, SQLite)
Phase 4: Object-Oriented Programming (OOP) & System Design
Phase 5: Pythonic Idioms, Functional Patterns & Performance (Decorators, Generators)
Phase 6: Networking, Web APIs & Asynchronous Programming (FastAPI, asyncio)
Phase 7: Professional Engineering: Testing, Packaging & CI/CD (pytest, Docker)
Phase 8: Data & AI Engineering Specialization (Pandas, Scikit-Learn, LLMs/RAG)
```

---

## 📍 Phase 1: Flow Control, Algorithmic Logic & Defensive Input
*Focus: Master loops, conditional branching, string algorithms, and rock-solid error recovery.*

### Lesson 1: String Parsing & Case Conversion [COMPLETED]
- **Core Theory:** String immutability, iterating through character streams, uppercase boundary detection.
- **Syntax Mastered:** `for char in word:`, `char.isupper()`, `char.lower()`, `if __name__ == "__main__":`.
- **File:** `Week 2/Lesson 1 - camel_to_snake.py`

### Lesson 2: Indefinite Iteration & State Tracking (`while` loops) [UP NEXT]
- **Core Theory:** When repetition length is unknown; sentinel values; state accumulation across loop cycles; early termination with `break`; skipping iterations with `continue`.
- **Syntax / Modules:** `while condition:`, `break`, `continue`, `import random`, `random.randint(a, b)`.
- **Hands-On Drills to Code:**
  1. *Drill 2.1 — Number Guessing Engine:* Computer picks random 1–100; user guesses; gives "Too High" / "Too Low"; tracks and displays attempt count.
  2. *Drill 2.2 — Reverse Guessing:* User picks a number in mind; computer guesses using binary search logic (asking user "higher/lower/correct") to guess in under 7 tries.
  3. *Drill 2.3 — Password Retry Guard:* User has max 3 attempts to enter the correct secret password; triggers lockout message if failed.
- **Checkpoint:** You understand the difference between sentinel loops (`while True: break`) and counter loops.

### Lesson 3: Advanced String Algorithms & Text Manipulation
- **Core Theory:** Slice stepping `[start:stop:step]`, substring search, string transformation without regex.
- **Syntax / Methods:** `str.replace()`, `str.join()`, `str.find()`, `str.count()`, `str.isalpha()`, `[::-1]`.
- **Hands-On Drills to Code:**
  1. *Drill 3.1 — Palindrome & Anagram Verifier:* Check if a phrase reads the same backward (ignoring punctuation/spaces), and if two words are anagrams.
  2. *Drill 3.2 — Vowel Stripper & Text Obfuscator:* Replace sensitive keywords with asterisks and strip all vowels from user text.
  3. *Drill 3.3 — Title Case Engine (from scratch):* Implement your own version of `.title()` without using the built-in method.
- **Checkpoint:** Able to reverse, filter, and rebuild strings purely with loops and slicing.

### Lesson 4: Nested Loops, Coordinate Systems & Pattern Logic
- **Core Theory:** Two-dimensional traversal (`row` and `column`), nested iteration complexity $O(n^2)$, grid representation.
- **Syntax / Techniques:** Nested `for row in ...: for col in ...:`, `print(..., end="")`.
- **Hands-On Drills to Code:**
  1. *Drill 4.1 — Dynamic Grid / Matrix Printer:* Print an $N \times N$ chessboard pattern using `X` and `O`.
  2. *Drill 4.2 — Multiplication Table Matrix:* Generate a formatted, aligned $10 \times 10$ multiplication table.
  3. *Drill 4.3 — Coordinate Map Distance Finder:* Generate a grid with two random points $(x_1, y_1)$ and $(x_2, y_2)$ and compute Manhattan distance.
- **Checkpoint:** Able to manipulate 2D coordinate spaces and control row/column output formatting.

### Lesson 5: Bulletproof Input Validation & Custom Exceptions
- **Core Theory:** Anticipating bad input; handling multiple error types; difference between catching errors and preventing them; the `else` and `finally` clauses.
- **Syntax / Keywords:** `try`, `except (ValueError, TypeError)`, `else`, `finally`, `raise ValueError("custom message")`.
- **Hands-On Drills to Code:**
  1. *Drill 5.1 — Multi-Type Form Validator:* Ask for Name (only letters), Age (int 1–120), Salary (float > 0) with graceful per-field re-prompting.
  2. *Drill 5.2 — Safe Division Calculator:* Handles division by zero, missing inputs, and non-numeric characters without crashing.
  3. *Drill 5.3 — Custom Exception Boundary:* Write a function that explicitly raises a `ValueError` if an input fails security checks.
- **Checkpoint:** A user typing random symbols or pressing enter cannot cause an unhandled crash.

### 🏆 Phase 1 Capstone Project: Terminal Wordle / Hangman Game Engine
- Full terminal game featuring random secret word selection, input validation (5-letter check, alphabetical only), colored/formatted letter feedback (Green/Yellow/Gray or `[+]`, `[?]`, `[-]`), maximum 6 attempts, and persistent win/loss score recording.

---

## 📍 Phase 2: Advanced Data Structures, Mutability & Collections
*Focus: Internal memory models, shallow vs deep copying, list/dict comprehensions, and specialized collections.*

### Lesson 6: Deep Dive into Lists, Mutability & References
- **Core Theory:** Pass-by-object-reference; mutable vs immutable types; shallow copies vs deep copies; in-place mutations vs new allocations.
- **Syntax / Methods:** `id()`, `list.copy()`, `copy.deepcopy()`, `.extend()`, `.insert()`, `.pop()`, `.remove()`, `sorted(..., key=...)`.
- **Hands-On Drills to Code:**
  1. *Drill 6.1 — Pointer & Mutation Visualizer:* Demonstrate how modifying list `b = a` affects `a`, and how to prevent it with slicing / `.copy()`.
  2. *Drill 6.2 — Custom Custom-Key Sorter:* Sort a list of tuples `(name, age, score)` by score descending, then by age ascending.
  3. *Drill 6.3 — In-Place Array Filter:* Remove all odd numbers from a list in-place without creating a new list.

### Lesson 7: Comprehensions (List, Dict, Set) & Generator Expressions
- **Core Theory:** Writing declarative, expressive, and optimized data transformations in a single line.
- **Syntax:** `[x for x in list if condition]`, `{k: v for k, v in pairs}`, `{x for x in list}`, `(x for x in list)`.
- **Hands-On Drills to Code:**
  1. *Drill 7.1 — Text Token Cleaner:* Given a messy paragraph, use comprehensions to produce lowercase, punctuation-free word tokens of length $> 3$.
  2. *Drill 7.2 — Dictionary Inverter:* Take `{user_id: username}` and invert it to `{username: user_id}`, handling collisions.
  3. *Drill 7.3 — Flattening a 2D Matrix:* Flatten a $3 \times 3$ nested list into a 1D list using a single nested list comprehension.

### Lesson 8: Sets, Tuples & Memory Immutability
- **Core Theory:** Hash tables under the hood; why set lookups are $O(1)$ while list lookups are $O(n)$; tuple unpacking; set algebra.
- **Syntax / Operators:** `set.union() |`, `intersection &`, `difference -`, `symmetric_difference ^`, tuple packing/unpacking `a, *b, c = values`.
- **Hands-On Drills to Code:**
  1. *Drill 8.1 — Log File IP Deduplicator:* Compare two sets of server visitor IPs to find new visitors, returning visitors, and lost visitors.
  2. *Drill 8.2 — Benchmark Duel (List vs Set):* Time how long it takes to search for an item in a list of 1,000,000 items vs a set of 1,000,000 items using `time.perf_counter()`.
  3. *Drill 8.3 — Advanced Tuple Unpacking:* Process a stream of sensor logs `(timestamp, sensor_id, *readings, status)` dynamically.

### Lesson 9: Advanced Dictionaries & `collections` Module
- **Core Theory:** Avoiding `KeyError`; performance of counting and grouping; standard library collection power tools.
- **Syntax / Classes:** `dict.get()`, `dict.setdefault()`, `collections.defaultdict`, `collections.Counter`, `collections.deque`.
- **Hands-On Drills to Code:**
  1. *Drill 9.1 — Word Frequency Analyzer:* Use `Counter` to find the top 5 most common words in a text passage.
  2. *Drill 9.2 — Multi-Value Grouping Engine:* Group a list of transaction records by customer ID using `defaultdict(list)`.
  3. *Drill 9.3 — Fixed-Size Undo Buffer:* Use `deque(maxlen=5)` to create an undo history that automatically discards oldest actions.

### 🏆 Phase 2 Capstone Project: In-Memory CRM & Analytical Query Engine
- Build an in-memory database system holding 100+ simulated customer records (nested dictionaries).
- Support dynamic querying: filtering by multiple attributes (`status="active"`, `spend > 500`), grouping by region, aggregating metrics (min/max/median), and generating structured summary reports.

---

## 📍 Phase 3: File Systems, Structured Formats & Databases
*Focus: Never lose data. Transition from raw text files to industry-standard CSV, JSON, and SQL databases.*

### Lesson 10: Robust File & Path Manipulation with `pathlib`
- **Core Theory:** Cross-platform path safety (Windows `\` vs Linux `/`); directory scanning; absolute vs relative paths.
- **Syntax / Classes:** `from pathlib import Path`, `Path.cwd()`, `.glob()`, `.rglob()`, `.exists()`, `.mkdir()`, `.read_text()`.
- **Hands-On Drills to Code:**
  1. *Drill 10.1 — Automated File Sorter:* Scan a folder and sort files into subfolders by extension (`.pdf`, `.py`, `.png`, `.txt`).
  2. *Drill 10.2 — Codebase Line Counter:* Recursively find all `.py` files in a directory and count total lines of code, ignoring comments.
  3. *Drill 10.3 — Safe File Backup Tool:* Copy files with timestamped backup extensions before modification.

### Lesson 11: Production-Grade CSV Processing
- **Core Theory:** Delimiters, escaping, headers, handling missing columns.
- **Syntax / Classes:** `import csv`, `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter`.
- **Hands-On Drills to Code:**
  1. *Drill 11.1 — Sales Log Cleaner:* Read a dirty CSV with inconsistent dates and missing values, sanitize rows, and write a cleaned CSV.
  2. *Drill 11.2 — CSV Merger & Re-indexer:* Combine two separate CSV files (e.g., users and orders) on a shared `user_id`.

### Lesson 12: JSON Serialization & Configuration Management
- **Core Theory:** Data interchange format; converting Python objects to JSON strings and vice-versa; handling non-serializable objects.
- **Syntax / Methods:** `import json`, `json.load()`, `json.loads()`, `json.dump(..., indent=4)`, `json.dumps()`, custom serializers.
- **Hands-On Drills to Code:**
  1. *Drill 12.1 — App Config Manager:* Save and load user preferences (theme, window size, API keys) in a JSON configuration file.
  2. *Drill 12.2 — Nested JSON Parser:* Parse a complex multi-level JSON API mock response and extract specific deeply nested keys.

### Lesson 13: Relational Data Persistence with SQLite (`sqlite3`)
- **Core Theory:** Tables, schemas, primary keys, foreign keys, SQL injection prevention via parameterized queries, transactions (`commit` & `rollback`).
- **Syntax / Methods:** `import sqlite3`, `cursor.execute("SELECT ... WHERE id = ?", (val,))`, `cursor.fetchall()`, `conn.commit()`.
- **Hands-On Drills to Code:**
  1. *Drill 13.1 — User Registration SQLite DB:* Create `users` table, insert records safely with parameter substitution, prevent duplicate usernames.
  2. *Drill 13.2 — Relational Orders Ledger:* Build two tables (`customers` and `orders`), insert relationships, and query using an `INNER JOIN`.

### 🏆 Phase 3 Capstone Project: Personal Finance & Asset Portfolio Database
- Replace raw text storage with a structured SQLite database.
- Features: Add incomes/expenses with categories, dates, and accounts; perform SQL aggregations (`SUM`, `AVG`, `GROUP BY category`); export monthly reports to CSV and JSON formats.

---

## 📍 Phase 4: Object-Oriented Programming (OOP) & System Design
*Focus: Move from procedural scripts to modular, scalable, enterprise-grade software design.*

### Lesson 14: Classes, Instances & State Encapsulation
- **Core Theory:** Why OOP matters; bundling data (attributes) with behaviors (methods); instance variables vs class variables.
- **Syntax / Keywords:** `class`, `__init__`, `self`, `ClassName.class_var`.
- **Hands-On Drills to Code:**
  1. *Drill 14.1 — Bank Account Entity:* Attributes for account number and balance; methods for `deposit()`, `withdraw()` (with overdraft guard), and `get_statement()`.
  2. *Drill 14.2 — Inventory Item Tracker:* Class variable tracking total inventory count across all instantiated items.

### Lesson 15: Property Decorators, Getters & Setters
- **Core Theory:** Data validation during attribute assignment; preserving public interfaces while adding backend logic; private convention `_protected`.
- **Syntax:** `@property`, `@attribute.setter`, `@attribute.deleter`.
- **Hands-On Drills to Code:**
  1. *Drill 15.1 — Temperature Converter Class:* Store temperature internally in Kelvin; provide properties for `celsius` and `fahrenheit` with validation (rejecting below absolute zero).
  2. *Drill 15.2 — Employee Salary Entity:* Validate that salary cannot be set to a negative number or reduced by more than 20% without manager override.

### Lesson 16: Inheritance, Polymorphism & Composition
- **Core Theory:** Code reuse without duplication; "is-a" (inheritance) vs "has-a" (composition); overriding methods; calling parent methods with `super()`.
- **Syntax:** `class Child(Parent):`, `super().__init__()`, method overriding.
- **Hands-On Drills to Code:**
  1. *Drill 16.1 — Payment Gateway System:* Base class `PaymentProcessor` with subclass implementations `CreditCardProcessor`, `PayPalProcessor`, `CryptoProcessor` sharing uniform `.pay(amount)` interface.
  2. *Drill 16.2 — Car Engine Composition:* Create an `Engine` class and a `Transmission` class, then compose them into a `Car` class instead of using inheritance.

### Lesson 17: Python Dunder (Magic) Methods
- **Core Theory:** Operator overloading; making custom objects behave like native Python types (printable, iterable, comparable).
- **Syntax / Methods:** `__str__`, `__repr__`, `__len__`, `__eq__`, `__lt__`, `__add__`, `__getitem__`.
- **Hands-On Drills to Code:**
  1. *Drill 17.1 — Custom Vector / Coordinate Math:* Class `Vector(x, y)` supporting addition `v1 + v2`, multiplication `v * 3`, equality `v1 == v2`, and string representation `(x, y)`.
  2. *Drill 17.2 — Custom Deck of Cards:* Class `Deck` supporting `len(deck)` and bracket indexing `deck[0]` through `__len__` and `__getitem__`.

### Lesson 18: Modern Data Modeling with `@dataclass`
- **Core Theory:** Eliminating boilerplate `__init__` and `__repr__`; type-hinted fields; immutable value objects (`frozen=True`).
- **Syntax:** `from dataclasses import dataclass, field`.
- **Hands-On Drills to Code:**
  1. *Drill 18.1 — Immutable Config Object:* Create a frozen dataclass representing database credentials.
  2. *Drill 18.2 — Product Catalog Entity:* Dataclass with default factory lists, auto-calculated total price, and custom ordering.

### 🏆 Phase 4 Capstone Project: Object-Oriented RPG Battle Simulator or E-Commerce Engine
- Design a modular simulation with `Player`, `Enemy`, `Weapon`, and `Inventory` classes.
- Use polymorphism for different attack types, properties for health bounds, dunder methods for weapon comparisons, and dataclasses for game items.

---

## 📍 Phase 5: Pythonic Idioms, Functional Patterns & Performance
*Focus: Master the features that make senior Python developers 10x faster and memory-efficient.*

### Lesson 19: Dynamic Arguments (`*args`, `**kwargs`) & Unpacking
- **Core Theory:** Flexible function signatures, forwarding arguments, parameter dictionary unpacking.
- **Syntax:** `def func(*args, **kwargs):`, `*list_var`, `**dict_var`.
- **Hands-On Drills to Code:**
  1. *Drill 19.1 — Universal Logger Wrapper:* Function that accepts any arbitrary message, timestamp, and metadata dictionary and formats them cleanly.
  2. *Drill 19.2 — Flexible Query Builder:* Function that takes table name and arbitrary `**filters` to generate SQL query strings dynamically.

### Lesson 20: Functional Primitives & Lambda Functions
- **Core Theory:** Functions as first-class citizens; anonymous functions; functional pipelines.
- **Syntax / Built-ins:** `lambda x: ...`, `map()`, `filter()`, `sorted(..., key=...)`, `zip()`, `enumerate()`.
- **Hands-On Drills to Code:**
  1. *Drill 20.1 — Data Pipeline Chain:* Given a list of user dictionaries, chain `filter` to find active users, `map` to extract emails, and `sorted` to alphabetize.
  2. *Drill 20.2 — Parallel Iterator:* Use `zip()` to combine timestamps, temperatures, and humidity readings into unified record logs.

### Lesson 21: Decorators & Function Closures
- **Core Theory:** Higher-order functions; wrapping execution; metadata preservation with `functools.wraps`.
- **Syntax:** `@decorator`, `def outer(fn): def inner(*args, **kwargs): ... return inner`.
- **Hands-On Drills to Code:**
  1. *Drill 21.1 — `@timer` Execution Decorator:* Measures and prints exact runtime of any function down to milliseconds.
  2. *Drill 21.2 — `@retry(max_attempts=3)` Decorator:* Automatically retries an unstable function (like a network request) if it raises an exception.
  3. *Drill 21.3 — `@validate_types` Decorator:* Checks that arguments passed to a function match expected types before execution.

### Lesson 22: Generators, `yield` & Memory Optimization
- **Core Theory:** Lazy evaluation; stream processing vs in-memory loading; handling gigabyte-sized files without RAM spikes.
- **Syntax:** `yield`, `yield from`, generator expressions `(x for x in ...)`
- **Hands-On Drills to Code:**
  1. *Drill 22.1 — Infinite Fibonacci Generator:* Generate Fibonacci numbers on-the-fly without storing them in a list.
  2. *Drill 22.2 — Large File Chunk Streamer:* Read a massive text file line-by-line using a generator function, filtering matching lines with near-zero memory footprint.

### Lesson 23: Custom Context Managers (`with` blocks)
- **Core Theory:** Resource acquisition is initialization (RAII); deterministic cleanup of files, network sockets, and database connections.
- **Syntax:** `__enter__` and `__exit__`, or `from contextlib import contextmanager`.
- **Hands-On Drills to Code:**
  1. *Drill 23.1 — Database Transaction Context Manager:* Automatically commits on success or rolls back changes if an exception occurs.
  2. *Drill 23.2 — Temporary File Directory Sandbox:* Creates a scratch folder upon entering and guarantees complete deletion upon exit.

### 🏆 Phase 5 Capstone Project: High-Performance Data Streaming & Monitoring Engine
- A production utility that streams a simulated high-volume log stream, uses generators to parse logs lazily, applies decorators for telemetry and timing, and saves filtered results through custom context managers.

---

## 📍 Phase 6: Networking, Web APIs & Asynchronous Programming
*Focus: Connect Python to the world — consuming external services, building backend APIs, and handling concurrency.*

### Lesson 24: Consuming REST APIs with `requests` / `httpx`
- **Core Theory:** Client-server model, HTTP verbs (GET, POST, PUT, DELETE), status codes (200, 201, 400, 401, 404, 500), authentication headers, query parameters.
- **Syntax / Libraries:** `import requests`, `response.json()`, `response.status_code`, `requests.Session()`.
- **Hands-On Drills to Code:**
  1. *Drill 24.1 — Live Weather & Currency CLI:* Fetch live weather for any city and convert foreign exchange rates using free public APIs.
  2. *Drill 24.2 — GitHub Repository Inspector:* Query GitHub's REST API with authentication token to list user repositories, stars, and open issues.

### Lesson 25: Asynchronous Concurrency with `asyncio`
- **Core Theory:** I/O-bound vs CPU-bound tasks; the event loop; cooperative multitasking vs threading.
- **Syntax:** `async def`, `await`, `asyncio.run()`, `asyncio.gather()`.
- **Hands-On Drills to Code:**
  1. *Drill 25.1 — Async URL Pinger:* Ping 10 different website URLs concurrently, printing status codes in seconds instead of minutes.
  2. *Drill 25.2 — Async Rate-Limited Worker:* Worker queue that processes tasks concurrently while respecting an API rate limit.

### Lesson 26: Building High-Performance REST APIs with FastAPI
- **Core Theory:** Modern Python backend engineering; automatic data validation with Pydantic; OpenAPI / Swagger documentation.
- **Syntax / Libraries:** `from fastapi import FastAPI`, `@app.get()`, `@app.post()`, `pydantic.BaseModel`.
- **Hands-On Drills to Code:**
  1. *Drill 26.1 — Note-Taking Microservice:* Full CRUD endpoints (`/notes`, `/notes/{id}`) with JSON validation and SQLite storage.
  2. *Drill 26.2 — Data Calculation API:* Endpoint that takes a JSON payload of numbers and returns statistical breakdowns (mean, median, standard deviation).

### Lesson 27: Web Scraping & Structured HTML Parsing
- **Core Theory:** Inspecting DOM trees; ethical scraping (`robots.txt`, rate limits); CSS selectors and XPath.
- **Syntax / Libraries:** `from bs4 import BeautifulSoup`, `soup.find_all()`, `soup.select()`.
- **Hands-On Drills to Code:**
  1. *Drill 27.1 — E-Commerce Price Monitor:* Scrape a product page, extract title and price, and alert if the price falls below a threshold.
  2. *Drill 27.2 — Table-to-CSV Extractor:* Scrape a Wikipedia table and convert it directly into a clean CSV file.

### 🏆 Phase 6 Capstone Project: Live Market Intelligence Aggregator & API
- An automated service that scrapes or fetches market data from multiple endpoints concurrently using `asyncio`, stores aggregated records in SQLite, and serves them via a custom FastAPI backend.

---

## 📍 Phase 7: Professional Engineering: Testing, Tooling & CI/CD
*Focus: Writing code that companies can trust in production. No more manual testing.*

### Lesson 28: Automated Unit Testing with `pytest`
- **Core Theory:** Why manual print tests fail; test discovery; assertions; test suites.
- **Syntax:** `def test_feature(): assert result == expected`, `pytest.raises(ValueError)`.
- **Hands-On Drills to Code:**
  1. *Drill 28.1 — Math & String Unit Tests:* Write comprehensive unit tests for your Week 2 camelCase converter and calculator functions.
  2. *Drill 28.2 — Negative & Edge Case Tests:* Test boundary conditions (empty strings, zero division, negative inputs, huge numbers).

### Lesson 29: Test Fixtures, Parametrization & Mocking
- **Core Theory:** DRY test suites; isolating dependencies; mocking network requests and databases with `unittest.mock`.
- **Syntax:** `@pytest.fixture`, `@pytest.mark.parametrize`, `from unittest.mock import patch, MagicMock`.
- **Hands-On Drills to Code:**
  1. *Drill 29.1 — Parametrized Validator Tests:* Run 15 different test cases against a single validation function in 3 lines of code.
  2. *Drill 29.2 — Mocked API Client Test:* Test an API consumer function without making real network calls by mocking `requests.get`.

### Lesson 30: Professional Project Architecture & Environment Isolation
- **Core Theory:** Virtual environments; dependency lockfiles; separating source code from tests; environment variable isolation.
- **Tools:** `venv`, `pip freeze > requirements.txt`, `python-dotenv`, `.env`, standard folder structure (`src/`, `tests/`).
- **Hands-On Drills to Code:**
  1. *Drill 30.1 — Clean Architecture Refactor:* Restructure an existing project into standard enterprise layout with `src/app/`, `tests/`, and `README.md`.
  2. *Drill 30.2 — Secrets Manager:* Load database URLs and API keys securely from `.env` using `os.getenv()`.

### Lesson 31: GitHub Actions CI & Docker Basics
- **Core Theory:** Continuous Integration (CI); containerization; ensuring code runs on any machine identically.
- **Tools:** `.github/workflows/tests.yml`, `Dockerfile`.
- **Hands-On Drills to Code:**
  1. *Drill 31.1 — GitHub Actions CI Pipeline:* Create a workflow that automatically runs `pytest` on every push to GitHub.
  2. *Drill 31.2 — Containerize a Python App:* Write a minimal `Dockerfile` to containerize your FastAPI application.

### 🏆 Phase 7 Capstone Project: Production-Ready, Tested & Containerized Service
- Take your best previous project, add a complete `pytest` test suite with $>85\%$ coverage, set up GitHub Actions CI to auto-test on push, and provide a `Dockerfile` for one-command deployment.

---

## 📍 Phase 8: Data & AI Engineering Specialization
*Focus: Vectorized math, data transformations with Pandas, machine learning modeling, and modern Generative AI / RAG.*

### Lesson 32: Vectorized Computing with NumPy
- **Core Theory:** Why Python loops are slow for math; CPU cache and contiguous C arrays; array broadcasting; vectorized operations.
- **Syntax / Libraries:** `import numpy as np`, `np.array()`, `arr.shape`, `arr.mean()`, boolean masking `arr[arr > 5]`.
- **Hands-On Drills to Code:**
  1. *Drill 32.1 — Array Benchmark Challenge:* Multiply 1,000,000 numbers using a standard Python `for` loop vs `np.ndarray` and compare speed.
  2. *Drill 32.2 — Matrix Operations & Normalization:* Normalize an $M \times N$ matrix using z-score normalization without any loops.

### Lesson 33: Data Wrangling & Analytics with Pandas
- **Core Theory:** Series and DataFrames; handling missing data (`NaN`); group-by aggregations; merging and joining tables.
- **Syntax / Libraries:** `import pandas as pd`, `df.read_csv()`, `df.groupby()`, `df.dropna()`, `df.fillna()`, `df.merge()`.
- **Hands-On Drills to Code:**
  1. *Drill 33.1 — Customer Churn Dataset Cleaning:* Load a raw CSV dataset, remove duplicate records, impute missing numbers, and standardize column types.
  2. *Drill 33.2 — Sales Cohort Analysis:* Group sales by month and product category to calculate revenue growth and top-performing segments.

### Lesson 34: Exploratory Data Analysis & Visualization
- **Core Theory:** Visualizing distributions, correlations, outliers, and trends.
- **Libraries:** `import matplotlib.pyplot as plt`, `import seaborn as sns`.
- **Hands-On Drills to Code:**
  1. *Drill 34.1 — Financial Trend Chart:* Plot moving averages, volume bars, and price fluctuations for financial records.
  2. *Drill 34.2 — Correlation Heatmap:* Generate a correlation heatmap identifying relationships between features in a dataset.

### Lesson 35: Machine Learning Fundamentals with Scikit-Learn
- **Core Theory:** Supervised vs unsupervised learning; feature scaling; train/test split; evaluation metrics (MSE, $R^2$, Accuracy, Precision, Recall, F1).
- **Libraries:** `from sklearn.model_selection import train_test_split`, `LinearRegression`, `RandomForestClassifier`.
- **Hands-On Drills to Code:**
  1. *Drill 35.1 — Predictive Pricing Model:* Train a regression model to predict housing or vehicle prices based on features.
  2. *Drill 35.2 — Classification Classifier:* Train a classifier to predict customer churn or spam email detection, evaluating with confusion matrix.

### Lesson 36: Generative AI, Embeddings & LLM Integration
- **Core Theory:** Transformer tokenization, temperature, system prompts, vector embeddings, cosine similarity.
- **Libraries:** `google-genai` / `openai`, vector embedding generation.
- **Hands-On Drills to Code:**
  1. *Drill 36.1 — Structured JSON Extractor via LLM:* Send raw, messy customer support emails to an LLM and force it to return strict structured JSON (sentiment, urgency, category).
  2. *Drill 36.2 — Semantic Search Engine:* Generate embeddings for 20 documents and compute cosine similarity to search documents by meaning rather than exact keywords.

### Lesson 37: Retrieval-Augmented Generation (RAG) Architecture
- **Core Theory:** Overcoming LLM knowledge limits; document chunking; vector databases (ChromaDB / FAISS); contextual prompt injection.
- **Hands-On Drills to Code:**
  1. *Drill 37.1 — Custom Document Q&A Bot:* Load your own text notes, chunk them, store in a vector database, and build an assistant that answers questions referencing only your notes.

### 🏆 Phase 8 Final Capstone Project: Autonomous AI Research & Data Analysis Agent
- An end-to-end AI application:
  1. Pulls data from an API or dataset.
  2. Cleans and computes statistical summaries using Pandas & NumPy.
  3. Sends summaries to an LLM to generate an automated executive briefing report.
  4. Saves results in a database and provides a web API to query the intelligence dashboard.

---

## 🛠️ The Standard Daily Lesson Workflow
Whenever you sit down to code:
1. Open your workspace and create `Phase X/Lesson Y - <topic>.py`.
2. Code the drills and run them locally: `python "Phase X/Lesson Y - <topic>.py"`.
3. Check off the drill criteria.
4. Commit and push:
   ```powershell
   git add .
   git commit -m "feat(phaseX): complete Lesson Y drills"
   git push origin main
   ```
