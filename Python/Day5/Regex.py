# =============================================================================
#                   EVERYTHING ABOUT REGULAR EXPRESSIONS (REGEX) IN PYTHON
# =============================================================================
# ✅ Regular Expressions (regex) are patterns used to match text.
# ✅ Python provides the `re` module to handle regex operations.
# ✅ Regex is useful for pattern matching, validation, and text manipulation.

import re  # Importing regex module

# =============================================================================
#                           1️⃣ REGEX BASIC FUNCTIONS
# =============================================================================

# Example 1: Using re.search() to check if pattern exists in a string
text = "The price of the product is $100"
pattern = r"\$\d+"  # Matches a dollar sign followed by digits

match = re.search(pattern, text)
if match:
    print("Found:", match.group())  # Output: Found: $100

# Example 2: Using re.match() to check if the string starts with a pattern
text = "Hello World!"
pattern = r"Hello"

if re.match(pattern, text):
    print("The string starts with 'Hello'")  # Output: The string starts with 'Hello'

# Example 3: Using re.findall() to extract all numbers from a text
text = "My contact numbers are 9876543210 and 1234567890."
pattern = r"\d{10}"  # Matches 10-digit numbers

numbers = re.findall(pattern, text)
print("Extracted Numbers:", numbers)  # Output: ['9876543210', '1234567890']

# =============================================================================
#                           2️⃣ REGEX METACHARACTERS
# =============================================================================
# Metacharacters are special symbols used to define patterns in regex.
# Some important ones:
# .  - Matches any character except newline
# ^  - Matches the start of a string
# $  - Matches the end of a string
# [] - Matches any one of the characters inside
# () - Groups part of a regex pattern
# *  - Matches 0 or more occurrences of the preceding character
# +  - Matches 1 or more occurrences of the preceding character
# ?  - Matches 0 or 1 occurrence of the preceding character
# |  - OR operator, matches either pattern on either side

# Example 4: Check if a string starts with a digit
text = "123Hello"
pattern = r"^\d"  # ^ ensures it starts with a digit

if re.search(pattern, text):
    print("String starts with a digit.")  # Output: String starts with a digit.

# Example 5: Extract all words starting with 'P' or 'p'
text = "Python is powerful. People love programming in Python."
pattern = r"\b[Pp]\w+"  # \b ensures whole words, \w+ matches word characters

words = re.findall(pattern, text)
print("Words starting with P/p:", words)  # Output: ['Python', 'powerful', 'People', 'programming', 'Python']

# =============================================================================
#                           3️⃣ SPECIAL SEQUENCES
# =============================================================================
# Some useful predefined character classes:
# \d  - Matches any digit (0-9)
# \D  - Matches any non-digit character
# \s  - Matches any whitespace (space, tab, newline)
# \S  - Matches any non-whitespace character
# \w  - Matches any word character (letters, digits, underscore)
# \W  - Matches any non-word character

# Example 6: Extract all words from a sentence
text = "Welcome to Python 3.10!"
pattern = r"\w+"

words = re.findall(pattern, text)
print("Extracted words:", words)  # Output: ['Welcome', 'to', 'Python', '3', '10']

# Example 7: Replace all digits in a string with '*'
text = "User's password is 12345."
pattern = r"\d"  # Matches any digit

modified_text = re.sub(pattern, "*", text)
print("Modified text:", modified_text)  # Output: User's password is *****.

# =============================================================================
#                           4️⃣ REGEX FOR VALIDATIONS
# =============================================================================
# Regex is commonly used for data validation.

# Example 8: Validate an email address
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

email = "example@mail.com"
print("Is valid email?", validate_email(email))  # Output: True

# Example 9: Validate a phone number (Indian format)
def validate_phone(phone):
    pattern = r"^\+91\d{10}$"  # Matches +91 followed by 10 digits
    return bool(re.match(pattern, phone))

phone = "+919876543210"
print("Is valid phone number?", validate_phone(phone))  # Output: True

# Example 10: Check if a password is strong (min 8 chars, contains digit, uppercase, lowercase)
def is_strong_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
    return bool(re.match(pattern, password))

password = "Secure123"
print("Is strong password?", is_strong_password(password))  # Output: True

# =============================================================================
#                           5️⃣ REGEX FOR FILE PROCESSING
# =============================================================================

# Example 11: Extract all email addresses from a file
def extract_emails_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Example usage: extract_emails_from_file("data.txt")  # Uncomment to use

# Example 12: Find all URLs in a given text
text = "Visit our website at https://www.example.com or follow us at http://facebook.com/page."
pattern = r"https?://[a-zA-Z0-9./_-]+"

urls = re.findall(pattern, text)
print("Extracted URLs:", urls)  
# Output: ['https://www.example.com', 'http://facebook.com/page']

# =============================================================================
#                           🎯 SUMMARY 🎯
# =============================================================================
# ✅ Regex allows efficient text pattern matching and extraction.
# ✅ The `re` module provides `search()`, `match()`, `findall()`, `sub()`, etc.
# ✅ Metacharacters and special sequences make regex powerful.
# ✅ Used for validation (emails, passwords, phone numbers).
# ✅ Useful for extracting information (emails, URLs, numbers).

# =============================================================================
