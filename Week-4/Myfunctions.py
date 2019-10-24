def first_and_last(the_list):
    return (the_list[0], the_list[-1])

def part_reverse(the_list, beginning, end):
    if beginning > end:
        print('You have entered an ending index larger than the beginning index. Please enter again.')
        raise ValueError
    if beginning > len(the_list):
        print('You have entered a beginning index larger than the number of elements in the list. Please enter again.')
        raise ValueError
    if end > len(the_list):
        print('You have entered a beginning index larger than the number of elements in the list. Please enter again')
        raise ValueError
    new = the_list[beginning: end]
    new.reverse()
    return (new)

def repeat_at_index(the_list, index):
    for i in range(2):
        the_list.insert(index, the_list[index])
    return the_list


def palindrome_word(word):
    if word == word[::-1]:
        print('This word is a palindrome.')
    else: 
        print('This word is not a palindrome.')
    return ' '

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    sentence = sentence.lower()
    punc = ['.',',','.',';',':','!','?']
    for i in range(len(punc)+1):
        sentence = sentence.strip(punc[i])
    sentence = sentence.strip()
    if sentence == sentence[::-1]:
        print('This word is a palindrome.')
    else: 
        print('This word is not a palindrome.')
    return ''

def main():
    '''
    The main function that returns when you run the code.
    '''
    #the_list = []
    #indeces = int(input('Please enter the number of elements in your list: '))
    #for i in range(0,indeces):
    #    element1 = int(input('Please enter an integer for element ' + str(i+1) + ': '))
    #    the_list.append(element1)

    #beginning2 = int(input('Please enter a beginning index: '))
    #end2 = int(input('Please enter an ending index: '))

    #index3 = int(input('Please enter the index integer: ')) 

    #word4 = input('Please enter a word: ')
    #print(first_and_last(the_list))
    #print(part_reverse(the_list, beginning, end))
    #print(repeat_at_index(the_list, index3))
    #print(palindrome_word(word4))
    sentence = 'Hello! How are you?'
    sentence = sentence.lower()
    punc = ['.',',','.',';',':','!','?']
    #for i in range(len(punc)+1):
    #sentence = sentence.strip(punc[i])
    sentence = sentence.strip()
    print(sentence)
    print(pun[2])

if __name__ == '__main__':
    main()