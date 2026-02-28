"""
Iterator and generator exercises
"""

# 1. Simple generator for even numbers
def even_numbers(n):
    """Yield even numbers from 0 to n (inclusive)."""
    for i in range(0, n + 1, 2):
        yield i


# 2. Fibonacci generator
def fibonacci(n):
    """Yield first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# 3. Custom iterator class
class Countdown:
    """Iterator that counts down from start to 0."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value