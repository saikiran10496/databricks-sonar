import pytest
from notebook1 import add_numbers, subtract_numbers  # Adjust this import based on your notebook's conversion to a .py file

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

def test_subtract_numbers():
    result = subtract_numbers(5, 3)
    assert result == 2, f"Expected 2, but got {result}"

def test_add_numbers_negative():
    result = add_numbers(-1, -1)
    assert result == -2, f"Expected -2, but got {result}"

def test_subtract_numbers_negative():
    result = subtract_numbers(-2, -3)
    assert result == 1, f"Expected 1, but got {result}"

# You can add more tests depending on the functions in your notebook.
