# 🐍 `python_files/` – Core Python, OOP & Mini-Projects

This folder contains all **Python script–based** work from Month 1.

The goal here is to build a **solid Python foundation** before moving fully into data science and ML.

---

## 📚 Topics Covered

- ✅ Basic syntax, variables, input/output  
- ✅ Strings, lists, tuples, sets, dictionaries  
- ✅ Loops (`for`, `while`) and control flow (`if/elif/else`)  
- ✅ Functions (with and without return values)  
- ✅ Object-Oriented Programming (classes, inheritance, polymorphism)  
- ✅ File handling (text and JSON)  
- ✅ CLI mini-applications  

---

## 🧱 Typical File Groups

> Actual file names may slightly differ; adjust according to your repo.

### 1️⃣ Basics (Day1–Day4)

- `day1.py`, `begin_python.py`, etc.
- Concepts:
  - Printing, string operations, indexing & slicing  
  - Using `len()`, `upper()`, `lower()`, `title()`, `strip()`, `find()`  
  - f-strings for formatted outputs  
  - Basic arithmetic (`+ - * / // % **`)  
  - Simple `if/else` for decision making  

Example:

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

### 2️⃣ Collections & Algorithms (Day5–Day8)

- Lists, nested lists, slicing with steps  
- Tuples (immutability)  
- Sets and basic set operations (union, intersection, difference)  
- Removing duplicates from a list in two ways:
  - With a loop  
  - Using `set()`  

Example – simple duplicate removal:

```python
def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique
```

Mini-scripts in this section:

- **BMI Calculator** – categorize user into Underweight/Normal/Overweight/Obese based on BMI  
- **Guess the Number Game** – random number between 1 and 100 with hints and attempt counter  
- **Marks Manager** – average, max, min, sorted list, and unique marks  

---

### 3️⃣ OOP Practice (Classes & Inheritance)

Key classes:

- `Residents` – class variables, instance variables, name splitting  
- `Person → Student/Teacher` – inheritance, overriding `get_details()`  
- `Employee → Dev/Manager` – manager with an internal list of employees and methods to add/remove them  
- `Animal → Prey/Predator` – multi-level and multiple inheritance  
- `Shape (abstract) → Circle, Rectangle, Square` – polymorphism with `area()` and `perimeter()` methods  

Example – abstract shape pattern:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

This section shows comfort with **OOP design and polymorphism**.

---

### 4️⃣ File Handling & Student Management System

You’ll find scripts that:

- Open text files with different modes (`r`, `w`)  
- Read whole files, line by line, or in chunks  
- Write and append to files  
- Copy content from one file to another  

#### JSON-based Student Management System

A more advanced CLI project where you can:

- Add new students (name, age, roll number, subjects)  
- View all stored students  
- Update student details (name, age, roll, subjects)  
- Search by **roll number** or **partial name**  
- Delete a student with confirmation  
- All data is persisted into a JSON file so it survives between runs  

Core ideas demonstrated:

- Using **classes** (`Student`) to structure data  
- Using **lists** to maintain an in-memory collection  
- Saving and loading using `json.dump()` / `json.load()`  
- Ensuring **unique roll numbers**  
- Basic error handling and input validation  

---

### 5️⃣ CLI Calculator Application

A structured calculator class with methods:

- `addition(a, b)`  
- `subtraction(a, b)`  
- `multiplication(a, b)`  
- `division(a, b)` (with zero division handling)  
- `remainder(a, b)`  
- `quotient(a, b)`  
- `power(a, b)`  

Plus:

- A user-friendly menu in the console  
- Input validation loops  
- A simplified version using a mapping of choice → function  

This shows ability to create **reusable classes** and **interactive CLI tools**.

---

## ▶️ How to Run Scripts

From the repo root:

```bash
cd python_files

# Examples (replace with your exact file names):
python bmi_calculator.py
python guess_number.py
python calculator_app.py
python student_management.py
```

If you’re using a virtual environment (recommended):

```bash
python -m venv .venv
# Activate it, then:
pip install -r ../requirements.txt
```

---

## 🧠 Skills Demonstrated in `python_files/`

- Writing clean, structured Python scripts  
- Designing and using classes effectively  
- Applying inheritance and polymorphism in realistic examples  
- Handling file input/output and JSON storage  
- Interacting with users via the terminal  
- Implementing basic algorithms & logic  

This folder is the **foundation** that supports all the later work in `jupyter_notebooks/` (NumPy, Pandas, ML, etc.).
