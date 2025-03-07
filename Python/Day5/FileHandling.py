# =============================================================================
#                     📌 EVERYTHING ABOUT FILE HANDLING IN PYTHON
# =============================================================================
# ✅ Python allows file operations such as reading, writing, and appending.
# ✅ The built-in `open()` function is used to open files.
# ✅ Modes:
#    - "r" → Read (default)
#    - "w" → Write (creates a new file if not exists)
#    - "a" → Append (adds content without removing existing data)
#    - "rb" / "wb" → Read/Write Binary files
#    - "r+" / "w+" → Read & Write
# =============================================================================

# -----------------------------------------------------------------------------
# 📌 1️⃣ READING A TEXT FILE
# -----------------------------------------------------------------------------

try:
    with open("sample.txt", "r") as file:  # Opens file in read mode
        content = file.read()  # Reads entire file
        print("📂 File Content:\n", content)
except FileNotFoundError:
    print("⚠️ Error: File not found!")

# -----------------------------------------------------------------------------
# 📌 2️⃣ WRITING TO A TEXT FILE (Overwrites existing content)
# -----------------------------------------------------------------------------

with open("sample.txt", "w") as file:
    file.write("Hello, this is a new file!\n")  # Writing text to file
    file.write("Python file handling is easy.\n")  # Writing multiple lines

print("✅ File written successfully!")

# -----------------------------------------------------------------------------
# 📌 3️⃣ APPENDING DATA TO AN EXISTING FILE (Keeps previous content)
# -----------------------------------------------------------------------------

with open("sample.txt", "a") as file:
    file.write("Appending new content to the file.\n")

print("✅ Data appended successfully!")

# -----------------------------------------------------------------------------
# 📌 4️⃣ READING A FILE LINE BY LINE
# -----------------------------------------------------------------------------

with open("sample.txt", "r") as file:
    print("📂 Reading file line by line:")
    for line in file:
        print(line.strip())  # Removes extra spaces and prints each line

# -----------------------------------------------------------------------------
# 📌 5️⃣ HANDLING CSV FILES
# -----------------------------------------------------------------------------

import csv

# Reading from a CSV file
try:
    with open("data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)  # Reading CSV
        for row in reader:
            print(row)  # Each row is a list
except FileNotFoundError:
    print("⚠️ CSV file not found!")

# Writing to a CSV file
with open("new_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Age", "City"])  # Writing header
    writer.writerow(["David", 28, "Seattle"])  # Writing data
    writer.writerow(["Emma", 24, "Boston"])

print("✅ CSV file written successfully!")

# -----------------------------------------------------------------------------
# 📌 6️⃣ HANDLING JSON FILES
# -----------------------------------------------------------------------------

import json

# Reading from a JSON file
try:
    with open("data.json", "r") as json_file:
        json_data = json.load(json_file)  # Load JSON data
        print("📂 JSON Data:", json_data)
except FileNotFoundError:
    print("⚠️ JSON file not found!")

# Writing to a JSON file
new_data = [
    {"name": "Eve", "age": 27, "city": "San Francisco"},
    {"name": "Frank", "age": 32, "city": "Denver"}
]

with open("new_data.json", "w") as json_file:
    json.dump(new_data, json_file, indent=4)  # Writing JSON data with indentation

print("✅ JSON file written successfully!")

# -----------------------------------------------------------------------------
# 📌 7️⃣ EXCEPTION HANDLING IN FILE OPERATIONS
# -----------------------------------------------------------------------------

try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())  # Trying to read a missing file
except FileNotFoundError:
    print("⚠️ Error: File does not exist!")
except Exception as e:
    print(f"⚠️ Unexpected Error: {e}")

# =============================================================================
#                            🎯 SUMMARY 🎯
# =============================================================================
# ✅ `open()` is used for file operations.
# ✅ Use `"r"` for reading, `"w"` for writing, and `"a"` for appending.
# ✅ Use `csv.reader()` and `csv.writer()` for CSV handling.
# ✅ Use `json.load()` and `json.dump()` for JSON handling.
# ✅ Always use `with open()` to prevent file leaks.
# =============================================================================
