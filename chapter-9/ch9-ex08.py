# Chapter 9
# Exercise 8

# Imports pickle
import pickle

# Function that opens the file
def open_file():
    output_file = open('emails.dat', 'wb')
    return output_file

# Defines the email list
def make_email_list():
    email_list = {}
    validation = 'y'
    # Prompts user to input a name and email address
    while validation == 'y':
        name = input('Enter a name to add to the email list: ')
        email = input('Enter an email address: ')
        name = name.lower()
        email = email.lower()
        email_list[name] = email
        validation = input('Enter Y to continue: ')
        validation = validation.lower()
    print(email_list)
    return email_list

# Defines the menu function. User can choose whether to
# Look up, add, change, or delete information that has been input
def menu(email_list):
    validation = 'y'
    while validation == 'y':
        select_menu = input('Enter "Look up", "Add", "Change" or "Delete": '
                            'If nothing to do, enter N: ')
        select_menu = select_menu.lower()
        if select_menu == 'look up':
            email_list = look_up(email_list)

        elif select_menu == 'add':
            email_list = add(email_list)

        elif select_menu == 'change':
            email_list = change(email_list)

        elif select_menu == 'delete':
            email_list = delete(email_list)
        # Ends the validation process
        elif select_menu == 'n':
            print('Complete!')
            validation = 'n'

# Function to loop through the names and email addresses
def look_up(email_list):
    name = input('Enter a name (in lowercase) to look up an email address: ')
    name = name.lower()
    print(email_list[name])
    return email_list

# Function to add an email address
def add(email_list):
    name = input('Enter a name (in lowercase) to add an email address: ')
    email = input('Enter an email address: ')
    name = name.lower()
    email = email.lower()
    email_list[name] = email    
    return email_list

# Function to change something in the email list
def change(email_list):
    name = input('Enter a name (in lowercase) to change the email address: ')
    name = name.lower()
    print(email_list[name])
    validation = input('Enter Y to change this address: ')
    validation = validation.lower()
    if validation == 'Y':
        email = input('Enter the email address: ')
        email = email.lower()
        email_list[name] = email    
    return email_list

# Function to delete an entry
def delete(email_list):
    name = input('Enter a name (in lowercase) to delete an email address: ')
    name = name.lower()
    print(email_list[name])
    validation = input('Enter Y to delete this address: ')
    validation = validation.lower()
    if validation == 'Y':
        del email_list[name]
    return email_list

# Runs the functions
output_file = open_file()
email_list = make_email_list()
menu(email_list)
pickle.dump(email_list, output_file)
output_file.close()

