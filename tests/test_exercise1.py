import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even():
    """Test that is_even returns True for even numbers and False for odd numbers."""
    assert is_even(4) == True, "Even number 4 should return True"
    assert is_even(3) == False, "Odd number 3 should return False"
    assert is_even(0) == True, "Zero is even and should return True"
    assert is_even(2) == True, "Even number 2 should return True"
    assert is_even(1) == False, "Odd number 1 should return False"


# bug report 2
def test_r2_rectangle_area():
    """Test that rectangle_area returns the product of width and height."""
    assert rectangle_area(5, 3) == 15, "Rectangle area should return 15 for width=5, height=3"
    assert rectangle_area(4, 6) == 24, "Rectangle area should return 24 for width=4, height=6"
    assert rectangle_area(0, 5) == 0, "Rectangle area should return 0 for width=0"
    assert rectangle_area(7, 7) == 49, "Rectangle area should return 49 for width=7, height=7"


# bug report 3
def test_r3_double():
    """Test that double(n) returns twice the number n."""
    assert double(4) == 8, "double(4) should return 8, but returns 6"
    assert double(0) == 0, "double(0) should return 0"
    assert double(3) == 6, "double(3) should return 6"
    assert double(10) == 20, "double(10) should return 20"
