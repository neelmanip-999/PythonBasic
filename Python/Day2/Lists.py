# ==============================================================
#               EVERYTHING ABOUT LISTS IN PYTHON
# ==============================================================
# This Python script explains everything about lists in Python,
# including creation, built-in functions, list manipulations, 
# and advanced list operations with detailed comments.

# ==============================================================
#                    1️⃣ INTRODUCTION TO LISTS
# ==============================================================
# A list is a collection of items stored in a single variable.
# Lists are mutable (can be changed) and can contain different data types.

# Creating lists
empty_list = []  # An empty list
numbers = [10, 20, 30, 40, 50]  # A list of integers
mixed_list = [1, "hello", 3.14, True]  # A list with mixed data types
nested_list = [[1, 2, 3], [4, 5, 6]]  # A nested list (list inside a list)

# Printing lists
print("Numbers List:", numbers)
print("Mixed List:", mixed_list)
print("Nested List:", nested_list)

# ==============================================================
#              2️⃣ ACCESSING LIST ELEMENTS
# ==============================================================
# List elements can be accessed using indexes (starting from 0).

print("First element:", numbers[0])  # Accessing first element
print("Last element:", numbers[-1])  # Accessing last element using negative indexing

# Accessing elements from a nested list
print("First element of nested list:", nested_list[0][0])  # Accessing first element of first list

# ==============================================================
#              3️⃣ LIST SLICING
# ==============================================================
# Slicing allows extracting a part of a list.

print("First 3 elements:", numbers[:3])  # Extracting first 3 elements
print("Elements from index 2 to end:", numbers[2:])  # Extracting from index 2 till the end
print("Every second element:", numbers[::2])  # Extracting elements with a step of 2

# ==============================================================
#              4️⃣ LIST MANIPULATION (MODIFYING LISTS)
# ==============================================================
# Lists are mutable, so we can change elements.

numbers[0] = 100  # Changing first element
print("Modified Numbers List:", numbers)

# Adding elements
numbers.append(60)  # Adds 60 at the end
print("After Append:", numbers)

numbers.insert(2, 25)  # Inserts 25 at index 2
print("After Insert:", numbers)

# Removing elements
numbers.remove(40)  # Removes the first occurrence of 40
print("After Remove:", numbers)

popped_element = numbers.pop()  # Removes last element and returns it
print("After Pop:", numbers, "| Popped Element:", popped_element)

del numbers[1]  # Deletes the element at index 1
print("After Delete:", numbers)

# ==============================================================
#              5️⃣ LIST OPERATIONS (MERGING, REPEATING)
# ==============================================================
# Concatenation (Merging lists)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged List:", merged_list)

# Repetition (Repeating elements)
repeated_list = list1 * 3  # Repeats list1 three times
print("Repeated List:", repeated_list)

# ==============================================================
#              6️⃣ LIST FUNCTIONS (BUILT-IN METHODS)
# ==============================================================
numbers = [10, 20, 30, 40, 50, 20]

# Finding length
print("Length of list:", len(numbers))

# Counting occurrences
print("Count of 20:", numbers.count(20))

# Finding index of an element
print("Index of 40:", numbers.index(40))

# Sorting lists
numbers.sort()  # Ascending order
print("Sorted List:", numbers)

numbers.sort(reverse=True)  # Descending order
print("Reverse Sorted List:", numbers)

# Reversing a list
numbers.reverse()
print("Reversed List:", numbers)

# Copying a list
numbers_copy = numbers.copy()
print("Copied List:", numbers_copy)

# Clearing a list (removes all elements)
numbers.clear()
print("After Clear:", numbers)

# ==============================================================
#              7️⃣ ADVANCED LIST OPERATIONS
# ==============================================================
# List comprehension (creating a list using a single line loop)
squares = [x**2 for x in range(1, 6)]  # Squares of numbers from 1 to 5
print("Squares List:", squares)

# Filtering list using list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers List:", even_numbers)

# List unpacking
a, b, *rest = [10, 20, 30, 40, 50]
print("Unpacked Values: a =", a, ", b =", b, ", rest =", rest)

# Checking if an element exists in a list
print("Is 30 in list1?", 30 in list1)
print("Is 100 in list1?", 100 in list1)

# ==============================================================
#                     🎯 SUMMARY 🎯
# ==============================================================
# ✅ Lists are ordered, mutable collections that can store different data types.
# ✅ Elements are accessed using indexing and modified as needed.
# ✅ Slicing allows extracting portions of lists.
# ✅ Lists can be merged, repeated, sorted, reversed, and copied.
# ✅ Python provides powerful built-in list methods.
# ✅ List comprehensions enable efficient list creation and filtering.

# ==============================================================

