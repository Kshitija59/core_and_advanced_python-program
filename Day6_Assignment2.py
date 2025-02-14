# Python program to check whether a number is palindrome or not

# Take input from the user
num = int(input("Enter a number: "))

# Store the original number to compare later
original_num = num

# Initialize the variable to store the reversed number
reversed_num = 0

# Reverse the number using a while loop
while num != 0:
    # Get the last digit of the number
    digit = num % 10
    # Add the digit to the reversed number
    reversed_num = reversed_num * 10 + digit
    # Remove the last digit from the original number
    num = num // 10

# Check if the original number is equal to the reversed number
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

#output
"Enter a number: 121"
"The number is a palindrome."
    
    

