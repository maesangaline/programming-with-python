# Marcie Sangaline
# CPT 156 Programming with Python
# Chapter 8, Exercise 1

# Define the main function
def main():
    # Input first, middle and last name
    first = input('Enter your first name. ')
    middle = input('Enter your middle name. ')
    last = input('Enter your last name. ')
    # Print the initials
    print(first[0].upper(), '.', middle[0].upper(), '.', last[0].upper(), '.', sep='')
# Runs the main function
main()
