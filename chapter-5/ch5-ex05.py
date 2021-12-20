# Chapter 5
# Exercise 5

# Input the value of the property
value = float(input('Enter the value of the property: $'))
def assessment(value):
    tax = value * 0.6 * 0.72 / 100
    print('$', format(tax, '.2f'), sep='')

assessment(value)

