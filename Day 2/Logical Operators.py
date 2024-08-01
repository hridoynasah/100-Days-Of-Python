# Define some boolean variables
a = True
b = False

# Logical AND
result_and = a and b
print(f"a and b: {result_and}")  # Output: False (because b is False)

# Logical OR
result_or = a or b
print(f"a or b: {result_or}")   # Output: True (because a is True)

# Logical NOT
result_not_a = not a
result_not_b = not b
print(f"not a: {result_not_a}") # Output: False (because a is True)
print(f"not b: {result_not_b}") # Output: True (because b is False)

# Combining logical operators
result_combined = (a and not b) or (not a and b)
print(f"(a and not b) or (not a and b): {result_combined}")  # Output: True
