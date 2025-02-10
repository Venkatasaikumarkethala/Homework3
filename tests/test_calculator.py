"""
Unit tests for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator  # Import only the Calculator class
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide  # Import operations separately

@pytest.mark.parametrize("number1, number2, operation, expected", [
    (3, 2, add, 5),
    (10, 5, subtract, 5),
    (4, 3, multiply, 12),
    (20, 4, divide, 5),
])
def test_operations(number1, number2, operation, expected):
    """Tests arithmetic operations using the Calculation class."""
    calc = Calculation(number1, number2, operation)
    assert calc.get_result() == expected

def test_calculator_perform_operation():
    """Tests the Calculator class using Calculation."""
    assert Calculator.perform_operation(6, 2, add) == 8
    assert Calculator.perform_operation(9, 3, subtract) == 6
    assert Calculator.perform_operation(7, 5, multiply) == 35
    assert Calculator.perform_operation(12, 4, divide) == 3

def test_divide_by_zero():
    """Tests division by zero error."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)
