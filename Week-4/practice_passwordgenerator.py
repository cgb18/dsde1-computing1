'''
Random password generator
'''

import string
import random

def password(length):
    '''
    This is a random password generator which allows you to choose the length of the desired
    password, and uses uppercase, lowercase, digits and characters from the string library.
    '''
    # string.printable is a string containing lowercase, uppercase, digits and
    # all the main punctuation characters.
    # random.sample returns a length l of unique elements chosen from the chosen
    # population, in this case the string.printable population.
    # Return the newly randomly generated password.
    return ''.join(random.sample(string.printable, length))

L = int(input('Please enter the length of your desired password:'))
print('Your randomly generated password of length ' + str(L) + ' is: ' + password(L))
