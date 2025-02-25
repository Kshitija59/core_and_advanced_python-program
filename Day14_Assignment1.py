'''Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.'''
try:
    # Taking user input for the numerator and denominator
    num1 = float(input("Enter the num1: "))
    num2 = float(input("Enter the num2: "))

    # Trying to perform division
    result = num1 / num2
    print("The result is:", result)

except ZeroDivisionError:
    # Handling the division by zero error
    print("Error: Cannot divide by zero!")




#OUTPUT
'''Enter the num1: 23
Enter the num2: 10
The result is: 2.3

Enter the num1: 20
Enter the num2: 5
The result is: 4.0'''

