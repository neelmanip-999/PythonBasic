# ==============================================================
#               LOOP EXERCISES SOLUTIONS IN PYTHON
# ==============================================================
# This Python script contains solutions to 5 different loop-based exercises.
# Each exercise is solved step by step with proper comments and explanations.

# ==============================================================
#            1️⃣ PRINT EVEN NUMBERS BETWEEN 1 AND 50
# ==============================================================
# We use a for loop to iterate from 1 to 50 and print only even numbers.

print("Even numbers between 1 and 50:")

# Using a for loop with range()
for num in range(1, 51):
    if num % 2 == 0:  # Checking if the number is even
        print(num, end=" ")  # Printing numbers in one line

print("\n")  # Adding a new line for better readability


# ==============================================================
#        2️⃣ FIND SUM OF DIGITS OF A NUMBER USING WHILE LOOP
# ==============================================================
# The program takes a number from the user and finds the sum of its digits.

# Taking user input
number = int(input("Enter a number to find sum of its digits: "))

# Initializing sum to 0
sum_of_digits = 0

# Using a while loop to extract and sum digits
while number > 0:
    digit = number % 10  # Extracting last digit
    sum_of_digits += digit  # Adding digit to sum
    number //= 10  # Removing last digit

# Displaying the sum of digits
print("Sum of digits:", sum_of_digits)


# ==============================================================
#         3️⃣ COUNT LETTER OCCURRENCES IN A WORD
# ==============================================================
# The program takes a word and a letter, then counts how many times the letter appears.

# Taking user input
word = input("Enter a word: ")
letter = input("Enter a letter to count its occurrences: ")

# Initializing count to 0
letter_count = 0

# Looping through each character in the word
for char in word:
    if char == letter:  # Checking if character matches the letter
        letter_count += 1

# Displaying the count of the letter
print(f"The letter '{letter}' appears {letter_count} times in '{word}'.")


# ==============================================================
#              4️⃣ PRINT A PYRAMID PATTERN
# ==============================================================
# This program prints a pyramid pattern of stars.

# Taking the number of rows as input
rows = int(input("Enter the number of rows for the pyramid: "))

print("Pyramid Pattern:")

# Using nested loops to print the pyramid
for i in range(1, rows + 1):
    # Printing spaces for alignment
    print(" " * (rows - i), end="")
    # Printing stars
    print("* " * i)

print()  # Adding a new line for better readability


# ==============================================================
#           5️⃣ GENERATE FIBONACCI SEQUENCE UP TO 10 TERMS
# ==============================================================
# The Fibonacci sequence starts with 0 and 1, where each next term is the sum of the previous two.

print("Fibonacci sequence up to 10 terms:")

# Initializing the first two terms
a, b = 0, 1

# Using a for loop to generate 10 terms
for _ in range(10):
    print(a, end=" ")  # Printing the term
    a, b = b, a + b  # Updating terms

print("\n")  # Adding a new line for better readability


# ==============================================================
#                    🎯 PROGRAM SUMMARY 🎯
# ==============================================================
# ✅ We printed all even numbers between 1 and 50 using a for loop.
# ✅ We found the sum of digits of a number using a while loop.
# ✅ We counted how many times a letter appears in a word using loops.
# ✅ We printed a pyramid pattern using nested loops.
# ✅ We generated the Fibonacci sequence up to 10 terms using a loop.

# ==============================================================

