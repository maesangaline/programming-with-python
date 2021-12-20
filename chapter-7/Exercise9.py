# Marcie Sangaline
# CPT 156 Programming with Python
# Chapter 7, Exercise 9

# Define the main function
def main():
  # Declare Variables
  counter = 0
  increaseYear = 0
  maxYear = 0
  maxYearPosition = 0
  minYear = 0
  minYearPosition = 0
  averagePeriod = 0

  # Create lists
  listNumbers = []
  listNumberAverage =[]
  # Generate a list for the years
  listYears = [i for i in range(1950,1991)]

  #Try and Except
  try:
    # Open USPopulation file
    objFile = open('USPopulation.txt', 'r')

    # Count the number of lines with values
    for i in objFile:
      counter = counter + 1

    # Set the listNumbers size
    for j in range(counter):
      listNumbers.append(0)

    # Go back to the beggining of the file
    objFile.seek(0)
    
    # Read each line
    for k in range(counter):
      listNumbers[k] = int(objFile.readline())
      minYear = listNumbers[0]

    # Calculate the average and find min and max
    for l in range(0, counter, +1):
      if (l+1) == counter:
        break
      
      # Calculate average years
      increaseYear = (listNumbers[l+1] - listNumbers[l])/2
      
      # Saves the largest number
      if increaseYear > maxYear:
        maxYear = increaseYear
        maxYearPosition = l+1

      # Saves the smallest number
      if minYear > increaseYear:
        minYear = increaseYear
        minYearPosition = l+1
    
    # Calculate the average
    averagePeriod = (listNumbers[counter-1] - listNumbers[0])/(counter-1)

    # Print  change, highest, and lowest numbers
    print("The average annual change in population was:", '{0:,.2f}'.format(averagePeriod, ".2f"))
    print("The year with the highest increase in population was", listYears[maxYearPosition])
    print("The year with the smallest increase in population was", listYears[minYearPosition])

    objFile.close()

  # Errors
  except FileNotFoundError:
    print("File does not exist")
  except IndexError as error:
    print("Index Invalid")
  except Exception as exception:
    print("Something is wrong")

# Call main function
main()
