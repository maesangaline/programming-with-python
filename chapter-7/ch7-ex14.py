# Chapter 7
# Exercise 14

# Import matplotlib
from matplotlib import pyplot as plt

# Create the lists
expense = ['1000', '150', '200', '50', '300', '350']
category = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']

# Open/Create the file
monthlyChart = open('expense.txt', 'r+')
# Write the lists
monthlyChart.writelines(category)
monthlyChart.writelines(expense)
monthlyChart.readlines()
monthlyChart.readlines()
# Plot the pie chart
plt.pie(expense, labels = category, starangel = 90, autopct = '%.1f%%')
plt.title('Monthly Expenses')
plt.show()
# Close
monthlyChart.close()
