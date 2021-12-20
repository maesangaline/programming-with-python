# Chapter 8
# Exercise 7

# Define the main function
def main():
    # Open and read the file
    objFile = open('text.txt' , 'r')
    textList = []
    for line in objFile:
        # Strip the spaces
        line = line.rstrip('/n')
        mylist = line
        # Create a list
        textList.append(mylist)

    # Print the results
    print('The number of uppercase letters in the file is: ')
    totalUpCaLetters = countUpperCase(textList)
    print(totalUpCaLetters)
    print()
    print('The number of lowercase letters in the file is: ')
    totalLoCaLetters = countLowerCase(textList)
    print(totalLoCaLetters)
    print()
    print('The number of digits in the file is: ')
    totalDigits = countDigits(textList)
    print(totalDigits)
    print()
    print('The number of whitespaces in the file is: ')
    totalWhiteSpaces = countWhiteSpace(textList)
    print(totalWhiteSpaces)
    
# Define the uppercase function        
def countUpperCase(anyList):
    count = 0
    # For loop to locate uppercase letters and store them into a list
    for row in range(len(anyList)):
        for i in range(len(anyList[row])):
            if anyList[row][i].isupper():
                count+= 1
    return count

# Define the lowercase function
def countLowerCase(anyList):
    count = 0
    # FOr loop to locate lowercase letters and store them into a list
    for row in range(len(anyList)):
        for i in range(len(anyList[row])):
            if anyList[row][i].islower():
                count+= 1
    return count

# Define the digits function
def countDigits(anyList):
    count = 0
    # For loop to locate digits and store them into a list
    for row in range(len(anyList)):
        for i in range(len(anyList[row])):
            if anyList[row][i].isdigit():
                count+= 1
    return count

# Define the white space function
def countWhiteSpace(anyList):
    count = 0
    # For loop to locate the white spaces remaining and store them into a list
    for row in range(len(anyList)):
        for i in range(len(anyList[row])):
            if anyList[row][i].isspace():
                count+= 1
    return count

# Run the main function
main()
