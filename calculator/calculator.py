"""
Advanced Calculator module using OOP and history management.
"""

from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide  # Import arithmetic operations

class Calculator:
    """Performs arithmetic calculations and stores history."""

    @staticmethod
    def perform_operation(number1: float, number2: float, operation):
        """
        Performs a calculation, stores it in history, and returns the result.
        
        Args:
            number1 (float): First number.
            number2 (float): Second number.
            operation (function): The arithmetic operation.

        Returns:
            float: The result of the operation.
        """
        calculation = Calculation(number1, number2, operation)
        Calculations.add_calculation(calculation)  # Store in history
        return calculation.get_result()

    @staticmethod
    def get_history():
        """Returns the calculation history."""
        return Calculations.get_all_calculations()

    @staticmethod
    def get_latest_calculation():
        """Returns the latest calculation from history."""
        return Calculations.get_latest()

    @staticmethod
    def clear_history():
        """Clears the calculation history."""
        Calculations.clear_history()
