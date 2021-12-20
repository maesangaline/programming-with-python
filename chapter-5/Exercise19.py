# Marcie Sangaline
# CPT 156 Programming with Python
# Chapter 5, Exercise 19

# Enter the present value
presentValue = float(input('Enter the current account value: $'))
# Enter the interest rate
interestRate = float(input('Enter the monthly interest rate: '))
# Enter the number of months
numMonths = int(input('Enter the number of months: '))


# Calculation for future value
def calculate(presentValue, interestRate, numMonths):
    # future value = present value x (1 + interest rate) ** months
    f = presentValue * ((1 + interestRate / 100) ** numMonths)
    # Print the future value in 2 decimal places
    print('The account will have a future value of: $', format(f, '.2f'))

calculate(presentValue, interestRate, numMonths)
