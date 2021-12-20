# Chapter 3
# Exercise 5

# Input the mass of the object
mass = float(input('Please enter the object\'s mass: '))

# Weight calculation
weight = mass * 9.8

# Determine if the object is too heavy
if weight > 500:
    print('The object is too heavy.')
# Determine if the object is too light
elif weight < 100:
    print('The object is too light.')
# Gives the weight if not too heavy or too light
else:
    print(weight)
