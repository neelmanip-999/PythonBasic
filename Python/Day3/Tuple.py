# ==============================================================
#               EVERYTHING ABOUT TUPLES IN PYTHON
# ==============================================================
# This Python script explains everything about tuples in Python,
# including creation, built-in functions, tuple manipulations, 
# and advanced tuple operations with detailed comments.

# ==============================================================
#                    1️⃣ INTRODUCTION TO TUPLES
# ==============================================================
# A tuple is an ordered collection of elements that are immutable.
# Tuples are similar to lists but cannot be modified after creation.

# Creating tuples
empty_tuple = ()  # An empty tuple
numbers = (10, 20, 30, 40, 50)  # A tuple of integers
mixed_tuple = (1, "hello", 3.14, True)  # A tuple with mixed data types
nested_tuple = ((1, 2, 3), (4, 5, 6))  # A nested tuple (tuple inside a tuple)

# Printing tuples
print("Numbers Tuple:", numbers)
print("Mixed Tuple:", mixed_tuple)
print("Nested Tuple:", nested_tuple)

# ==============================================================
#              2️⃣ ACCESSING TUPLE ELEMENTS
# ==============================================================
# Tuple elements can be accessed using indexes (starting from 0).

print("First element:", numbers[0])  # Accessing first element
print("Last element:", numbers[-1])  # Accessing last element using negative indexing

# Accessing elements from a nested tuple
print("First element of nested tuple:", nested_tuple[0][0])  # Accessing first element of first tuple

# ==============================================================
#              3️⃣ TUPLE SLICING
# ==============================================================
# Slicing allows extracting a part of a tuple.

print("First 3 elements:", numbers[:3])  # Extracting first 3 elements
print("Elements from index 2 to end:", numbers[2:])  # Extracting from index 2 till the end
print("Every second element:", numbers[::2])  # Extracting elements with a step of 2

# ==============================================================
#              4️⃣ IMMUTABILITY OF TUPLES
# ==============================================================
# Unlike lists, tuples **cannot be modified** after creation.

# Trying to modify a tuple will result in an error.
# numbers[0] = 100  # ❌ This will cause a TypeError!

# However, we can **reassign** the entire tuple (but not modify individual elements).
numbers = (100, 20, 30, 40, 50)  # This is allowed
print("Modified Tuple:", numbers)

# ==============================================================
#              5️⃣ TUPLE OPERATIONS (MERGING, REPEATING)
# ==============================================================
# Concatenation (Merging tuples)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged Tuple:", merged_tuple)

# Repetition (Repeating elements)
repeated_tuple = tuple1 * 3  # Repeats tuple1 three times
print("Repeated Tuple:", repeated_tuple)

# ==============================================================
#              6️⃣ TUPLE FUNCTIONS (BUILT-IN METHODS)
# ==============================================================
numbers = (10, 20, 30, 40, 50, 20)

# Finding length
print("Length of tuple:", len(numbers))

# Counting occurrences
print("Count of 20:", numbers.count(20))

# Finding index of an element
print("Index of 40:", numbers.index(40))

# ==============================================================
#              7️⃣ ADVANCED TUPLE OPERATIONS
# ==============================================================
# Tuple unpacking
a, b, *rest = (10, 20, 30, 40, 50)
print("Unpacked Values: a =", a, ", b =", b, ", rest =", rest)

# Checking if an element exists in a tuple
print("Is 30 in tuple1?", 30 in tuple1)
print("Is 100 in tuple1?", 100 in tuple1)

# Converting a tuple to a list (useful if we need to modify elements)
tuple_to_list = list(numbers)
print("Tuple converted to list:", tuple_to_list)

# Converting a list to a tuple
list_to_tuple = tuple([1, 2, 3, 4, 5])
print("List converted to tuple:", list_to_tuple)

# ==============================================================
#                     🎯 SUMMARY 🎯
# ==============================================================
# ✅ Tuples are ordered, immutable collections that store different data types.
# ✅ Elements are accessed using indexing and extracted using slicing.
# ✅ Unlike lists, tuples cannot be modified after creation.
# ✅ Tuples support concatenation, repetition, and built-in methods.
# ✅ Tuple unpacking allows assigning values to multiple variables.
# ✅ Conversion between lists and tuples is possible.

# ==============================================================

