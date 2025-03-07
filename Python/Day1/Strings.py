# ==============================================================
#                  STRINGS IN PYTHON - COMPLETE GUIDE
# ==============================================================
# A string in Python is a sequence of characters enclosed in quotes.
# Strings are one of the most commonly used data types in Python.

# ==============================================================
#                   1️⃣ STRING CREATION
# ==============================================================
# Strings can be created using single, double, or triple quotes.

single_quoted = 'Hello'
double_quoted = "Python"
triple_quoted = '''This is a
multi-line string'''

# Printing the strings
print("Single Quoted:", single_quoted)
print("Double Quoted:", double_quoted)
print("Triple Quoted:\n", triple_quoted)

# Checking the type of a string
print("Type of variable:", type(single_quoted))  # Output: <class 'str'>

# ==============================================================
#                2️⃣ STRING INDEXING AND ACCESS
# ==============================================================
# Strings are indexed, meaning each character has a position (index).
# Indexing starts from 0 (first character) and goes up to (length - 1).

text = "PYTHON"

# Accessing individual characters
print("First character:", text[0])   # P
print("Last character:", text[-1])   # N (negative index starts from the end)
print("Third character:", text[2])   # T

# ==============================================================
#                  3️⃣ STRING SLICING
# ==============================================================
# Slicing allows extracting parts of a string using [start:end:step].
# Syntax: string[start:end]  → Extracts characters from start to (end-1).

message = "Hello, World!"

# Extracting substrings
print("First 5 characters:", message[0:5])  # Hello
print("Last 6 characters:", message[-6:])  # World!
print("Every second character:", message[::2])  # Hlo ol!

# Reversing a string using slicing
reversed_string = message[::-1]
print("Reversed String:", reversed_string)  # !dlroW ,olleH

# ==============================================================
#             4️⃣ POPULAR STRING METHODS (INBUILT FUNCTIONS)
# ==============================================================

sample_text = "  python programming  "

# ✅ Converting to Uppercase and Lowercase
print("Uppercase:", sample_text.upper())  # PYTHON PROGRAMMING
print("Lowercase:", sample_text.lower())  # python programming

# ✅ Removing extra spaces
print("Stripped Text:", sample_text.strip())  # "python programming" (removes leading/trailing spaces)

# ✅ Finding substrings
print("Index of 'prog':", sample_text.find("prog"))  # 8 (index where 'prog' starts)

# ✅ Replacing text
print("Replaced Text:", sample_text.replace("python", "Java"))  # "  Java programming  "

# ✅ Checking if a string starts or ends with a specific word
print("Starts with 'python':", sample_text.strip().startswith("python"))  # True
print("Ends with 'ing':", sample_text.strip().endswith("ing"))  # True

# ✅ Splitting a string into a list of words
words = sample_text.strip().split(" ")  # Splits by spaces
print("Words List:", words)  # ['python', 'programming']

# ✅ Joining a list of words into a string
joined_text = "-".join(words)
print("Joined Text:", joined_text)  # python-programming

# ==============================================================
#                  5️⃣ STRING IMMUTABILITY
# ==============================================================
# Strings in Python are immutable, meaning they cannot be changed after creation.

immutable_str = "Python"

# ❌ This will cause an error: immutable_str[0] = 'J'
# ✅ Instead, create a new string
new_str = "J" + immutable_str[1:]
print("Modified String:", new_str)  # Jython

# ==============================================================
#         6️⃣ MULTI-LINE STRINGS AND ESCAPE CHARACTERS
# ==============================================================

# Multi-line strings using triple quotes
multi_line_string = """This is
a multi-line
string."""
print(multi_line_string)

# Escape characters
print("This is a \"quoted\" word")  # Using \" to include quotes
print("New line\nNext line")  # \n moves text to a new line
print("Tab\tSpace")  # \t adds a tab space

# ==============================================================
#           7️⃣ STRING FORMATTING (f-strings, format, %)
# ==============================================================

name = "Alice"
age = 25

# ✅ f-strings (Recommended)
print(f"My name is {name} and I am {age} years old.")

# ✅ Using format()
print("My name is {} and I am {} years old.".format(name, age))

# ✅ Using % operator
print("My name is %s and I am %d years old." % (name, age))

# ==============================================================
#                           🔥 SUMMARY 🔥
# ==============================================================
# ✅ Strings are sequences of characters enclosed in quotes.
# ✅ Strings are indexed (both positive and negative indexing).
# ✅ String slicing allows extracting parts of a string.
# ✅ Strings are immutable (cannot be modified directly).
# ✅ Python provides many inbuilt string methods like upper(), lower(), strip(), find(), replace(), etc.
# ✅ String formatting can be done using f-strings, .format(), or % formatting.
# ✅ Escape characters like \n (newline) and \t (tab) are used to format strings.

# ==============================================================
#            🎯 NEXT STEPS: PRACTICE EXERCISES 🎯
# ==============================================================

