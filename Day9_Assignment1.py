# Input string
input_str = "P@#yn26at^&i5ve"

# Initialize counters for letters, digits, and symbols
chars = 0
digits = 0
symbols = 0

# Loop through each character in the input string
for char in input_str:
    if char.isalpha():  # Check if the character is a letter
        chars += 1
    elif char.isdigit():  # Check if the character is a digit
        digits += 1
    else:  # If it's neither a letter nor a digit, it's a symbol
        symbols += 1

# Print the results
print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)

#OUTPUT
"""Chars = 8
Digits = 3
Symbols = 4"""


