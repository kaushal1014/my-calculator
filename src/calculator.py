"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result

# TODO: Students will add multiply, divide, power, sqrt functions
def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    result = 0
    count = 0
    while count < abs(b):
        result += a
        count += 1
    if b < 0:
        result = -result
    return result

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Division by zero not allowed")
    quotient = 0
    remainder = abs(a)
    divisor = abs(b)
    while remainder >= divisor:
        remainder -= divisor
        quotient += 1
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        quotient = -quotient
    return quotient

def power(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, int):
        raise TypeError("Power requires numeric base and integer exponent")
    result = 1
    count = 0
    while count < abs(b):
        result = multiply(result, a)
        count += 1
    if b < 0:
        result = divide(1, result)  # returns 0 for large denominators
    return result

def sqrt(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Sqrt requires numeric input")
    if n < 0:
        raise ValueError("Negative numbers not supported")
    x = 0
    while multiply(x, x) <= n:
        x += 1
    return x - 1

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")