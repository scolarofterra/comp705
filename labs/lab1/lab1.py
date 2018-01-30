"""
Travis Deschenes
UNHM COMP705 Lab 1
An Introduction to Python
Jan 24, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    exstring = "hello world" 
    return exstring

def give_me_an_integer():
    """
    This function returns an integer value
    """
    exint = 5
    return exint

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    questoin = True
    return questoin

def give_me_a_float():
    """
    This function returns a float value
    """
    pi = 3.14
    return pi

def give_me_a_list():
    """
    This function returns a list
    """
    dragon = ["Tao","Draco","thoron","Ancalagon"] 
    return dragon

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    Tolkin = {"elf":"Elrond", "Human":"Aregon","hobit":"frodo","Dragon":"Ancalagon"}
    return Tolkin

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    tup = 'hello', 'spartian', 117

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    pass

def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    num = number

    if(num % 2 == 0) :num
    	return True

    else:
    	return False

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    num1 = number1
    num2 = number2
    if(num1 < num2) :
    	return True

    else:
    	return False
