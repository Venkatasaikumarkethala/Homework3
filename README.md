# 📌 Advanced Calculator - Level 3 (Part 3)

This is the **Level 3 Advanced Calculator** implementation for the assignment.  
It introduces **calculation history management** using the `Calculations` class  
and further improves **OOP principles, testing, and code coverage**.

---

## 📜 Features

✔️ **Encapsulation** of arithmetic operations using the `Calculation` class  
✔️ **Static method** usage in the `Calculator` class  
✔️ **Class method** usage in the `Calculations` class for managing history  
✔️ **Calculation history storage and retrieval**  
✔️ **Exception handling** for division by zero  
✔️ **Unit tests using `pytest`** (95%+ coverage)  
✔️ **Code quality checked with `pylint`**  

---

## 📂 Project Structure

```
calculator_project/
│── calculator/
│   │── __init__.py
│   │── calculator.py   # Uses Calculations class to store history
│   │── calculation.py  # Encapsulates a single calculation
│   │── calculations.py # Stores history of calculations
│   │── operations.py   # Defines basic arithmetic operations
│── tests/
│   │── test_calculator.py   # Unit tests for Calculator and Calculations
│── requirements.txt
│── .pylintrc
│── README.md
│── pytest.ini
│── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/calculator_project.git
cd calculator_project
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use the Calculator

### Using Python

Import the calculator module and perform operations:

```python
from calculator.calculator import Calculator
from calculator.operations import add, subtract, multiply, divide

# Perform operations using static method
print(Calculator.perform_operation(5, 3, add))       # Output: 8
print(Calculator.perform_operation(10, 4, subtract)) # Output: 6
print(Calculator.perform_operation(6, 7, multiply))  # Output: 42
print(Calculator.perform_operation(15, 3, divide))   # Output: 5.0

# Retrieve calculation history
print(Calculator.get_history())

# Get the latest calculation result
latest_calc = Calculator.get_latest_calculation()
print(latest_calc.get_result())

# Clear the history
Calculator.clear_history()
```

---

## 🛠️ Running Tests

### Run Pytest

```bash
pytest --cov=calculator tests/
```

✔️ Expected Output:
```
TOTAL                           57      3    95%
========================== 9 passed in 0.06s ==========================
```

### Run Pylint for Code Quality Check

```bash
pylint calculator/
```

✔️ Expected **Pylint Score: 7+/10**  

---

## 📜 Code Explanation

### **`Calculation` Class**
- Encapsulates a **single arithmetic operation**.
- Stores **two operands**, the **operation**, and the **result**.

### **`Calculations` Class**
- Uses **class methods** to **store and retrieve past calculations**.
- Implements **methods for retrieving history, clearing history, and getting the latest calculation**.

### **`Calculator` Class**
- Uses **static methods** to perform operations.
- Calls the `Calculations` class to store and retrieve past results.

### **`operations.py`**
- Defines **basic arithmetic functions** (`add`, `subtract`, `multiply`, `divide`).

---

## 🏁 Final Steps
- ✅ Ensure **all tests pass** (pytest).  
- ✅ Ensure **95%+ test coverage** (pytest-cov).  
- ✅ Ensure **Pylint score 7+/10** (pylint calculator/).  
- ✅ **Submit your GitHub repository link** for grading.

