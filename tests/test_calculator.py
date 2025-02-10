"""
Unit tests for the Calculator class and history management.
"""

import pytest
from calculator.calculator import Calculator
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture(autouse=True)
def setup():
    """Clears history before each test to ensure clean state."""
    Calculations.clear_history()

@pytest.mark.parametrize("number1, number2, operation, expected", [
    (3, 2, add, 5),
    (10, 5, subtract, 5),
    (4, 3, multiply, 12),
    (20, 4, divide, 5),
])
def test_operations(number1, number2, operation, expected):
    """Tests arithmetic operations using the Calculation class."""
    result = Calculator.perform_operation(number1, number2, operation)
    assert result == expected

def test_calculator_perform_operation():
    """Tests the Calculator class using Calculation."""
    assert Calculator.perform_operation(6, 2, add) == 8
    assert Calculator.perform_operation(9, 3, subtract) == 6
    assert Calculator.perform_operation(7, 5, multiply) == 35
    assert Calculator.perform_operation(12, 4, divide) == 3

def test_calculation_history():
    """Tests calculation history management."""
    calc1 = Calculator.perform_operation(2, 2, add)
    calc2 = Calculator.perform_operation(4, 2, subtract)

    assert len(Calculations.get_all_calculations()) == 2
    assert Calculations.get_latest().get_result() == calc2

def test_clear_history():
    """Tests clearing calculation history."""
    Calculator.perform_operation(3, 3, multiply)
    assert len(Calculations.get_all_calculations()) == 1
    Calculator.clear_history()
    assert len(Calculations.get_all_calculations()) == 0

def test_divide_by_zero():
    """Tests division by zero error."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        Calculator.perform_operation(10, 0, divide)

def test_clear_history():
    """Tests clearing the calculation history."""
    Calculator.perform_operation(5, 5, add)
    assert len(Calculations.get_all_calculations()) == 1
    Calculator.clear_history()
    assert len(Calculations.get_all_calculations()) == 0

def test_get_latest_calculation():
    """Tests retrieving the latest calculation."""
    Calculator.perform_operation(10, 2, subtract)
    latest_calc = Calculator.get_latest_calculation()
    assert latest_calc.get_result() == 8
