#!/usr/bin/env python3

import hw4_solution as sol
import nose.tools 
# --------------------------------------------------------------------
# Problem 1
# 
# Create a function, is_odd, that takes a number and returns True if
# that number is odd.
# 
# Function: is_odd
# 
# parameters:
# - number
#
# returns: boolean
def test_is_odd():
    assert sol.is_odd(0) == False
    assert sol.is_odd(1) == True
    assert sol.is_odd(5) == True
    assert sol.is_odd(6) == False
    assert sol.is_odd(-5) == True
    assert sol.is_odd(3.14) == False
    assert sol.is_odd(3*3000) == True


# --------------------------------------------------------------------
# Problem 2
# 
# Create a function, is_even, that takes a number and returns True if
# that number is even. 
# 
# Function: is_even
# 
# parameters:
# - number
#
# returns: boolean
def test_is_even():
    assert sol.is_even(0) == True
    assert sol.is_even(1) == False
    assert sol.is_even(5) == False
    assert sol.is_even(6) == True
    assert sol.is_even(-6) == True
    assert sol.is_even(3.14) == False
    assert sol.is_even(4*3000) == True

# --------------------------------------------------------------------
# Problem 3
# 
# Create a function, is_mult_of_four, that takes a number and returns
# True if that number is a multiple of four. 
# 
# Function: is_mult_of_four
# 
# parameters:
# - number
#
# returns: boolean
def test_is_mult_of_four():
    assert sol.is_mult_of_four(4) == True
    assert sol.is_mult_of_four(-4) == True
    assert sol.is_mult_of_four(0) == True
    assert sol.is_mult_of_four(3) == False
    assert sol.is_mult_of_four(2*6000) == True
    assert sol.is_mult_of_four(4.7) == False
    

# --------------------------------------------------------------------
# Problem 4
# 
# Create a function, is_mult_of_x, that takes a number and a divisor
# and returns True if that number is divisible by divisor
# 
# Function: is_mult_of_divisor
# 
# parameters:
# - number
# - divisor
#
# returns: boolean
def test_is_mult_of_x():
    assert sol.is_mult_of_x(0,3) == True
    assert sol.is_mult_of_x(0,-3) == True
    assert sol.is_mult_of_x(4,2) == True
    assert sol.is_mult_of_x(-6,3) == True
    assert sol.is_mult_of_x(-4,-2) == True
    assert sol.is_mult_of_x(3,1) == True
    assert sol.is_mult_of_x(4.3,1) == False
# --------------------------------------------------------------------
# Problem 5
# 
# Given a string s, return a string made of the first 2 and the last 2
# chars of the original string, so 'spring' yields 'spng'. However, if
# the string length is less than 2, return instead the empty string.
#
# Function: both_ends
#
# parameters:
# - s
#
# returns: string
def test_both_ends():
    assert sol.both_ends('spring') == 'spng'
    assert sol.both_ends('book') == 'book'
    assert sol.both_ends('fox') == 'foox'
    assert sol.both_ends('at') == 'atat'
    assert sol.both_ends('a') == ''
    assert sol.both_ends('') == ''


