"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply, power, sqrt

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


# TODO: Students will add TestMultiplyDivide class
def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2
def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0
    assert subtract(-5, -3) == -2


def test_power_positive_exponent():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_power_negative_exponent():
    assert power(2, -2) == 0

def test_sqrt_perfect_square():
    assert sqrt(16) == 4
    assert sqrt(1) == 1

def test_sqrt_non_perfect_square():
    assert sqrt(20) in [4, 5]

def test_sqrt_negative_number():
    with pytest.raises(ValueError, match="Negative numbers not supported"):
        sqrt(-9)
