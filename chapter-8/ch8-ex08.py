# Chapter 8
# Exercise 8

# User inputs the sentence
sentence = input('Enter a sentence with all lowercase letters: ')

# Define the main function
def main(sentence):
    # Split the sentence
    sentenceList = sentence.split(' ')
    newSentence = ''
    # For loop to create uppercase letters
    for i in sentenceList:
        n = i[0].upper()
        new = i.replace(i[0], n)
        space = ' '
        newSentence += new + space
    # Prints the new sentence with uppercase
    print(newSentence)
# Run the main function
main(sentence)
