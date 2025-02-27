# Assignemnt -Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen

with open("ABC.txt", "w") as file:
    file.write("This is the first line of the file.\n")
    file.write("This is the second line of the file.\n")
    file.write("This is the third line of the file.\n")


    
def read_file_and_display(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Loop through each line in the file and print it
            for line in file:
                print(line.strip())  # .strip() removes the newline character at the end of the line
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the file name
read_file_and_display("ABC.txt")

'''output
This is the first line of the file.
This is the second line of the file.
This is the third line of the file.'''
