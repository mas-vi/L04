import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_valid_password_input_validation():
    # Test case 1: None input - should raise TypeError due to len(None)
    # Note: The original function will raise an error, so we test that it fails gracefully
    # Since the bug report says it raises an error, we verify it doesn't return a boolean
    try:
        result = is_valid_password(None)
        assert False, "Expected TypeError for None input, but got a result"
    except TypeError:
        pass  # Expected behavior - correct input validation
    
    # Test case 2: Empty string - should return False (correct)
    assert is_valid_password("") == False
    
    # Test case 3: String with less than 8 characters - should return False (correct)
    assert is_valid_password("123456") == False
    
    # Test case 4: String with 8+ characters and no digits - should return False
    assert is_valid_password("abcdefgh") == False
    
    # Test case 5: String with 8+ characters and at least one digit - should return True
    assert is_valid_password("12345678") == True
    
    # Test case 6: Non-string input like integer - should raise TypeError
    try:
        is_valid_password(12345678)
        assert False, "Expected TypeError for integer input"
    except TypeError:
        pass


# bug report 2
def test_r2_clamp_inverted_bounds():
    """Test that clamp works correctly when low > high, returning high for values within the range."""
    assert clamp(7, 10, 5) == 5, "clamp(7, 10, 5) should return 5, not 10"
    assert clamp(3, 10, 5) == 5, "clamp(3, 10, 5) should return 5, not 3"
    assert clamp(15, 10, 5) == 15, "clamp(15, 10, 5) should return 15 when x > high"


# bug report 3
def test_r3_is_passing_invalid_input():
    """Test that is_passing handles non-numeric inputs without raising TypeError"""
    # Test with string input
    assert not is_passing("A"), "String input should return False without raising TypeError"
    
    # Test with other non-numeric types
    assert not is_passing(None), "None input should return False without raising TypeError"
    assert not is_passing(True), "Boolean input should return False without raising TypeError"
    assert not is_passing([1, 2]), "List input should return False without raising TypeError"
    assert not is_passing({"a": 1}), "Dictionary input should return False without raising TypeError"
    
    # Test with negative numbers (should return False as expected)
    assert not is_passing(-1), "Negative grade should return False"
