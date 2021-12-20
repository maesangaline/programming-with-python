# Chapter 6
# Exercise 3


def main():
    # Input the file name
    file = input('Enter a file name: ')
    objFile = open(file, 'r')
    line = objFile.readline()
    line = line.rstrip('\n')
    # Number starts at one
    lineNum = 1
    # Read the file
    while line != '':
        # Print the file name preceded with a line number then :
        print(lineNum, ':', line, sep='')
        line = objFile.readline()
        line = line.rstrip('\n')
        # Increase the number
        lineNum += 1
    # Close the file
    objFile.close()
# Call the main function
main()
