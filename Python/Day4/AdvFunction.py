# =============================================================================
#                EVERYTHING ABOUT MAP, REDUCE, AND LAMBDA IN PYTHON
# =============================================================================
# In this script, we will explore:
# ✅ Lambda functions (anonymous functions in Python)
# ✅ The `map()` function for applying operations to collections
# ✅ The `reduce()` function for cumulative operations
# ✅ Real-world examples of these functions

# =============================================================================
#                           1️⃣ LAMBDA FUNCTION
# =============================================================================
# A lambda function in Python is an **anonymous, single-line function**.
# It has no name and can have multiple parameters but only one expression.
# Syntax:
#       lambda arguments: expression

# Example 1: A lambda function to add 10 to a number
add_10 = lambda x: x + 10
print("Lambda Add 10:", add_10(5))  # Output: 15

# Example 2: A lambda function to multiply two numbers
multiply = lambda x, y: x * y
print("Lambda Multiply:", multiply(4, 5))  # Output: 20

# Example 3: Using lambda inside a sorted function
names = ["Alice", "Bob", "Charlie", "David"]
names_sorted = sorted(names, key=lambda name: len(name))  # Sorting by length
print("Sorted by length:", names_sorted)  # Output: ['Bob', 'Alice', 'David', 'Charlie']

# =============================================================================
#                           2️⃣ MAP FUNCTION
# =============================================================================
# The `map()` function applies a given function to **each item** in an iterable (like a list).
# Syntax:
#       map(function, iterable)

# Example 1: Squaring numbers using map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 2: Converting a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = list(map(lambda word: word.upper(), words))
print("Uppercase Words:", uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# =============================================================================
#                           3️⃣ REDUCE FUNCTION
# =============================================================================
# The `reduce()` function is used for **cumulative operations** on an iterable.
# It applies the function **cumulatively**, reducing the iterable to a single value.
# `reduce()` is available in the `functools` module.
# Syntax:
#       reduce(function, iterable)

from functools import reduce

# Example 1: Finding the sum of all numbers in a list
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", sum_of_numbers)  # Output: 15 (1+2+3+4+5)

# Example 2: Finding the product of all numbers in a list
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product_of_numbers)  # Output: 120 (1*2*3*4*5)

# =============================================================================
#             🎯 REAL-WORLD USE CASES OF MAP, REDUCE, AND LAMBDA
# =============================================================================

# ✅ Use Case 1: Convert a list of temperatures from Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print("Fahrenheit Temps:", fahrenheit_temps)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]

# ✅ Use Case 2: Find the longest word in a list using reduce()
words_list = ["Python", "Lambda", "Functions", "MapReduce"]
longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words_list)
print("Longest Word:", longest_word)  # Output: 'Functions'

# ✅ Use Case 3: Filter out odd numbers using map() and lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)  # Output: [2, 4]

# =============================================================================
#                     🎯 SUMMARY 🎯
# =============================================================================
# ✅ `lambda` creates small, anonymous functions with a single expression.
# ✅ `map()` applies a function to every element in an iterable.
# ✅ `reduce()` applies a function cumulatively to reduce an iterable to a single value.
# ✅ These functions make Python more concise and efficient, especially for functional programming.

# =============================================================================
