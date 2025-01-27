# tests/test_notebook1.py

import sys
import os

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from notebooks.notebook1 import your_function_to_test  # Import your function here
 notebook1.py


def test_example_function():
    # Define your expected value for the test
    expected_value = 42
    
    # Call the function you want to test
    result = your_function_to_test()
    
    # Assert that the function's result matches the expected value
    assert result == expected_value


# Example of a more specific test if your function uses a dictionary or JSON-like structure
def test_json_structure():
    # Simulate a dictionary that you are testing
    test_data = {
        "showTitle": True,
        "computePreferences": None,
        "maxResults": 10
    }
    
    # Your function might return something similar to the above structure
    result = your_function_to_test()
    
    # Check that the result matches expected structure
    assert result["showTitle"] is True
    assert result["computePreferences"] is None
    assert result["maxResults"] == 10


# Add more tests as necessary for other functionality in your notebook

