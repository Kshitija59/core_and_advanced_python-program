# Python program to find the factorial of a number using a while loop

# Take input from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the factorial, starting from 1
factorial = 1

# Initialize a variable to control the while loop
i = 1

# Use a while loop to calculate the factorial
while i <= num:
    factorial *= i  # Multiply the current factorial by the current number (i)
    i += 1  # Increment i by 1 in each iteration

# Output: Print the calculated factorial
print(f"The factorial of {num} is {factorial}")

#Output
"Enter a number: 5"
"The factorial of 5 is 120"
