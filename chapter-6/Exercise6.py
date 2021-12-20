# Marcie Sangaline
# CPT 156 Programming with Python
# Chapter 6, Exercise 6


def main():
    # Open the file name
    objFile = open('numbers.txt', 'r')
    # Define the variables
    count = 0
    total = 0
    # Reads the file
    for i in objFile:
        total += int(i)
        count += 1
    # Calculate and print the average of the numbers in the file
    print(total / count)
    # Close the file
    objFile.close()
# Call the main function
main()
