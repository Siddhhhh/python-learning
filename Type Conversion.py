# Program: Basic Input & Arithmetic Operations in Python

# --- First operation: Add 1 to user input
x = input("x: ")
y = int(x) + 1
print("x:", x, "y:", y)  # Shows original and incremented values

# --- Second operation: Subtract 6 from input
x = input("x: ")
y = int(x) - 6
print("x:", x, "y:", y)

# --- Third operation: Multiply, divide, and cube the input
x = input("x: ")
y = int(x) * 2       # Multiply by 2
z = int(x) / 2       # Divide by 2
o = int(x) ** 3      # Cube the number
print("x:", y, z, o)

# --- Fourth operation: Multiple calculations on the same input
a = input("a: ")

b = int(a) * 2       # Multiply by 2
c = int(a) - 6       # Subtract 6
d = int(a) / 2       # Divide by 2
e = int(a) ** 3      # Cube the number
f = int(a) // 3      # Floor division by 3
g = int(a) % 2       # Modulo (remainder) when divided by 2
q = int(a) + 1       # Increment by 1

# Print all calculated values
print("a:", a, b, c, d, e, f, g)
