"""
Arithmetic operations module.
"""

def add(number1: float, number2: float) -> float:
    """Returns the sum of two numbers."""
    return number1 + number2

def subtract(number1: float, number2: float) -> float:
    """Returns the difference of two numbers."""
    return number1 - number2

def multiply(number1: float, number2: float) -> float:
    """Returns the product of two numbers."""
    return number1 * number2

def divide(number1: float, number2: float) -> float:
    """Returns the quotient of two numbers. Raises ValueError if dividing by zero."""
    if number2 == 0:
        raise ValueError("Cannot divide by zero!")
    return number1 / number2
