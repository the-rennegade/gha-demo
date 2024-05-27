import sys

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

print(f"Python Version: {sys.version}")

print("3 + 2 =")
print(add(3, 2))

print("5 - 2 =")
print(subtract(5, 2))
