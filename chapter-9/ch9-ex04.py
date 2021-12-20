# Chapter 9
# Exercise 4

# Define the main function
def main():
    file = input('Enter a file name: ')
    objFile = open(file, 'r')
    unique_words = set()
    for i in objFile:
        i = i.rstrip('\n')
        if i not in unique_words:
            unique_words.add(i)
    print(unique_words)

main()
