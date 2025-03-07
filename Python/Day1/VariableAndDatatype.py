"""
This Python script covers the fundamental concepts of variables and data types.
Every section is explained with detailed comments, examples, and explanations.

Topics Covered:
1. Variables and Assignments
2. Naming Rules for Variables
3. Data Types (int, float, str, bool, list, tuple, set, dict)
4. Numeric Data Types
5. String Operations
6. Boolean Values
7. Lists and their Operations
8. Tuples and their Properties
9. Sets and their Properties
10. Dictionaries and Key-Value Pairs
11. Type Conversion (Casting)
12. User Input Handling
13. Mutable vs Immutable Data Types
"""

# ------------------- 1. Variables and Assignments -------------------
# In Python, variables are used to store data values.
# Python is dynamically typed, meaning we don't need to declare a variable type explicitly.

name = "John Doe"  # A string variable
age = 25  # An integer variable
height = 5.9  # A floating-point variable
is_student = True  # A boolean variable

# Printing the variables along with their types
print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Is Student:", is_student, "Type:", type(is_student))

# ------------------- 2. Naming Rules for Variables -------------------
# ✅ Valid variable names
my_var = 10
_myVar = 20
myVar123 = 30
myVarName = "Valid"

# ❌ Invalid variable names (these will cause errors if uncommented)
# 123abc = "Invalid"  # Cannot start with a number
# my-var = "Invalid"  # Cannot contain hyphen (-)
# my var = "Invalid"  # Cannot have spaces

# ------------------- 3. Data Types in Python -------------------
# Python has various built-in data types:
# int, float, str, bool, list, tuple, set, dict

# Integer (int)
num1 = 100
print("Integer:", num1, "Type:", type(num1))

# Float (float)
num2 = 10.75
print("Float:", num2, "Type:", type(num2))

# Complex Number (complex)
num3 = 3 + 4j
print("Complex Number:", num3, "Type:", type(num3))

# ------------------- 4. String Data Type -------------------
# Strings are sequences of characters
string1 = 'Hello'
string2 = "Python"
string3 = '''Multiline
String'''

print("First character of string1:", string1[0])  # Indexing
print("Substring from string2:", string2[1:4])  # Slicing

# ------------------- 5. Boolean Data Type -------------------
# Boolean represents True or False values
is_python_easy = True
is_java_hard = False

print("Is Python Easy?", is_python_easy, "Type:", type(is_python_easy))
print("Is Java Hard?", is_java_hard, "Type:", type(is_java_hard))

# ------------------- 6. List Data Type -------------------
# Lists are ordered, mutable collections
fruits = ["Apple", "Banana", "Cherry"]
print("Fruits List:", fruits, "Type:", type(fruits))

# Modify the list
fruits.append("Mango")  # Adds a new element
print("Updated Fruits List:", fruits)

# ------------------- 7. Tuple Data Type -------------------
# Tuples are ordered but immutable
coordinates = (10.5, 20.3)
print("Coordinates Tuple:", coordinates, "Type:", type(coordinates))

# ------------------- 8. Set Data Type -------------------
# Sets store unique values and do not allow duplicates
unique_numbers = {1, 2, 3, 1, 2}  # Duplicate values are ignored
print("Unique Numbers Set:", unique_numbers, "Type:", type(unique_numbers))

# ------------------- 9. Dictionary Data Type -------------------
# A dictionary stores data in key-value pairs
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A"
}

print("Student Dictionary:", student, "Type:", type(student))
print("Student Name:", student["name"])

# ------------------- 10. Type Conversion (Casting) -------------------
# Converting between different data types

a = 10
b = float(a)  # Converts int to float
print("Converted float:", b, "Type:", type(b))

c = "100"
d = int(c)  # Converts string to int
print("Converted int:", d, "Type:", type(d))

e = [1, 2, 3]
f = tuple(e)  # Converts list to tuple
print("Converted Tuple:", f, "Type:", type(f))

# ------------------- 11. User Input in Python -------------------
# Taking input from the user
# Input is always a string, so type conversion may be needed

# user_age = int(input("Enter your age: "))  # Uncomment to take input
# print("Your age is:", user_age, "Type:", type(user_age))

# ------------------- 12. Mutable vs Immutable Data Types -------------------
# Some data types are mutable (changeable), while others are immutable (cannot change)

# Mutable (can change): List, Dictionary, Set
mutable_list = [1, 2, 3]
mutable_list.append(4)
print("Modified List:", mutable_list)

# Immutable (cannot change): Tuple, String
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10  # ❌ This will cause an error
print("Immutable Tuple:", immutable_tuple)

# ------------------- Summary -------------------
"""
Key Takeaways:
1️⃣ Variables store values dynamically without explicit type declaration.
2️⃣ Data types include int, float, str, bool, list, tuple, set, and dict.
3️⃣ Lists are mutable, while tuples are immutable.
4️⃣ Dictionaries store key-value pairs; sets store unique elements.
5️⃣ Type conversion allows changing data types dynamically.
6️⃣ User input requires type conversion if needed.
7️⃣ Understanding mutable vs immutable helps prevent unintended modifications.
"""

# End of script 🚀
