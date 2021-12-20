# Chapter 5
# Exercise 3

# Input that asks for replacement cost
cost = float(input('Enter the replacement cost of the building: '))

def calculate(cost):
    # Calculate 80% of the value
    insurance = cost * 0.8

    # Print the calculation for min insurance
    print('The minimum amount of insurnace that should be purchased is $', format(insurance, '.2f'))


# Call the function
calculate(cost)
