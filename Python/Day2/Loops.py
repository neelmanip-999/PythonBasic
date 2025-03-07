# ==============================================================
#                   LOOPS IN PYTHON - COMPLETE GUIDE
# ==============================================================
# Loops are used to execute a block of code multiple times.
# Python supports two main types of loops:
# 1. For Loop
# 2. While Loop

# Python also provides loop control statements:
# - break (exit loop)
# - continue (skip iteration)
# - pass (placeholder)

# ==============================================================
#                        1️⃣ FOR LOOP
# ==============================================================
# The 'for' loop is used to iterate over a sequence (list, tuple, string, etc.).

print("FOR LOOP EXAMPLES:")

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)  

# Iterating over a string (character by character)
word = "PYTHON"
for letter in word:
    print("Letter:", letter)  

# Using range() to iterate through numbers
for num in range(1, 6):  # Loops from 1 to 5
    print("Number:", num)  

# Using range() with step
for even in range(0, 10, 2):  # Loops through even numbers from 0 to 8
    print("Even Number:", even)  

# ==============================================================
#                        2️⃣ WHILE LOOP
# ==============================================================
# The 'while' loop runs as long as the condition remains True.

print("\nWHILE LOOP EXAMPLES:")

counter = 1
while counter <= 5:  # Loop continues until counter > 5
    print("Counter:", counter)
    counter += 1  # Incrementing counter

# Using while loop with user input
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to stop: ")  # Keeps asking until user types 'exit'
    print("You entered:", user_input)

# ==============================================================
#              3️⃣ LOOP CONTROL STATEMENTS
# ==============================================================
# Python provides break, continue, and pass statements.

print("\nLOOP CONTROL EXAMPLES:")

# Break statement: Exits the loop immediately
for num in range(1, 10):
    if num == 5:
        print("Breaking at", num)
        break  # Exits loop when num is 5
    print("Number:", num)

# Continue statement: Skips current iteration and moves to the next one
for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue  # Skips iteration when num is 3
    print("Number:", num)

# Pass statement: Does nothing, used as a placeholder
for num in range(1, 4):
    if num == 2:
        pass  # Placeholder, does nothing
    print("Number:", num)

# ==============================================================
#              4️⃣ NESTED LOOPS (LOOP INSIDE LOOP)
# ==============================================================
# A nested loop is a loop inside another loop.

print("\nNESTED LOOP EXAMPLES:")

for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i = {i}, j = {j}")  # Prints combinations

# ==============================================================
#        5️⃣ REAL-WORLD EXAMPLES OF LOOPS
# ==============================================================
print("\nREAL-WORLD EXAMPLES:")

# Example 1: Printing a multiplication table
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Example 2: Summing numbers in a list using a loop
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number  # Adding each number to total
print("Total Sum:", total)

# Example 3: Finding prime numbers in a range using loops
print("Prime numbers between 1 and 20:")
for num in range(2, 21):
    is_prime = True
    for div in range(2, num):  # Checking divisibility
        if num % div == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# ==============================================================
#                     🔥 SUMMARY 🔥
# ==============================================================
# ✅ For loop is used for iterating over sequences like lists, tuples, and strings.
# ✅ While loop runs as long as the condition is True.
# ✅ Loop control statements:
#    - break → exits the loop
#    - continue → skips the current iteration
#    - pass → does nothing, used as a placeholder
# ✅ Nested loops allow loops inside another loop.
# ✅ Loops are used in real-world applications like:
#    - Printing multiplication tables
#    - Summing values in a list
#    - Finding prime numbers

# ==============================================================
#        🎯 NEXT STEPS: PRACTICE EXERCISES 🎯
# ==============================================================


