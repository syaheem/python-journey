# 🐍 Python Mastery Roadmap — Zero to Professional

> **Philosophy:** Every lesson builds on the last. You don't move forward until you can write the current lesson from memory. Speed doesn't matter — depth does.

---

## 🗺️ Overview

| Phase | Focus | Outcome |
|:---|:---|:---|
| **Phase 1** (Weeks 1–4) | Core Python | You can write any logic from scratch |
| **Phase 2** (Weeks 5–8) | Intermediate Python | You write clean, reusable, professional code |
| **Phase 3** (Weeks 9–14) | Applied Python | You build real tools and APIs |
| **Phase 4** (Weeks 15–20) | Data & Automation | You work with data like a data engineer |
| **Phase 5** (Weeks 21–28) | AI & ML Engineering | You build, fine-tune, and deploy AI models |

---

## ⚡ Phase 1: Core Python (Weeks 1–4)
> **Goal:** Build an unshakeable foundation. After this phase you can solve any problem with basic Python — no Googling the fundamentals.

### Week 1 — Syntax, Variables & Functions
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | Variables, data types (`int`, `float`, `str`, `bool`) | Personal info printer |
| 2 | `input()`, type casting, f-strings | Unit converter (km ↔ miles, °C ↔ °F) |
| 3 | Arithmetic, operator precedence, `round()` | Tip calculator |
| 4 | `def` functions, `return`, parameters | Math toolbox (`add`, `subtract`, `area`) |
| 5 | Scope: local vs global variables | Inventory counter |
| **Mini Project** | — | **CLI Receipt Printer** (items, quantities, subtotal, tax, total) |

### Week 2 — Control Flow & Loops
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | `if / elif / else`, comparison operators | Grade classifier |
| 2 | `while True` + `break` + `continue` | Number guessing game |
| 3 | `for` loops + `range()` | Multiplication table generator |
| 4 | Nested loops & loop control | Pattern printer (triangles, pyramids) |
| 5 | String methods (`upper`, `lower`, `strip`, `split`, `replace`) | camelCase → snake_case converter |
| **Mini Project** | — | **CLI Rock Paper Scissors** (best of 5, score tracker) |

### Week 3 — Data Structures
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | Lists: indexing, slicing, `append`, `pop`, `sort` | Leaderboard manager |
| 2 | List comprehensions | Filter & transform pipelines |
| 3 | Dictionaries: CRUD, iteration, nested dicts | Student grade book |
| 4 | Tuples & sets (when and why to use them) | Unique word counter |
| 5 | Combining structures (list of dicts, dict of lists) | Contact book CLI |
| **Mini Project** | — | **Inventory Management System** (add/remove/search/restock) |

### Week 4 — Error Handling & File I/O
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | `try / except / finally` — catching specific errors | Safe calculator |
| 2 | Raising your own exceptions with `raise` | Input validation library |
| 3 | Reading & writing files (`open`, `with`, `r`, `w`, `a`) | Note-taking CLI |
| 4 | Working with CSV files using `csv` module | Sales report reader |
| 5 | Working with JSON files using `json` module | Settings/config file manager |
| **Mini Project** | — | **Personal Journal App** (entries saved/loaded from JSON) |

---

## 🔧 Phase 2: Intermediate Python (Weeks 5–8)
> **Goal:** Write code that other developers respect — modular, readable, and reusable.

