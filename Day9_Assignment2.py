# Input string
input_str = "String and String Function"

# Initialize an empty string to store the result
result = ""

# Loop through each character in the input string
for char in input_str:
    # If the character is not already in the result string, add it
    if char not in result:
        result += char

# Print the result
print(result)

#OUTPUT
"""String and Function"""
