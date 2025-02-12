# Program to check if a number is positive, negative, or zero

# Taking input from the user
num = float(input("Enter a number: "))

# Checking if the number is positive
if num > 0:
    print("num is a positive number.")
# Checking if the number is negative
elif num < 0:
    print("num is a negative number.")
# If the number is neither positive nor negative, it must be zero
else:
    print("num is zero.")
