# Define a list of numbers
numbers = [34, 12, 98, 7, 56, 21]

# Initialize variables to store the largest and smallest numbers
# Start with the first number in the list as both largest and smallest
largest = numbers[0]
smallest = numbers[0]

# Loop through each number in the list
for num in numbers:
    # If the current number is larger than the largest, update largest
    if num > largest:
        largest = num
    # If the current number is smaller than the smallest, update smallest
    if num < smallest:
        smallest = num

# Print the largest and smallest numbers
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)


"""
Output
The largest number in the list is: 98
The smallest number in the list is: 7
"""
