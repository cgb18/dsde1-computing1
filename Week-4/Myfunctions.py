#---------------Lists--------------

def first_and_last(the_list):
    return (the_list[0], the_list[-1])

def part_reverse(the_list, beginning, end):
    #this raises a value error if the beginning > end or if either the beginning
    #or the end are bigger than the number of elements in the list
    if beginning > end:
        print('You have entered an ending index larger than the beginning index. Please enter again.')
        raise ValueError
    #try:
    #    beginning = int(input('Please reenter a beginning index: '))
        end = int(input('Please reenter an ending index: '))
    if beginning > len(the_list):
        print('You have entered a beginning index larger than the number of elements in the list. Please enter again.')
        raise ValueError
    #try:
    #    beginning = int(input('Please reenter a beginning index: '))
    if end > len(the_list):
        print('You have entered a beginning index larger than the number of elements in the list. Please enter again')
        raise ValueError
    #try:
    #    beginning = int(input('Please reenter an ending index: '))
    
    #this slices the list
    new = the_list[beginning: end]

    #this reverses the list
    new.reverse()
    return (new)

def repeat_at_index(the_list, index):
    #this inserts the index element on the list in the index position 2 times
    for i in range(2):
        the_list.insert(index, the_list[index])
    return the_list

#-------------Strings-------------

def palindrome_word(word):
    #this checks whether the reversed string is equal to the original string
    if word == word[::-1]:
        print('This word is a palindrome.')
    else: 
        print('This word is not a palindrome.')
    return ' '

def palindrome_sentence(sentence):
    import string
    #this turns all of the letters in the string to lowercase
    sentence = sentence.lower()
    #this removes all the punctuation in the string using the imported package
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    #this removes all whitespace throughout the string, as sentence.strip() only removes it from the sides
    sentence = sentence.replace(' ', '')
    #this checks whether the reversed string is equal to the original (after being adjusted)
    if sentence == sentence[::-1]:
        print('This sentence is a palindrome.')
    else: 
        print('This sentence is not a palindrome.')
    return ''
 
def concatenate_sentences(sentence1, sentence2):
    #this removes the whitespace at the start and end of the string
    sentence1 = sentence1.strip(' ')
    sentence2 = sentence2.strip(' ')
    
    #this checks whether the first element of the string is an uppercase letter
    if sentence1[0].isupper() is False: 
        sentence1 = sentence1.replace(sentence1[0],sentence1[0].upper(),1) 
        #this replaces the first element of the string with the upper case version of it
    if sentence2[0].isupper() is False:
        sentence2 = sentence2.replace(sentence2[0],sentence2[0].upper(),1)

    #this checks whether the given suffix is at the end of the string
    if sentence1.endswith('.'):
        sentence1
    elif sentence1.endswith('!'):
        sentence1
    elif sentence1.endswith('?'):
        sentence1
    else:
        sentence1 = sentence1 + input('Please add punctuation at the end of the first sentence: ')
        #this adds a string to the existing one

    if sentence2.endswith('.'):
        sentence2
    elif sentence2.endswith('!'):
        sentence2
    elif sentence2.endswith('?'):
        sentence2
    else:
        sentence2 = sentence2 + input('Please add punctuation at the end of the second sentence: ')
    
    #string addition to concatenate the sentences
    concatenated = sentence1 + ' ' + sentence2

    return concatenated

#----------Dictrionaries----------


def index_exists(dictionary, key):
    #returns false if the given key is in the dictionary
    return bool(key in dictionary.keys())

def value_exists(dictionary, value):
    #returns true if the given value is in the dictionary
    return bool(value in dictionary.values())

def merge_dictionaries(dictionary1, dictionary2):
    merged_dict = {**dictionary1, **dictionary2}
    return merged_dict


#---------Testing functions---------

def other():
    #1 - gives the first and last items of a list
    # this creates a list
    the_list = []
    #asks the user indeces
    indeces = int(input('Please enter the number of elements in your list: '))
    #asks the user to input elements for the list one at a time
    for i in range(0,indeces):
        element1 = int(input('Please enter an integer for element ' + str(i+1) + ': '))
        the_list.append(element1)
    print(first_and_last(the_list))
    
    #2 - reverses the sliced list
    beginning2 = int(input('Please enter a beginning index: '))
    end2 = int(input('Please enter an ending index: '))
    print(part_reverse(the_list, beginning, end))

    #3 - repeats the element at an index 3 times at the place of the index
    index3 = int(input('Please enter the index integer: '))
    print(repeat_at_index(the_list, index3))

    #4 - checks whether a word is a palindrome
    word4 = input('Please enter a word: ')
    print(palindrome_word(word4))

    #5 - checks whether a sentence is a palindrome
    sentence5 = input('Please enter a sentence: ')
    print(palindrome_sentence(sentence5))

    #6 - concatenates sentences and allows to type punctuation + fixes upper case
    sentence1 = input('Please enter a first sentence: ')
    sentence2 = input('Please enter a second sentence: ')
    print(concatenate_sentences(sentence1, sentence2))

    #7 - lets the user create a dictionary + checks whether a given key is present
    dictionary = {}
    n_keys = int(input('Please enter the number of keys in your dictionary: '))
    for i in range(0,n_keys):
        key1 = input('Please enter key ' + str(i+1) + ': ') #inputs the keys one at a time
        item1 = input('Please enter item ' + str(i+1) + ': ') #inputs the items one at a time
        dictionary[key1] = item1 #adds the keys and items to the dictionary
    print(index_exists(dictionary, input('Please type a given key to check if it is present in the dictionary: ')))

    #8 - checks whether a given value is present
    print(value_exists(dictionary, input('Please type a given value to check if it is present in the dictionary: ')))

def main():
    #9 - lets the user create 2 dictionaries and merges all of the values
    dictionary1 = {}
    n_keys1 = int(input('Please enter the number of keys in your first dictionary: '))
    for i in range(0,n_keys1):
        key1 = input('Please enter key ' + str(i+1) + ': ')
        item1 = input('Please enter item ' + str(i+1) + ': ')
        dictionary1[key1] = item1
    
    dictionary2 = {}
    n_keys2 = int(input('Please enter the number of keys in your second dictionary: '))
    for i in range(0,n_keys2):
        key1_2 = input('Please enter key ' + str(i+1) + ': ')
        item1_2 = input('Please enter item ' + str(i+1) + ': ')
        dictionary2[key1_2] = item1_2
    print(merge_dictionaries(dictionary1, dictionary2))

if __name__ == '__main__':
    main()