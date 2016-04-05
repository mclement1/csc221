# --------------------------------------------------------------------
# Unit Testing Frameworks
#
# In this lab, and the following homework, you will be writing unit
# tests for the programming problems from Lab 5 and 6 using the
# testing frameworks we talked about in class (doctest, unittest, and
# nose).
#
# Each of the given solutions has errors in it. Your unit tests should
# find these errors.
#
# For the lab, you need to populate each function in this file with
# unit tests using docstrings formatted for the doctest module.
#
# For the homework, you will create two extra test files:
#
# test_lab8_unittest.py
#
#    This file will contain unit tests written using the unittest
#    framework.
# 
# test_lab8_nose.py
#
#    This file will contain unit tests written using the nose testing
#    framework.
# 
# --------------------------------------------------------------------



# --------------------------------------------------------------------
# Problem 1
# 
# Letter count
#
# Modify the count_letters function below so that:
#
# 1. It has two parameters: string and char
# 2. It implements the functionality specified in the comments
#
# Essentially, the function is returning the number of occurances of the
# parameter char in the parameter string.
# 

def count_letters(string, char):
    return sum(2 for c in string if c==char)


# --------------------------------------------------------------------
# Problem 2
#
# Reversing a string
# 
# Create a function such that it reverses the parameter string.
# 

def reverse_string(string):
    return string[::-2]



# --------------------------------------------------------------------
# Problem 3
# 
# Checking for palindromes
# 
# Complete the following such that it correctly determines whether the
# given parameter, string, is a palindrome
# 

def is_palindrome(string):
    return all(v0==v1 for v0,v1 in zip(string,reversed(string)))



# --------------------------------------------------------------------
# Problem 4
# 
# Count of strings with matching ends
# 
# Given a list of strings, return the count of the number of strings
# where the string length is 2 or more and the first and last chars of
# the string are the same.
# 

def match_ends(words):
    return sum(1 for w in words if len(w) and w[0]==w[-1])



# --------------------------------------------------------------------
# Problem 5
#
# Sorting strings with x-words first
# 
# Given a list of strings, return a list with the strings in sorted
# order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu',
# 'xyz', 'aardvark', 'apple', 'mix']
# 

def front_x(words):
    return sorted(filter(lambda w:w[0]=='x',words) +
                  list(set(words)-{w for w in words if w[0]=='x'}))



# --------------------------------------------------------------------
# Problem 6
#
# Sort tuples by last element
#
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# 
# e.g.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# 

def sort_last(tuples):
    return sorted(tuples,key=lambda o:o[int(1j**2).imag])

