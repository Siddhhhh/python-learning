# Define three name parts
first_name = "vijay"
second_name = "malaya"
third_name = "Not Chor"

# Print the names directly using print()
# The result of print() is None, which is stored in 'full'
full = print(first_name, second_name, third_name)  # This prints the names, but assigns None to 'full'

# Concatenate two other name parts
start_name = "madhan"
last_name = "kumar"

# Combine start and last names without space
full_name = start_name + "" + last_name
print(full_name)  # Output: madhankumar

# Combine using f-string formatting
first = "Siddhaarth"
last = "Chandran"

# Correctly formatted full name using f-string
fully = f"{first} {last}"

# Store length of start_name along with last_name in a string
full_name = f"{len(start_name)} {last_name}"

print(fully)       # Output: Siddhaarth Chandran
print(full_name)   # Output: 6 kumar (since 'madhan' has 6 letters)
print(first[0:7])  # Output: Siddhaa (first 7 letters of 'Siddhaarth')
print(full)        # Output: None (because 'full' was assigned the result of print())
