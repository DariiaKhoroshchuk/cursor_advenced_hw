# 1. Create tests for class Calculator (functions_to_test.py)
#     a. Using unittest lib
#     b. Using pytest lib
""" A simple calculator App"""


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')

    return x / y
