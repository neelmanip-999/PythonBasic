# ==============================================================
#                  STRING EXERCISES SOLUTIONS
# ==============================================================
# This Python script contains solutions to 5 different string-related exercises.
# Each exercise is solved step by step with proper comments and explanations.

# ==============================================================
#                    1️⃣ REVERSE A STRING
# ==============================================================
# Take a string input from the user and print it in reverse.

# Taking user input
user_string = input("Enter a string: ")  

# Reversing the string using slicing
reversed_string = user_string[::-1]

# Displaying the reversed string
print("Reversed String:", reversed_string)


# ==============================================================
#        2️⃣ CONVERT A STRING TO UPPERCASE WITHOUT upper()
# ==============================================================
# We convert a lowercase string to uppercase without using the built-in upper() method.

# Taking user input
lowercase_string = input("Enter a lowercase string: ")  

# Manual conversion using ASCII values
uppercase_string = ""

for char in lowercase_string:
    # If the character is a lowercase letter (a-z), convert it to uppercase (A-Z)
    if 'a' <= char <= 'z':
        uppercase_string += chr(ord(char) - 32)  # Convert ASCII value
    else:
        uppercase_string += char  # Keep non-lowercase characters unchanged

# Displaying the manually converted uppercase string
print("Uppercase String:", uppercase_string)


# ==============================================================
#        3️⃣ EXTRACT DOMAIN NAME FROM EMAIL ADDRESS
# ==============================================================
# Extracting the domain name from an email address.

# Taking user input
email = input("Enter an email address: ")  

# Finding the index of '@' symbol
at_index = email.find("@")  

# Extracting the domain by slicing from '@' onward
domain = email[at_index+1:]  

# Displaying the extracted domain
print("Domain Name:", domain)


# ==============================================================
#            4️⃣ COUNT THE NUMBER OF VOWELS IN A STRING
# ==============================================================
# This program counts the number of vowels (a, e, i, o, u) in a given string.

# Taking user input
text = input("Enter a string to count vowels: ")  

# Defining a set of vowels
vowels = "aeiouAEIOU"

# Counting vowels using a loop
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1

# Displaying the count of vowels
print("Number of vowels:", vowel_count)


# ==============================================================
#       5️⃣ REPLACE ALL SPACES IN A STRING WITH UNDERSCORES
# ==============================================================
# This program replaces all spaces in a string with underscores.

# Taking user input
string_with_spaces = input("Enter a string with spaces: ")  

# Replacing spaces with underscores
string_with_underscores = string_with_spaces.replace(" ", "_")

# Displaying the modified string
print("Modified String:", string_with_underscores)


# ==============================================================
#                     🎯 PROGRAM SUMMARY 🎯
# ==============================================================
# ✅ We took a string input and printed it in reverse.
# ✅ We converted a lowercase string to uppercase manually without using upper().
# ✅ We extracted the domain name from an email address.
# ✅ We counted the number of vowels in a given string.
# ✅ We replaced all spaces in a string with underscores.
# ==============================================================

