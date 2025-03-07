# =============================================================================
#                      EVERYTHING ABOUT FUNCTIONS IN PYTHON
# =============================================================================
# In this script, we will explore:
# ✅ What are functions in Python?
# ✅ Defining and calling functions
# ✅ Different types of functions
# ✅ Function parameters (default, keyword, arbitrary)
# ✅ Variable scope (local vs global)
# ✅ Recursion
# ✅ 20 Example Functions for Better Understanding

# =============================================================================
#                           1️⃣ WHAT IS A FUNCTION?
# =============================================================================
# A function is a block of code that runs when called. 
# It allows **code reuse, modularity, and better readability**.

# Syntax:
# def function_name(parameters):
#     # function body
#     return value (optional)

# Example 1: A simple function
def greet():
    print("Hello! Welcome to Python Functions.")

greet()  # Calling the function

# =============================================================================
#                       2️⃣ FUNCTION PARAMETERS & ARGUMENTS
# =============================================================================

# Example 2: Function with parameters
def add_numbers(a, b):
    return a + b

print("Addition:", add_numbers(5, 3))  # Output: 8

# Example 3: Default parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()  # Output: Hello, Guest!
greet_user("Alice")  # Output: Hello, Alice!

# Example 4: Keyword arguments
def student_details(name, age):
    print(f"Student: {name}, Age: {age}")

student_details(age=21, name="Bob")  # Order doesn't matter

# Example 5: Arbitrary arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))  # Output: 15

# Example 6: Arbitrary keyword arguments (**kwargs)
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Charlie", age=30, city="New York")

# =============================================================================
#                       3️⃣ VARIABLE SCOPE (LOCAL vs GLOBAL)
# =============================================================================

x = 10  # Global variable

def modify_variable():
    global x  # Using the global keyword
    x = x + 5
    print("Inside function:", x)

modify_variable()
print("Outside function:", x)  # Output: 15

# =============================================================================
#                           4️⃣ RECURSION
# =============================================================================
# A function calling itself is called **recursion**.

# Example 7: Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # Output: 120

# =============================================================================
#                      🎯 20 FUNCTION EXAMPLES FOR PRACTICE 🎯
# =============================================================================

# Example 8: Check if a number is even or odd
def is_even(n):
    return n % 2 == 0

print("Is 10 even?", is_even(10))  # Output: True

# Example 9: Find the maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

print("Max number:", max_of_three(10, 25, 15))  # Output: 25

# Example 10: Find the length of a string without using len()
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

print("Length of 'Python':", string_length("Python"))  # Output: 6

# Example 11: Reverse a string
def reverse_string(s):
    return s[::-1]

print("Reverse of 'hello':", reverse_string("hello"))  # Output: 'olleh'

# Example 12: Check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))  # Output: True

# Example 13: Generate Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print("Fibonacci 10 terms:", fibonacci(10))

# Example 14: Count vowels in a string
def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

print("Number of vowels in 'hello':", count_vowels("hello"))  # Output: 2

# Example 15: Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("30°C in Fahrenheit:", celsius_to_fahrenheit(30))  # Output: 86.0

# Example 16: Find prime numbers in a range
def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

print("Prime numbers between 10 and 50:", primes_in_range(10, 50))

# Example 17: Check if a number is Armstrong
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)

print("Is 153 an Armstrong number?", is_armstrong(153))  # Output: True

# Example 18: Calculate GCD (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD of 48 and 18:", gcd(48, 18))  # Output: 6

# Example 19: Convert a list of words to title case
def title_case(words):
    return [word.capitalize() for word in words]

print("Title case:", title_case(["hello", "world"]))  # Output: ['Hello', 'World']

# Example 20: Check if a given year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("Is 2024 a leap year?", is_leap_year(2024))  # Output: True

# =============================================================================
#                      🎯 SUMMARY 🎯
# =============================================================================
# ✅ Functions allow modular programming and code reuse.
# ✅ Different types of arguments: default, keyword, *args, **kwargs.
# ✅ Scope determines variable accessibility (local vs global).
# ✅ Recursion is when a function calls itself (useful for problems like factorial).
# ✅ We implemented **20 real-world examples** to understand functions better.

# =============================================================================
