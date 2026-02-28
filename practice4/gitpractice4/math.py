"""
Math and random operations
"""

import math
import random


# 1. Basic math functions
def square_root(x):
    return math.sqrt(x)


def power(base, exp):
    return math.pow(base, exp)


def factorial(n):
    return math.factorial(n)


# 2. Random utilities
def random_integer(a, b):
    """Return random integer between a and b (inclusive)."""
    return random.randint(a, b)


def random_choice(lst):
    """Return random element from list."""
    return random.choice(lst)