# 🧠 AI Month 1 – Python, Data & ML Foundations

Welcome! This repository contains my **Month 1 journey** towards becoming an **AI/ML Engineer**.

I structured the work into two main parts:

- `python_files/` → Pure Python practice, OOP, file handling, and CLI mini-projects  
- `jupyter_notebooks/` → NumPy, Pandas, visualization (Matplotlib/Seaborn), and first ML experiments  

---

## 📌 Highlights

- ✅ Strong base in **Python** (syntax, OOP, files, error handling)  
- ✅ Multiple **console projects** (calculator, BMI, guess-the-number, student manager)  
- ✅ Hands-on with **NumPy** & **Pandas** for data manipulation  
- ✅ Visualizations with **Matplotlib** & **Seaborn**  
- ✅ Built a **Spam Detection classifier** using scikit-learn’s `Pipeline` + `MultinomialNB`  
- ✅ Implemented **Gradient Descent from scratch** and visualized the optimization path  

---

## 🗂️ Repository Structure

```bash
AI_month1/
├── python_files/
│   ├── ... Python scripts for each day (Day1–Day14, mini-projects)
│   └── README.md
├── jupyter_notebooks/
│   ├── day15-*.ipynb      # NumPy basics
│   ├── day16.ipynb        # Pandas slicing & indexing
│   ├── day17.ipynb        # StudentsPerformance dataset
│   ├── day18.ipynb        # GroupBy operations
│   ├── day19.ipynb        # Matplotlib charts & CSV data
│   ├── day20.ipynb        # Seaborn basics
│   ├── day21.ipynb        # Seaborn + filtering
│   ├── Spam.ipynb         # Spam detection ML pipeline
│   ├── Day27.ipynb        # Gradient descent from scratch
│   └── README.md
├── datasets/ (optional, if you keep CSVs here)
├── requirements.txt
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
└── CODE_OF_CONDUCT.md
```

> Note: Actual file names may vary slightly depending on how they are organized locally.

---

## 🎯 Learning Goals for Month 1

- Comfortably write and structure **Python code**  
- Understand **OOP concepts** (inheritance, polymorphism, abstract classes)  
- Work with **files & JSON** to persist data  
- Use **NumPy** for numerical operations  
- Use **Pandas** to inspect, filter, and export real datasets  
- Make **visualizations** to understand data  
- Build at least one **end-to-end ML model** using scikit-learn  

---

## 🧩 Key Components

### 1️⃣ `python_files/` – Core Python & Mini-Projects

This folder contains:

- Core Python topics:  
  - Strings, numbers, lists, tuples, sets, dictionaries  
  - Loops, conditions, functions, list operations  
- OOP practice:  
  - `Student`, `Residents`, `Person → Student/Teacher`, `Employee → Dev/Manager`, etc.  
  - Abstract `Shape` class (`Circle`, `Rectangle`, `Square`) with `area()` and `perimeter()`  
- File handling:  
  - Reading/writing `.text` files  
  - Copying contents between files  
- JSON-based **Student Management System**:  
  - Add/view/update/delete/search students  
  - Save and load from JSON (`day14_students.json`)  
  - Input validation, uniqueness checks  

👉 See: [`python_files/README.md`](./python_files/README.md) for detailed breakdown.

---

### 2️⃣ `jupyter_notebooks/` – Data & ML

This folder tracks my transition from **basic data handling** to **machine learning**:

- **NumPy**: array creation, shapes, axes, slicing, broadcasting, reductions  
- **Pandas**:
  - Reading CSVs  
  - Filtering, sorting, slicing  
  - `groupby()` and aggregations  
  - Exporting filtered data to new CSVs  
- **Visualization**:
  - Matplotlib: line plots, bar charts, combined visualizations  
  - Seaborn: distribution and relational plots, basic EDA  
- **ML – Spam Detection**:
  - Load `spam.csv`  
  - Split into train/test (`train_test_split`)  
  - Build a `Pipeline` with text vectorization + `MultinomialNB`  
  - Evaluate using `accuracy_score` and `classification_report`  
- **Optimization – Gradient Descent**:
  - Implement gradient descent for a simple function  
  - Track and plot the descent path with Matplotlib  

👉 See: [`jupyter_notebooks/README.md`](./jupyter_notebooks/README.md) for detailed notebook descriptions.

---

## ⚙️ Tech Stack

- **Language**: Python 3.x  
- **Core Libraries**:  
  - `numpy`, `pandas`  
  - `matplotlib`, `seaborn`  
  - `scikit-learn`  
- **Tools**:  
  - Jupyter Notebook / JupyterLab  
  - Any code editor (VS Code, etc.)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/AI_month1.git
cd AI_month1
```

### 2️⃣ Create and Activate Virtual Environment (Recommended)

```bash
python -m venv .venv

# Windows
.venv\Scriptsctivate

# Linux / macOS
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Python Scripts

```bash
cd python_files

# Examples:
python bmi_calculator.py
python guess_the_number.py
python student_manager.py
python calculator_app.py
```

(Note: Adjust file names to match your actual script names.)

### 5️⃣ Run Notebooks

```bash
jupyter notebook
# or
jupyter lab
```

Then open any notebook from the `jupyter_notebooks/` folder.

---

## 🧪 Example: Spam Detection Workflow

High-level steps followed in `Spam.ipynb`:

1. Load `spam.csv` using Pandas.  
2. Clean/inspect the data (check shapes, sample rows).  
3. Split into train/test using `train_test_split`.  
4. Build a `Pipeline` with:  
   - Text vectorizer (such as `CountVectorizer` or `TfidfVectorizer`)  
   - `MultinomialNB` classifier  
5. Train the model using `.fit(X_train, y_train)`.  
6. Evaluate using:
   - `accuracy_score(y_test, y_pred)`  
   - `classification_report(y_test, y_pred)`  

This is my first **end-to-end NLP classification** project.

---

## 📉 Example: Gradient Descent (Day27)

In `Day27.ipynb`:

- Define a scalar function `f(x)`  
- Initialize a starting point `x0`  
- Iteratively update `x` using gradient descent:  

```python
x = x - lr * f_prime(x)
```

- Log values in a `history` list  
- Visualize:
  - The curve of `f(x)`  
  - The descent steps using `scatter` on top of the curve  

This helps build intuition about **optimization and loss minimization** used in ML.

---

## 📈 Skills Demonstrated

- ✅ Python fundamentals (logic, loops, conditions, functions)  
- ✅ OOP design and class relationships  
- ✅ File & JSON handling for persistence  
- ✅ NumPy operations for numerical computing  
- ✅ Pandas for practical data analysis  
- ✅ Matplotlib/Seaborn for visualization & EDA  
- ✅ Training and evaluating a basic ML model  
- ✅ Implementing optimization (gradient descent) manually  

---

## 🛣️ Roadmap

- 🔜 Month 2 – Feature engineering, more ML models (Regression & Classification)  
- 🔜 Add confusion matrix & ROC curve for Spam classifier  
- 🔜 Add more real-world datasets  
- 🔜 Start organizing code into packages/modules for reuse  

---

## 🤝 Contributing

This is primarily a **personal learning repository**, but suggestions and ideas are welcome.  
See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for simple guidelines.

---

## 📄 License

This project is licensed under the **MIT License** – see [`LICENSE`](./LICENSE) for details.
