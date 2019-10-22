'''
Practicing functions
'''
'''
1)  Write a function that adds 1 
    to the input and prints the result.
'''
def inc(a):
    a += 1
    #Could use a = a + 1, but this rewrites a
    print('The output of function 1 for your input is:', a)

'''
2)  Write a function that adds 1
    to the input and returns the result.
'''
def inc_return(a):
    a += 1
    return a

'''
3)  Write a function that adds
    the two input numbers together
    and returns the sum.
'''
def sum(a, b):
    sum = a + b
    return sum

'''
4)  Write a function that takes two
    numbers, adds them together using 
    sum() and then increments the sum
    using inc_return.
'''
def sum_inc(a, b):
    sum_ab = sum(a,b)
    sum_inc = inc_return(sum_ab)
    return sum_inc

'''
5)  Write a function that returns a 
    boolean (True or False) for whether 
    the input number is even
'''
def is_even(a):
        return (bool(a % 2 == 0))

'''
6)  Create for loop that takes a string
    and an integer and returns a new string 
    that is the string repeated equal to 
    integer
    e.g. string_repeat('ho', 3) returns
    'hohoho'.
'''
def string_repeat(phrase, repeat):
    for i in range(repeat):
        concatenate = (i+1) * phrase 
    return concatenate

def main():
    '''
    The main function that returns when you run the code.
    '''
    phrase=input('Please enter a string to be repeated: ')
    repeat=int(input('Please enter an integer number of repeats: '))
    print(string_repeat(phrase,repeat))

if __name__ == '__main__':
    main()