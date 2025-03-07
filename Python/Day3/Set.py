# ==============================================================
#                  EVERYTHING ABOUT SETS IN PYTHON
# ==============================================================
# This Python script explains everything about sets in Python,
# including creation, built-in functions, set operations,
# and advanced set manipulations with detailed comments.

# ==============================================================
#                     1️⃣ INTRODUCTION TO SETS
# ==============================================================
# A set is an **unordered**, **mutable** collection of **unique elements**.
# It does not allow duplicate values and is useful for mathematical operations 
# like union, intersection, and difference.

# Creating an empty set (Note: {} creates an empty dictionary, so we use set())
empty_set = set()

# Creating a set with elements
numbers = {1, 2, 3, 4, 5}
print("Set of numbers:", numbers)

# Creating a set with duplicate values (duplicates are removed automatically)
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates removed:", unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Creating a set from a list
list_to_set = set([10, 20, 20, 30, 40])
print("Converted from list:", list_to_set)  # Output: {10, 20, 30, 40}

# Creating a set using set() constructor
string_set = set("hello")  # Output: {'h', 'e', 'l', 'o'} (unordered)
print("Set from string:", string_set)

# ==============================================================
#               2️⃣ ADDING & REMOVING ELEMENTS
# ==============================================================

# Adding a single element using add()
numbers.add(6)
print("After adding 6:", numbers)

# Adding multiple elements using update()
numbers.update([7, 8, 9])
print("After adding multiple values:", numbers)

# Removing an element using remove() (throws error if element not found)
numbers.remove(3)
print("After removing 3:", numbers)

# Removing an element using discard() (does NOT throw error if element not found)
numbers.discard(10)  # No error even if 10 is not in the set

# Removing a random element using pop()
popped_value = numbers.pop()
print("Popped element:", popped_value)

# Clearing all elements from the set
numbers.clear()
print("Set after clearing:", numbers)

# ==============================================================
#               3️⃣ SET OPERATIONS (UNION, INTERSECTION, ETC.)
# ==============================================================
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# Union: Combines both sets (A ∪ B)
union_set = setA.union(setB)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: Common elements (A ∩ B)
intersection_set = setA.intersection(setB)
print("Intersection:", intersection_set)  # Output: {4, 5}

# Difference: Elements in A but not in B (A - B)
difference_set = setA.difference(setB)
print("Difference (A - B):", difference_set)  # Output: {1, 2, 3}

# Symmetric Difference: Elements in A or B but not both (A △ B)
symmetric_difference_set = setA.symmetric_difference(setB)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

# ==============================================================
#               4️⃣ CHECKING SET RELATIONSHIPS
# ==============================================================

setC = {1, 2}
setD = {1, 2, 3, 4, 5}

# Subset: Checks if setC is a subset of setD (C ⊆ D)
print("Is setC a subset of setD?", setC.issubset(setD))  # Output: True

# Superset: Checks if setD is a superset of setC (D ⊇ C)
print("Is setD a superset of setC?", setD.issuperset(setC))  # Output: True

# Disjoint: Checks if two sets have no common elements
print("Are setC and setB disjoint?", setC.isdisjoint(setB))  # Output: False

# ==============================================================
#               5️⃣ ITERATING THROUGH A SET
# ==============================================================

fruits = {"apple", "banana", "cherry"}

# Looping through a set
for fruit in fruits:
    print("Fruit:", fruit)

# ==============================================================
#               6️⃣ SET COMPREHENSIONS
# ==============================================================
# Similar to list comprehensions, we can create sets dynamically.

# Example: Creating a set of squares from 1 to 5
squares_set = {x**2 for x in range(1, 6)}
print("Set of squares:", squares_set)  # Output: {1, 4, 9, 16, 25}

# ==============================================================
#               7️⃣ FROZEN SETS (IMMUTABLE SETS)
# ==============================================================
# A frozenset is an immutable version of a set.
# Once created, it cannot be modified (i.e., no add() or remove()).

# Creating a frozenset
frozen_numbers = frozenset([1, 2, 3, 4, 5])
print("Frozen Set:", frozen_numbers)

# Attempting to modify will cause an error
# frozen_numbers.add(6)  # ❌ This will raise an AttributeError

# ==============================================================
#               8️⃣ MERGING SETS
# ==============================================================

# Method 1: Using update()
setX = {10, 20}
setY = {30, 40}
setX.update(setY)
print("Merged using update():", setX)  # Output: {10, 20, 30, 40}

# Method 2: Using union() (creates a new set)
merged_set = setX.union(setY)
print("Merged using union():", merged_set)  # Output: {10, 20, 30, 40}

# ==============================================================
#                     🎯 SUMMARY 🎯
# ==============================================================
# ✅ Sets are unordered, mutable collections of unique elements.
# ✅ Elements are added using add(), multiple elements using update().
# ✅ Elements are removed using remove(), discard(), or pop().
# ✅ Supports set operations like union, intersection, difference.
# ✅ Supports subset, superset, and disjoint set checks.
# ✅ Looping through a set is possible.
# ✅ Set comprehensions allow dynamic creation.
# ✅ Frozen sets are immutable versions of sets.
# ✅ Sets are useful in removing duplicates and performing mathematical operations.

# ==============================================================

