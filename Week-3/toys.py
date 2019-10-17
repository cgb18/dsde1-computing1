'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''
import sys

# write a function that adds 1
# to the input and prints the result
def inc(a):
    a += 1
    #a = a + 1
    print('The output of function 1 for input a=5 is:', a)

inc(5)

# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    a += 1
    return a # hint this is incomplete

print('The output of function 2 for input a=5 is: ' + str(inc_return(5)))

# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    sum = a + b
    return sum

print('The output of function 3 for inputs a=10, b=5 is: ', str(sum(10,5)))

# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    sum_ab = sum(a,b)
    sum_inc = inc_return(sum_ab)
    return sum_inc

print('The output of function 4 for inputs a=10, b=5 is: ' + str(sum_inc(10,5)))

# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
        return (bool(a % 2 == 0))

print('The output of function 5 for inputs a=101 is: ' + str(is_even(101)))

# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    for i in range(repeat):
        concatenate = (i+1) * phrase 
    # hint: you can add strings together 
    # in order to concatenate them
    return concatenate

print('The output of function 6 is for inputs phrase=Hello! , b=6 is: ', str(string_repeat('Hello! ', 6)))