# Python program to reverse a number using a while loop

# Take input from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the reversed number
reversed_num = 0

# Use a while loop to reverse the number
while num > 0:
    # Extract the last digit of the number
    digit = num % 10
    
    # Add the digit to the reversed number
    reversed_num = reversed_num * 10 + digit
    
    # Remove the last digit from the original number
    num = num // 10

# Output: Print the reversed number
print("Reversed number:", reversed_num)


"""
Enter a number: 12345
Reversed number: 54321
"""
