# Marcie Sangaline
# CPT 156 Programming with Python
# Chapter 8, Exercise 2

# Define the main function
def main():
    # Input the numbers 
    numbers = input('Enter numbers with no spaces: ')
    # Define total
    total = 0
    # Add the numbers together
    for i in numbers:
        total += int(i)
    # Print the total
    print(total)
# Run the main function
main()
