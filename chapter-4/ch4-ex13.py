# Chapter 4
# Exercise 13


# Input starting number of organisms
startingnumber = int(input('Enter the starting number of organisms '))
# Input the daily increase
dailyincrease = int(input('Enter the daily population increase ' ))
# Input the number of days left to multiply
days = int(input('Enter the number of days left to multiply '))

# Print the day approx and population, tabbed
print('Day Approximate\t', 'Population')

# For loop that uses the number of days then calculates the population increase by the percent of increase.
for x in range(1, days + 1):
    print(x, '\t', '\t', startingnumber)
    startingnumber += startingnumber * dailyincrease / 100
