# String Methods Demo in Python

# Define a string with leading and trailing spaces
college = "     Sri Krishna Arts and science college in coimbatore and entertaining   "

# Print the original string (with spaces)
print(college)

# Convert the string to all uppercase letters
print(college.upper())

# Convert the string to all lowercase letters
print(college.lower())

# Capitalize the first letter of every word
print(college.title())

# Remove leading and trailing whitespace
print(college.strip())

# Find the position of the first occurrence of the substring "and"
# Returns the index if found, or -1 if not found
print(college.find("and"))

# Find the index of the substring "Sri" (case-sensitive)
print(college.find("Sri"))

# Try to find a substring that doesn't exist in the string
# This will return -1 since "siddhaarth" is not in the string
print(college.find("siddhaarth"))

# Slice the string starting from index 7 to the end
# This skips the first few spaces and part of "Sri"
print(college[7:])

# Replace all occurrences of the letter "i" with "lol"
print(college.replace("i", "lol"))

# Count how many times the letter "i" appears in the string
print(college.count("i"))

# Check if the substring "jaj" is present in the string (returns True/False)
print("jaj" in college)

# Case-sensitive check: this will return False
print("sri" in college)

# Case-sensitive check: this will return True
print("Sri" in college)

# Check if "siddharth" is NOT in the string (returns True/False)
print("siddharth" not in college)
