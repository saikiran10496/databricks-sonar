import pytest
from notebooks.notebook1 import add_numbers, subtract_numbers  # Correct the import path

def test_add_numbers():
    assert add_numbers(3, 2) == 5
    assert add_numbers(-1, -1) == -2
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(3, 2) == 1
    assert subtract_numbers(-1, -1) == 0
    assert subtract_numbers(0, 1) == -1
