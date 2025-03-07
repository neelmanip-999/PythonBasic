# =============================================================================
#                   📌 EVERYTHING ABOUT EXCEPTION HANDLING IN PYTHON
# =============================================================================
# ✅ Exceptions are runtime errors that can cause a program to stop unexpectedly.
# ✅ Python provides the `try-except` block to handle exceptions gracefully.
# ✅ Exception handling improves the robustness of the program.
# =============================================================================

# Example 1: Basic Try-Except Block
try:
    num = int(input("Enter a number: "))  # User enters a non-numeric value
    print(f"You entered: {num}")
except ValueError:  # Handles invalid integer conversion
    print("Invalid input! Please enter a valid integer.")

# =============================================================================
#                          1️⃣ HANDLING MULTIPLE EXCEPTIONS
# =============================================================================
# ✅ Python allows handling different exceptions separately.
# ✅ The `except` block can specify different error types.

try:
    a, b = 10, 0
    print(a / b)  # Division by zero error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Invalid input type!")
except Exception as e:
    print(f"Unexpected Error: {e}")  # Catches all other exceptions

# =============================================================================
#                          2️⃣ USING ELSE & FINALLY BLOCKS
# =============================================================================
# ✅ The `else` block executes if no exception occurs.
# ✅ The `finally` block executes no matter what (useful for cleanup).

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("Negative numbers are not allowed!")  # Raising an exception
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Valid input: {num}")  # Executes only if no error occurs
finally:
    print("Execution completed.")  # Always runs (useful for file closing)

# =============================================================================
#                          3️⃣ RAISING CUSTOM EXCEPTIONS
# =============================================================================
# ✅ Python allows manually raising exceptions using the `raise` keyword.
# ✅ This is useful for enforcing business logic.

def withdraw_money(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")  # Raising a custom exception
    balance -= amount
    return balance

try:
    print(withdraw_money(1000, 1500))  # Will raise an exception
except ValueError as e:
    print(f"Transaction Failed: {e}")

# =============================================================================
#                          4️⃣ DEFINING CUSTOM EXCEPTION CLASSES
# =============================================================================
# ✅ We can define our own exception classes by inheriting from `Exception`.

class NegativeNumberError(Exception):
    """Custom Exception for negative numbers"""
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"Valid number: {num}"

try:
    print(check_positive(-5))  # Will raise NegativeNumberError
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}")

# =============================================================================
#                          5️⃣ PRACTICAL EXAMPLES
# =============================================================================

# Example 1: Handling File Not Found Error
try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: The file does not exist!")

# Example 2: Handling KeyError in Dictionary
data = {"name": "Alice", "age": 25}
try:
    print(data["city"])  # Key does not exist
except KeyError:
    print("Error: Key not found in dictionary.")

# Example 3: Handling IndexError in Lists
numbers = [1, 2, 3]
try:
    print(numbers[5])  # Out of range index
except IndexError:
    print("Error: List index out of range.")

# Example 4: Handling TypeError in String Operations
try:
    print("Age: " + 25)  # Cannot concatenate string with int
except TypeError:
    print("Error: Cannot concatenate string with integer.")

# =============================================================================
#                           🎯 SUMMARY 🎯
# =============================================================================
# ✅ `try-except` is used to catch and handle exceptions.
# ✅ Multiple `except` blocks can handle different error types.
# ✅ `finally` is useful for cleanup operations.
# ✅ We can raise custom exceptions using `raise`.
# ✅ Defining custom exception classes allows specific error handling.

# =============================================================================
