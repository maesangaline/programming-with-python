# Chapter 3
# Exercise 17

# Create response
response = ''

#Print the first statement
print('Reboot the computer and try to connect.')

#Did it work? Enter yes/no.
response = input('Did that fix the problem? Enter yes or no. ')

# If / else statements requesting yes/no. Yes ends dialog. No proceeds to further inquiries.
if response == 'yes':
    print('Great!')
elif response == 'no':
    print('Reboot the router and try to connect again.')
    response = input('Did that fix the problem?' )
    if response == 'yes':
        print('Great!')
    elif response == 'no':
        print('Make sure that cables between the router & modem are plugged in firmly.')
        response = input('Did that fix the problem?' )
        if response == 'yes':
            print('Great!')
        elif response == 'no':
            print('Move the router to a new location and try to connect.')
            response = input('Did that fix the problem?' )
            if response == 'yes':
                print('Great!')
            elif response == 'no':
                print('Get a new router.')
