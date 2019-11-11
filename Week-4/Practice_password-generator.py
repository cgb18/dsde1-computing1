import string
import random

def password(l):
    ''' This is a random password generator which allows you to choose the length 
    of the desired password, and uses uppercase, lowercase, digits and characters
    from the string library. '''
    
    # string.printable is a string containing lowercase, uppercase, digits and
    # all the main punctuation characters.
    # random.sample returns a length l of unique elements chosen from the chosen
    # population, in this case the string.printable population.

    pw = ''.join(random.sample(string.printable,l))

    # Return the newly randomly generated password.
    return pw

l = int(input('Please enter the length of your desired password:'))
print('Your randomly generated password of length ' + str(l) + ' is: ' + password(l))