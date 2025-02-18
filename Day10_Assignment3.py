# Define a list with some duplicate values
numbers = [1, 2, 3, 4, 5, 6, 2, 3, 7, 8, 9, 5]

# Create an empty list to store duplicate values
duplicates = []

# Loop through the list to find duplicates
for i in range(len(numbers)):
    # Check if the number is repeated and not already in the duplicates list
    if numbers[i] in numbers[i+1:] and numbers[i] not in duplicates:
        duplicates.append(numbers[i])

# Print the duplicate values
print("Duplicate values in the list are:", duplicates)

""" Output
Duplicate values in the list are: [2, 3, 5]
"""
