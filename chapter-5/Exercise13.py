# Marcie Sangaline
# CPT 156 Programming with Python
# Chapter 5, Exercise 13

# Creates a function with the falling_time parameter
def falling_distance(falling_time):
    # Calculate the falling disance
    gravity = 9.8
    distance = (1 / 2) * gravity * (falling_time **2)
    return distance

# Create a loop that accepts 10 falling scenarios
def  main():
    # Create a table to display the time and distance
    print('Time \t Falling Distance \t')
    for x in range(1, 11):
        # Print the 10 results, formatting 2 decimal places
        print(x, '\t', format(falling_distance(x), '.2f'))

# Run the function
main()
