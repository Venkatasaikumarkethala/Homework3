"""
Calculator module using OOP principles.
"""

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide 

class Calculator:
    """Performs arithmetic calculations using Calculation instances."""

    @staticmethod
    def perform_operation(number1: float, number2: float, operation):
        """
        Performs a calculation and returns the result.
        
        Args:
            number1 (float): First number.
            number2 (float): Second number.
            operation (function): The arithmetic operation.

        Returns:
            float: The result of the operation.
        """
        calculation = Calculation(number1, number2, operation)
        return calculation.get_result()
