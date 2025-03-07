# ==============================================================
#               EVERYTHING ABOUT DICTIONARIES IN PYTHON
# ==============================================================
# This Python script explains everything about dictionaries in Python,
# including creation, built-in functions, dictionary manipulations, 
# and advanced dictionary operations with detailed comments.

# ==============================================================
#                    1️⃣ INTRODUCTION TO DICTIONARIES
# ==============================================================
# A dictionary is an **unordered**, **mutable** collection of key-value pairs.
# Each key in a dictionary must be unique and **immutable** (e.g., string, number, tuple).
# Values can be of any data type.

# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with key-value pairs
student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "grades": [90, 85, 88],  # Values can be lists, tuples, or even other dictionaries
    "is_graduated": False
}

# Printing the dictionary
print("Student Information:", student_info)

# ==============================================================
#               2️⃣ ACCESSING DICTIONARY ELEMENTS
# ==============================================================
# Dictionary elements are accessed using keys.

print("Student's Name:", student_info["name"])  # Accessing value using a key
print("Student's Age:", student_info.get("age"))  # Using .get() (avoids errors if key is missing)

# Checking if a key exists
if "major" in student_info:
    print("Major:", student_info["major"])

# Attempting to access a non-existing key (avoiding error)
print("GPA (Default if missing):", student_info.get("GPA", "Not available"))

# ==============================================================
#               3️⃣ MODIFYING A DICTIONARY
# ==============================================================
# Dictionaries are mutable, meaning we can change their contents.

# Adding a new key-value pair
student_info["GPA"] = 3.8
print("Updated Dictionary:", student_info)

# Modifying an existing value
student_info["age"] = 23
print("Updated Age:", student_info["age"])

# Removing a key-value pair using del
del student_info["is_graduated"]
print("Dictionary after deletion:", student_info)

# Removing a key using pop() (returns the value of the removed key)
removed_value = student_info.pop("GPA", "Key not found")  # Avoids error if key is missing
print("Removed GPA:", removed_value)

# ==============================================================
#               4️⃣ DICTIONARY FUNCTIONS (BUILT-IN METHODS)
# ==============================================================

# Getting all keys
print("All Keys:", student_info.keys())

# Getting all values
print("All Values:", student_info.values())

# Getting all key-value pairs as a list of tuples
print("All Items:", student_info.items())

# Copying a dictionary (creates a new independent copy)
student_copy = student_info.copy()
print("Copied Dictionary:", student_copy)

# Clearing all items in a dictionary
student_copy.clear()
print("Cleared Dictionary:", student_copy)

# ==============================================================
#               5️⃣ ITERATING THROUGH A DICTIONARY
# ==============================================================

# Iterating through keys
for key in student_info:
    print("Key:", key, "-> Value:", student_info[key])

# Iterating through key-value pairs
for key, value in student_info.items():
    print(f"{key}: {value}")

# ==============================================================
#               6️⃣ NESTED DICTIONARIES
# ==============================================================
# A dictionary can contain another dictionary.

company = {
    "CEO": {"name": "Elon Musk", "age": 50},
    "Employees": {
        "Alice": {"position": "Engineer", "salary": 70000},
        "Bob": {"position": "Manager", "salary": 85000}
    }
}

# Accessing nested dictionary elements
print("CEO's Name:", company["CEO"]["name"])
print("Bob's Salary:", company["Employees"]["Bob"]["salary"])

# ==============================================================
#               7️⃣ DICTIONARY COMPREHENSIONS
# ==============================================================
# Similar to list comprehensions, we can create dictionaries dynamically.

# Example: Creating a dictionary with squares of numbers from 1 to 5
squares = {x: x**2 for x in range(1, 6)}
print("Squares Dictionary:", squares)

# Example: Converting a list into a dictionary (index as key)
fruits = ["apple", "banana", "cherry"]
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print("Fruit Dictionary:", fruit_dict)

# ==============================================================
#               8️⃣ MERGING DICTIONARIES
# ==============================================================
# Method 1: Using update() (modifies the original dictionary)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print("Merged Dictionary (update method):", dict1)

# Method 2: Using dictionary unpacking (Python 3.5+)
merged_dict = {**dict1, **dict2}
print("Merged Dictionary (unpacking method):", merged_dict)

# ==============================================================
#               9️⃣ REMOVING ITEMS SAFELY
# ==============================================================

# pop() removes a specific key and returns its value
removed_item = student_info.pop("major", "Key not found")  # Avoids error if key is missing
print("Removed Item:", removed_item)

# popitem() removes and returns the last key-value pair (Python 3.7+)
last_item = student_info.popitem()
print("Removed Last Item:", last_item)

# ==============================================================
#                     🎯 SUMMARY 🎯
# ==============================================================
# ✅ Dictionaries store data in key-value pairs.
# ✅ Keys must be unique and immutable, values can be of any type.
# ✅ Dictionaries are mutable (modifiable).
# ✅ Elements are accessed using keys or .get() to avoid errors.
# ✅ We can modify, delete, and iterate over dictionary elements.
# ✅ Dictionary comprehensions allow dynamic creation of dictionaries.
# ✅ Nested dictionaries allow storing complex data structures.
# ✅ We can merge dictionaries using update() or unpacking.

# ==============================================================

