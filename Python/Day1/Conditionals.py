# conditionals_python.py

"""
This Python script covers the fundamental concepts of conditionals.
Every section is explained with detailed comments and examples.

Topics Covered:
1. Introduction to Conditionals
2. If Statement
3. If-Else Statement
4. If-Elif-Else Ladder
5. Nested If Statements
6. Logical Operators in Conditionals
7. Short-Circuiting in Conditionals
8. Ternary Operator (Conditional Expressions)
9. Match-Case (Python 3.10+)
10. Real-world Example
"""

# ------------------- 1. Introduction to Conditionals -------------------
# Conditionals are used to control the flow of execution in a program based on conditions.
# Python supports if, if-else, if-elif-else, and nested if statements.

# ------------------- 2. If Statement -------------------
# The simplest conditional statement checks if a condition is True.

age = 20  # Define an age variable
if age >= 18:  # If condition is True, execute the indented block
    print("You are eligible to vote.")

# ------------------- 3. If-Else Statement -------------------
# The else block executes when the if condition is False.

num = 10
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# ------------------- 4. If-Elif-Else Ladder -------------------
# Used when there are multiple conditions to check in sequence.

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# ------------------- 5. Nested If Statements -------------------
# A conditional statement inside another conditional statement.

num = 15
if num > 0:
    print("Positive Number")
    if num % 5 == 0:
        print("Divisible by 5")

# ------------------- 6. Logical Operators in Conditionals -------------------
# Logical operators (and, or, not) allow combining conditions.

gpa = 3.8
attendance = 85
if gpa >= 3.5 and attendance >= 80:
    print("Eligible for scholarship")

# ------------------- 7. Short-Circuiting in Conditionals -------------------
# 'and' stops if the first condition is False, 'or' stops if the first condition is True.

def check():
    print("Function Executed")
    return True

if False and check():  # 'check()' won't execute due to short-circuiting
    print("This won't be printed")

if True or check():  # 'check()' won't execute due to short-circuiting
    print("This will be printed")

# ------------------- 8. Ternary Operator (Conditional Expressions) -------------------
# A compact way of writing if-else in a single line.

age = 16
message = "Adult" if age >= 18 else "Minor"
print("You are a:", message)

# ------------------- 9. Match-Case (Python 3.10+) -------------------
# A modern way to implement switch-case like functionality.

status_code = 404
match status_code:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")

# ------------------- 10. Real-world Example -------------------
# Checking login access based on role

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful! Welcome Admin.")
elif username == "user" and password == "abcd":
    print("Login successful! Welcome User.")
else:
    print("Invalid credentials. Access denied.")

# ------------------- Summary -------------------
"""
Key Takeaways:
1️⃣ If statements execute code when a condition is True.
2️⃣ If-Else handles both True and False cases.
3️⃣ If-Elif-Else allows multiple conditions.
4️⃣ Nested If checks conditions inside another If.
5️⃣ Logical operators (and, or, not) help combine conditions.
6️⃣ Short-circuiting prevents unnecessary evaluations.
7️⃣ Ternary operators allow compact conditional expressions.
8️⃣ Match-Case provides structured branching for Python 3.10+.
"""

# End of script 🚀
