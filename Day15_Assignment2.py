#Write a function in Python to count and display the total number of words in a text file “ABC.txt”
def count_words_in_file(filename):
    try:
        total_words = 0  # Initialize a counter for words
        
        # Open the file in read mode
        with open(filename, 'r') as file:
            for line in file:
                # Split each line into words and count them
                words = line.split()  # This will split by any whitespace
                total_words += len(words)  # Add the number of words in this line
        
        # Display the total word count
        print(f"Total number of words in the file: {total_words}")
    
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the file name
count_words_in_file("ABC.txt")

'''OUTPUT
Total number of words in the file: 15'''
