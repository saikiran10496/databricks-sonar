import sys
import os

# Add the notebooks directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebooks')))

# Import the functions from notebook1
from notebook1 import add_numbers, subtract_numbers

# Test for add_numbers function
def test_add_numbers():
    result = add_numbers(5, 3)
    assert result == 8  # Expected result is 8

def test_add_numbers_negative():
    result = add_numbers(-5, -3)
    assert result == -8  # Expected result is -8

def test_add_numbers_mixed():
    result = add_numbers(-5, 3)
    assert result == -2  # Expected result is -2

# Test for subtract_numbers function
def test_subtract_numbers():
    result = subtract_numbers(5, 3)
    assert result == 2  # Expected result is 2

def test_subtract_numbers_negative():
    result = subtract_numbers(-5, -3)
    assert result == -2  # Expected result is -2

def test_subtract_numbers_mixed():
    result = subtract_numbers(-5, 3)
    assert result == -8  # Expected result is -8
