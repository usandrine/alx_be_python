#!/usr/bin/env python3
"""
arithmetic_operations.py

Defines the perform_operation function for basic arithmetic,
intended to be imported by main.py.
"""

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs one of four basic arithmetic operations on two numbers.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform ('add', 'subtract', 
                       'multiply', or 'divide').

    Returns:
    - float or str: The result of the operation, or an error message 
                    for division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handling for division by zero
            return "Division by zero is not allowed."
        return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'. Must be 'add', 'subtract', 'multiply', or 'divide'."

if __name__ == '__main__':
    # Example usage for testing purposes
    print(f"5 + 6 = {perform_operation(5, 6, 'add')}")
    print(f"10 - 4 = {perform_operation(10, 4, 'subtract')}")
    print(f"7 * 3 = {perform_operation(7, 3, 'multiply')}")
    print(f"9 / 3 = {perform_operation(9, 3, 'divide')}")
    print(f"5 / 0 = {perform_operation(5, 0, 'divide')}")