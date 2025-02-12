# Program to check if a year is a leap year or not

# Taking input from the user
year = int(input("Enter a year: "))

# Checking if the year is divisible by 400, it's a leap year
if (year % 400 == 0):
    print("year} is a leap year.")
# Checking if the year is divisible by 100 but not by 400, it's not a leap year
elif (year % 100 == 0):
    print("year is not a leap year.")
# Checking if the year is divisible by 4 but not by 100, it's a leap year
elif (year % 4 == 0):
    print("year is a leap year.")
# If none of the conditions are true, it's not a leap year
else:
    print("year is not a leap year.")
