# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform the division and check for zero denominator
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only."
