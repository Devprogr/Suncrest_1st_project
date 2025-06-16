a = input("Enter the first number: ")   # Example: "10"
b = input("Enter the second number: ")  # Example: "5"

# Convert input strings to integers so we can do math
a = int(a)
b = int(b)

# Addition
add_result = a + b
print("Addition:", add_result)

# Subtraction
sub_result = a - b
print("Subtraction:", sub_result)

# Multiplication
mul_result = a * b
print("Multiplication:", mul_result)

# Division (returns float)
div_result = a / b
print("Division:", div_result)

# Extra: Floor Division (whole number)
floor_div = a // b
print("Floor Division:", floor_div)

# Extra: Modulus (remainder)
remainder = a % b
print("Remainder:", remainder)