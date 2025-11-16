# https://github.com/camry-walter/lab11-CW-AE.git
# Partner 1: Camryn Walter
# Partner 2: Adrian Espinoza
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math
def square_root(a):
    if a > 0:
        return math.sqrt(a)
    else:
        raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return b/a
    except ZeroDivisionError:
        raise ZeroDivisionError

def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise ValueError

def exponent(a, b):
    return a**b


