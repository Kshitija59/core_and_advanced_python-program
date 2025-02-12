# Program to find the largest among three numbers

# Taking three numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Comparing the numbers to find the largest
if num1 >= num2 and num1 >= num3:
    # If num1 is greater than or equal to both num2 and num3
    print("The largest number is num1.")
elif num2 >= num1 and num2 >= num3:
    # If num2 is greater than or equal to both num1 and num3
    print("The largest number is num2.")
else:
    # If num3 is greater than or equal to both num1 and num2
    print("The largest number is num3.")
