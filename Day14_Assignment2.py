'''Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer'''

# Program to handle ValueError for invalid integer input

try:
    # Prompt the user to input an integer
    user_input = input("Enter an integer: ")

    # Try converting the input to an integer
    user_input = int(user_input)

    print(f"The integer you entered is: {user_input}")

except ValueError:
    # Handling ValueError if the input is not a valid integer
    print("Error: That's not a valid integer!")


'''OUTPUT:
Enter an integer: 24
The integer you entered is: 24

Enter an integer: 12.3
Error: That's not a valid integer!'''