### Week 5 — Functions, Deeper
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | `*args` and `**kwargs` | Flexible logging function |
| 2 | Lambda functions & when to use them | Sorting complex lists |
| 3 | `map()`, `filter()`, `zip()` | Data transformation pipeline |
| 4 | Closures & function factories | Multiplier / discount generators |
| 5 | Decorators: writing and applying `@decorator` | `@timer` and `@validate_input` decorator |
| **Mini Project** | — | **Utility Toolkit** (a module of helper functions you'll reuse forever) |

### Week 6 — Object-Oriented Programming (OOP)
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | Classes & instances, `__init__`, attributes | `BankAccount` class |
| 2 | Methods vs functions, `self` | `Student` class with grade methods |
| 3 | Inheritance & `super()` | `SavingsAccount` extends `BankAccount` |
| 4 | Dunder methods (`__str__`, `__repr__`, `__len__`, `__eq__`) | Custom `Vector` class |
| 5 | Class methods (`@classmethod`) & static methods (`@staticmethod`) | `User` class with factory constructors |
| **Mini Project** | — | **CLI Library System** (Book, Member, Library classes) |

### Week 7 — Modules, Packages & the Standard Library
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | Structuring your own modules & packages | Multi-file project layout |
| 2 | `datetime` & `time` — dates, formatting, timezones | Age & deadline calculator |
| 3 | `os` & `pathlib` — filesystem navigation | File organizer script |
| 4 | `re` (regular expressions) — pattern matching | Email & phone number validator |
| 5 | `argparse` — CLI argument parsing | Scriptable command-line tools |
| **Mini Project** | — | **File Organizer CLI** (sorts downloads folder by extension/date) |

### Week 8 — Pythonic Code & Performance
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | List/dict/set comprehensions (advanced patterns) | Data cleanup pipeline |
| 2 | Generators & `yield` — memory-efficient iteration | Large file line reader |
| 3 | Context managers (`with`) — writing your own | `Timer` and `FileManager` context managers |
| 4 | Type hints & `mypy` — writing self-documenting code | Typed versions of Week 5-7 projects |
| 5 | Profiling & optimizing slow code | Benchmarking comparisons |
| **Mini Project** | — | **Data Cleaner** (reads messy CSV, fixes issues, writes clean version) |

---

## 🛠️ Phase 3: Applied Python (Weeks 9–14)
> **Goal:** Build tools that actually run on the internet and talk to external systems.

### Week 9 — Working with APIs
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | HTTP basics (GET, POST, status codes, headers) | Concept walkthrough |
| 2 | `requests` library — calling REST APIs | Live weather CLI tool |
| 3 | Parsing JSON API responses | Crypto price tracker |
| 4 | API authentication (API keys, Bearer tokens) | GitHub profile viewer |
| 5 | Rate limiting, retries & error handling in API calls | Robust API client wrapper |
| **Mini Project** | — | **News Digest CLI** (fetches top headlines by topic using NewsAPI) |

### Week 10 — Web Scraping
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | HTML structure — understanding the DOM | Manual inspection practice |
| 2 | `BeautifulSoup` — parsing HTML | Static page scraper |
| 3 | Extracting tables, links & images | Wikipedia table extractor |
| 4 | Handling pagination & dynamic content | Multi-page scraper |
| 5 | Respecting `robots.txt` & ethical scraping | Scraper with rate limiting |
| **Mini Project** | — | **Job Posting Scraper** (saves listings to CSV with filters) |

### Week 11 — Databases (SQL)
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | Relational databases & SQL basics (`SELECT`, `WHERE`, `ORDER BY`) | Concept walkthroughs |
| 2 | `sqlite3` — using SQL inside Python | Local database creator |
| 3 | CRUD with `sqlite3` | CLI To-Do app backed by SQLite |
| 4 | Joins & relationships (one-to-many, many-to-many) | Student/Course enrollment DB |
| 5 | `SQLAlchemy` ORM basics | Python class → database table mapping |
| **Mini Project** | — | **Expense Tracker v2** (full SQL backend, categories, monthly reports) |

### Week 12 — Building Web Apps with Flask
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | Flask basics: routes, templates, `render_template` | "Hello World" web page |
| 2 | HTML forms & `request.form` — handling user input | Simple form → response page |
| 3 | Connecting Flask to SQLite | Persistent note-taking web app |
| 4 | REST API with Flask (`jsonify`, status codes) | JSON API for the expense tracker |
| 5 | Deploying Flask apps to the web (Railway / Render) | Live URL for your project |
| **Mini Project** | — | **Personal Portfolio API** (Flask REST API listing your projects) |

### Week 13 — Testing & Code Quality
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | Why testing matters — unit vs integration tests | Concept + examples |
| 2 | `pytest` basics — writing and running tests | Test suite for your utility toolkit |
| 3 | Test-driven development (TDD) — write tests first | TDD kata: FizzBuzz & Roman numerals |
| 4 | Mocking external calls with `unittest.mock` | Testing API-dependent code |
| 5 | Code coverage & `pytest-cov` | Achieving 90%+ coverage |
| **Mini Project** | — | **Fully Tested Flask API** (all endpoints covered by tests) |

### Week 14 — Git, GitHub & Project Structure
| Lesson | Topic | Build |
|:--|:--|:--|
| 1 | Branching: `git branch`, `checkout`, `merge` | Feature branch workflow |
| 2 | Pull requests & code review | Collaborating on a fork |
| 3 | Professional project structure (`src/`, `tests/`, `docs/`) | Restructure your best project |
| 4 | `README.md` best practices, `LICENSE`, `.gitignore` | Polished GitHub profile |
| 5 | GitHub Actions CI — auto-run tests on push | CI pipeline for your Flask project |
| **Capstone** | — | **GitHub Portfolio Ready** — 3 clean repos with tests, CI, and READMEs |

---

## 📊 Phase 4: Data & Automation (Weeks 15–20)
> **Goal:** Work with real data the way data engineers do at companies.

### Week 15 — NumPy
Numerical computing, arrays, vectorized math, broadcasting.
**Build:** Scientific calculator that handles arrays of measurements.

### Week 16 — Pandas
DataFrames, loading CSVs/JSON/Excel, cleaning messy data, `groupby`, `merge`, `pivot`.
**Build:** Sales analytics dashboard (CLI) from raw transaction data.

### Week 17 — Data Visualization
`matplotlib` and `seaborn` — line charts, bar charts, heatmaps, histograms.
**Build:** Monthly expense report with auto-generated charts.

### Week 18 — Advanced Pandas & ETL Pipelines
Multi-source data joins, missing data strategies, transformation chains, writing to multiple formats.
**Build:** ETL pipeline that pulls from an API, cleans data, and saves to SQLite.

### Week 19 — Automation & Scheduling
`schedule`, `subprocess`, `smtplib` (email), OS automation, running scripts on a timer.
**Build:** Daily automated report emailed to yourself every morning.

### Week 20 — Phase 4 Capstone
**Build:** End-to-end data pipeline — scrape or pull from an API, clean with Pandas, store in SQL, visualize, and auto-email a weekly report.

---

## 🤖 Phase 5: AI & ML Engineering (Weeks 21–28)
> **Goal:** Build, train, evaluate, and deploy machine learning and AI systems.

### Week 21 — Machine Learning Foundations
Statistics refresher (mean, median, std dev, correlation), intro to `scikit-learn`, train/test split, accuracy metrics.

### Week 22 — Supervised Learning
Linear regression, logistic regression, decision trees, random forests, model evaluation (confusion matrix, F1, ROC).
**Build:** House price predictor / loan approval classifier.

### Week 23 — Unsupervised Learning
K-means clustering, PCA (dimensionality reduction), anomaly detection.
**Build:** Customer segmentation system.

### Week 24 — Deep Learning Foundations
Neural networks (perceptron → multi-layer), backpropagation intuition, `PyTorch` basics.
**Build:** Handwritten digit classifier (MNIST).

### Week 25 — Natural Language Processing (NLP)
Tokenization, TF-IDF, word embeddings, sentiment analysis, text classification.
**Build:** Product review sentiment analyzer.

### Week 26 — Working with LLMs & the Gemini / OpenAI APIs
Prompt engineering, embeddings, retrieval-augmented generation (RAG), building chatbots.
**Build:** AI-powered FAQ bot backed by your own documents.

### Week 27 — MLOps: Deploying AI
Model serving with FastAPI, containerizing with Docker, monitoring model performance.
**Build:** Deployed ML API — public URL that returns predictions.

### Week 28 — Phase 5 Capstone
**Build:** End-to-end AI product — a web interface that takes user input, queries an LLM or ML model, stores conversations in a database, and returns structured intelligent responses.

---

## 📌 Principles To Code By

> These rules separate amateurs from professionals. Internalize them early.

1. **Write it ugly first.** Make it work before making it clean.
2. **Name things clearly.** `get_monthly_expenses()` beats `func1()` every time.
3. **One function, one job.** A function that does two things should be two functions.
4. **If you copied it, understand it.** Never paste code you can't explain line by line.
5. **Commit small and often.** One logical change = one commit.
6. **Read error messages in full.** The last line of a Python traceback is your answer.
7. **Master the fundamentals.** Frameworks come and go — logic is forever.
8. **Build real things.** A project you built beats a certificate every time.

---

## 🏁 What You'll Be Able to Do After 28 Weeks

- ✅ Write Python fluently without referring to documentation for basics
- ✅ Build and deploy full-stack web applications
- ✅ Design and query relational databases
- ✅ Build automated data pipelines (ETL)
- ✅ Train and evaluate machine learning models
- ✅ Build products powered by LLMs (like ChatGPT, Gemini)
- ✅ Contribute to open source and pass technical interviews
- ✅ Apply for: Data Analyst, Backend Developer, ML Engineer, Data Engineer, AI Engineer roles

---

*Last updated: Week 2 in progress.*
