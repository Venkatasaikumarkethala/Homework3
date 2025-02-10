# 📌 Intermediate Calculator - Level 2 (Part 2)

This is the **Level 2 Intermediate Calculator** implementation for the assignment.  
It introduces **Object-Oriented Programming (OOP)** principles by encapsulating  
calculations inside a **`Calculation` class** and using **static methods** in the `Calculator` class.

---

## 📜 Features

✔️ **Encapsulation** of arithmetic operations using the `Calculation` class  
✔️ **Static method** usage in the `Calculator` class  
✔️ **Exception handling** for division by zero  
✔️ **Modular code structure** (Separation of Concerns)  
✔️ **Unit tests using `pytest`**  
✔️ **Code quality checked with `pylint`**  

---

## 📂 Project Structure

```
calculator_project/
│── calculator/
│   │── __init__.py
│   │── calculator.py   # Performs operations using Calculation class
│   │── calculation.py  # Encapsulates a single calculation
│   │── operations.py   # Defines basic arithmetic operations
│── tests/
│   │── test_calculator.py   # Unit tests for Calculator and Calculation classes
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
```

---

## 🛠️ Running Tests

### Run Pytest

```bash
pytest --cov=calculator tests/
```

✔️ Expected Output:
```
========================== 5 passed in 0.06s ==========================
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

### **`Calculator` Class**
- Uses **static methods** to perform operations.
- Calls the `Calculation` class to store and retrieve results.

### **`operations.py`**
- Defines **basic arithmetic functions** (`add`, `subtract`, `multiply`, `divide`).

---

## 🏁 Next Steps - Level 3 (Part 3)
- Implement **calculation history** using a `Calculations` class.
- Store past calculations and retrieve them.
- Use **class methods** for history management.
- Improve **unit testing** with **parameterized test data**.

