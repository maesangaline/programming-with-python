# Marcie Sangaline
# CPT 156 Programming with Python
# Chapter 8, Exercise 10

# Define the function to convert the string and store them
def storeString(string):
    d = dict()
    for x in string:
        if not d.get(x):
            d[x] = 1
        else:
            d[x] += 1
    return d

# Define the main function
def main():
    string = input("Enter sentence: ").lower()
    maxKey = 0
    maxVal = 0
    d = storeString(string)
    # For loop to find each string
    for x in d.keys():
        if(maxVal < d[x]):
            maxVal = d[x]
            maxKey = x
    print("Most frequent character =",maxKey)

# Run the main function
main()
