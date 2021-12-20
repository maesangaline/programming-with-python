# Chapter 9
# Exercise 4

# Define the main function
def main():
    # Prompts the user to input the file name (text.txt)
    file = input('Enter a file name: ')
    # Open the file and read
    objFile = open(file, 'r')
    # Stores all unique words in a set
    unique_words = set()
    # Parses through the file for unique words
    for i in objFile:
        # Stores the unique word
        i = i.rstrip('\n')
        if i not in unique_words:
            unique_words.add(i)
    # Prints all of the unique words       
    print(unique_words)

main()
