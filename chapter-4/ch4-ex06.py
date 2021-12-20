# Chapter 4
# Exercise 6

# Prints celsius and fahrenheit then does 20 calculations
print('Celsius', 'Fahrenheit')
print('-'*20)

# for loop that calculates from 0-20 using the formula to convert F to C
for c in range(21):
    print(format(c),'\t', format(9 / 5 * c + 32))
