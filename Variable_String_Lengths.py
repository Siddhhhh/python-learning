# Define string variables
siddhaarth = "College Student"      # Represents your role
madhan = "College Friend"           # Represents your friend's role

# Print the length (number of characters) of each string
print(len(siddhaarth))              # Output: 15 (including space)
print(len(madhan))                  # Output: 14 (including space)

# Print the full values of each variable
print(siddhaarth)                   # Output: College Student
print(madhan)                       # Output: College Friend

# String slicing examples

# Print characters from index 0 to 5 (6 characters total)
print(siddhaarth[0:6])              # Output: Colleg

# Print characters from index 7 to 8 in 'madhan'
print(madhan[7:9])                  # Output: Fr

# Print characters from beginning to index 13
print(siddhaarth[:14])             # Output: College Studen

# Print characters from beginning to index 20 (no error even if it's longer than actual string)
print(madhan[:21])                 # Output: College Friend
