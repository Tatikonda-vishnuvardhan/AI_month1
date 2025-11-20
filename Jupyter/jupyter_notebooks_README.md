# 📓 `jupyter_notebooks/` – Data, Visualization & ML

This folder contains all my **notebook-based** learning and experiments from Month 1.  
It marks the transition from **pure Python** to **data analysis and machine learning**.

---

## 🧱 Topics Covered

- ✅ NumPy – arrays, shapes, slicing, broadcasting, aggregations  
- ✅ Pandas – DataFrames, CSV I/O, filtering, grouping, exporting  
- ✅ Matplotlib – line & bar charts, multiple series, styling basics  
- ✅ Seaborn – quick EDA plots and relationships  
- ✅ Real dataset exploration (e.g. StudentsPerformance)  
- ✅ Text classification: Spam vs Ham using scikit-learn  
- ✅ Gradient Descent implemented from scratch  

---

## 📁 Notebook Overview

> File names may differ slightly – adjust to your exact naming.

### 1️⃣ `day15-1.ipynb` & `day15-2.ipynb` – NumPy Foundations

**Concepts:**

- Creating 1D, 2D, and 3D arrays with `np.array()`  
- Checking `ndim`, `shape`, and `dtype`  
- Indexing and slicing in multiple dimensions  
- Scalar operations and broadcasting  
- Aggregations like `np.sum(a, axis=0/1/2)`  

These notebooks build comfort with **numerical operations**, which is key for ML and deep learning.

---

### 2️⃣ `day16.ipynb` – Pandas Basics

**Key operations:**

- Importing `pandas as pd` and loading CSV data  
- Creating DataFrames from dictionaries and lists  
- Inspecting data (`head()`, `info()`, `describe()`)  
- Selecting rows/columns using:
  - `df["col"]`, `df[["col1","col2"]]`  
  - Boolean masks: `df[df["col"] > value]`  
- Resetting index and exporting to CSV via `df.to_csv("sample1.csv", index=False)`  

Focus: **slicing, indexing, selecting, and writing back**.

---

### 3️⃣ `day17.ipynb` – Students Performance Dataset

**Dataset:** `day17_StudentsPerformance.csv`  

Tasks performed:

- Load dataset with `pd.read_csv(...)`  
- Inspect structure (columns, types)  
- Filter **high scoring students** based on conditions like:

```python
high_math = df[df["math score"] >= 85]
```

- Combine conditions for multiple subjects (math/reading/writing)  
- Export high scorers to `day17_High_Scorers.csv`

This notebook demonstrates **real-world style filtering** and **subset export**.

---

### 4️⃣ `day18.ipynb` – GroupBy & Aggregations

Focus on `groupby()`:

- Group by a column such as `"Gender"` or `"Class"`  
- Compute:
  - Mean scores  
  - Counts  
  - Sum/Max/Min depending on context  
- Sort aggregated data with `sort_values()`  

This builds intuition for **grouped statistics**, which is very important for analytics.

---

### 5️⃣ `day19.ipynb` – Matplotlib & CSV Data

Focus: building **visuals** from CSV files.

- Import: `from matplotlib import pyplot as plt`  
- Read CSV files such as `day19_data1.csv`, `day19_data2.csv`, `day19_data3.csv`  
- Plot:
  - Line charts: `plt.plot(x, y)`  
  - Bar charts: `plt.bar(x, y)`  
  - Combine multiple lines on the same graph  
- Add labels, titles, legends:

```python
plt.xlabel("Age")
plt.ylabel("Number of Developers")
plt.title("Developers by Age")
plt.legend(["All Developers", "Python Developers"])
plt.show()
```

This notebook creates a strong base in **manual plotting**.

---

### 6️⃣ `day20.ipynb` & `day21.ipynb` – Seaborn EDA

Focus: **faster visualization** with Seaborn.

- Import: `import seaborn as sns`  
- Example plots (depending on notebook content):
  - `sns.scatterplot(...)`  
  - `sns.histplot(...)` or `displot`  
  - `sns.heatmap(...)` for correlations  
  - `sns.jointplot(...)` to see distributions and relationships  

Also includes examples like:
- Filtering subsets:
  - Students with `math score > 80`  
- Looking at distributions across categories

These notebooks show how to do **quick EDA (Exploratory Data Analysis)**.

---

### 7️⃣ `Spam.ipynb` – Spam Detection ML Pipeline

This is the **first true ML project** in the repository.

**Steps:**

1. **Load Data**

```python
import pandas as pd
df = pd.read_csv("spam.csv")
```

2. **Split into Features & Labels**

```python
X = df["message_column"]
y = df["label_column"]  # spam / ham
```

3. **Train/Test Split**

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

4. **Build Pipeline**

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

model = Pipeline([
    ("vec", CountVectorizer()),
    ("clf", MultinomialNB())
])

model.fit(X_train, y_train)
```

5. **Evaluate**

```python
from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

**What this shows:**

- How to work with **text data**  
- How to use scikit-learn **Pipelines**  
- How to evaluate a classifier using standard metrics  

---

### 8️⃣ `Day27.ipynb` – Gradient Descent from Scratch

Focus: building **intuition** for ML optimization.

**Core steps:**

1. Define a function `f(x)` you want to minimize.  
2. Optionally define its derivative `f'(x)` manually.  
3. Choose:
   - Learning rate `lr`  
   - Number of iterations  
   - Initial guess `x0`  

4. Iteratively update:

```python
x = x0
history = [x]

for i in range(num_iters):
    grad = f_prime(x)
    x = x - lr * grad
    history.append(x)
```

5. Plot:

- The curve of `f(x)` across a range  
- The points from `history` using `plt.scatter(...)`  

This gives a **visual sense** of how gradient descent “walks down” the curve to reach a minimum.

---

## ▶️ How to Use These Notebooks

From the repo root:

```bash
pip install -r requirements.txt
jupyter notebook
```

Then:

1. Open the `jupyter_notebooks/` folder from the Jupyter UI.  
2. Start with:
   - `day15-1.ipynb` & `day15-2.ipynb` for NumPy  
   - `day16.ipynb` → `day17.ipynb` → `day18.ipynb` for Pandas  
   - `day19.ipynb` → `day20.ipynb` → `day21.ipynb` for visualization  
   - `Spam.ipynb` for ML  
   - `Day27.ipynb` for gradient descent  

---

## 🧠 Skills Demonstrated in `jupyter_notebooks/`

- Working comfortably with **NumPy arrays**  
- Effectively using **Pandas** for tabular data  
- Visualizing data and trends with **Matplotlib & Seaborn**  
- Implementing a full **text classification pipeline**  
- Understanding and visualizing **gradient-based optimization**  

This folder marks the transition from **“I know Python”** to  
**“I can use Python to analyze data and build ML models.”**
